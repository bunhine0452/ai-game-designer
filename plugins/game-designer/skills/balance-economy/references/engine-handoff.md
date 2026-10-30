# Handing design numbers to an engine

The design table stays the **source of truth**. The engine gets a generated copy, and every
generated file names its source. When a number changes, edit the table and re-export. Never
hand-edit the engine copy, or design and build drift apart silently.

## The pipeline

1. Finalize the table with the other scripts (cost curve fit, economy sim, progression).
2. Export it: `python3 scripts/export_engine.py <table> --name <Row> --engine <engine> --out <dir>`.
3. Commit the table and the generated files together, so a diff shows the design change and its
   effect in the same commit.
4. In the engine, load the data through the generated loader. Write gameplay code against the
   typed row, never against raw dictionaries.

## What each target gets

| Engine | Files | How to use them |
|---|---|---|
| Godot 4 | `<row>_def.gd` (`class_name <Row>Def extends Resource`), `<rows>.json`, `<row>_db.gd` | Put the JSON in `res://data/`, then call `<Row>Db.load_rows()` to get `Array[<Row>Def]`. Resources also show up in the inspector. |
| Unity | `<Row>Row.cs` (`[Serializable]`), `<Row>Table.cs` (`ScriptableObject`), `<rows>.json` | Create the table asset (Assets → Create → Design Data), then call `LoadFromJson(textAsset)` from an editor button or at startup. The JSON keys match the C# field names, because `JsonUtility` maps by name. |
| Unreal 5 | `<Row>Row.h` (`USTRUCT : FTableRowBase`), `<rows>_datatable.csv` | Add the header to a module and compile, then import the CSV as a DataTable with that row struct. The first column `Name` is the row key. A column that was also called `name` becomes `DisplayName`. |
| Any | `<rows>.json` with `_source` and typed `rows` | For web prototypes, tools and spreadsheets. |

Types are inferred per column: whole numbers become `int`, other numbers `float`,
true/false/yes/no `bool`, and everything else a string. Store flags as 0/1 when the balance
scripts need numbers. They export as `int`, which every engine reads.

## Working with engine MCP servers

Several community MCP servers let an agent drive an engine editor directly. Examples include
Godot and Unity bridges and multi-engine plugins. They're useful for the step after export:
placing the data asset, wiring it to a scene, and running the game. Keep the split clear:

- **This plugin decides the numbers** and checks them (simulators, curves, reviews).
- **The engine MCP server applies them**: it creates assets, edits scenes and runs playtests.

Ask the engine-side agent to import the generated files rather than retype numbers. Ask it to
report back anything it had to change, so the design table can be updated too. These servers
are third-party projects. Review what each one can do in your editor before you install it.

## Checklist before hand-off

- [ ] Every value in the table is final, or marked `placeholder` in a notes column.
- [ ] Column names are stable. Renaming one breaks code that uses the generated field.
- [ ] IDs are unique (a duplicate row name in Unreal gets a suffix, which hides the clash).
- [ ] The playtest build reads the generated file, not a hand-copied constant.

## Sources
- [C2] Schreiber & Romero (2021), *Game Balance* (spreadsheets as the source of truth).
- [B2] Giovannetti (2019), *Slay the Spire: Metrics Driven Design and Balance* (GDC).
- Full bibliography: `research/SOURCES.md` in the repository.
