# Análisis de la Curva de Costes y Equilibrio de Torres (12 Guardianes)

**Proyecto:** Jardín de Guardianes  
**Módulo:** Balance Transitivo y Curva de Costes de Unidades  
**Herramienta de cálculo:** `scripts/cost_curve.py`  
**Archivos de datos asociados:**  
- Datos brutos iniciales: [`towers_cost_data.csv`](towers_cost_data.csv)  
- Ajuste y residuos iniciales: [`towers_cost_data_fit.csv`](towers_cost_data_fit.csv) y [`towers_cost_data_report.md`](towers_cost_data_report.md)  
- Datos y ajuste rebalanceados: [`towers_rebalanced_data.csv`](towers_rebalanced_data.csv) y [`towers_rebalanced_data_report.md`](towers_rebalanced_data_report.md)

---

## 1. Fundamento Teórico: Balance Transitivo y Curva de Coste

En el diseño de sistemas de juego, el **equilibrio del juego (Game Balance)** de carácter **transitivo (Transitive Balance)** establece que a mayor coste pagado en recursos dentro de la partida (Néctar Solar), mayor debe ser la potencia efectiva de la torre a lo largo de una **curva de coste (Cost Curve)** predecible.

Siguiendo el método formal de Ian Schreiber (*Game Balance Concepts*), el coste justo de cada unidad se define como:
$$\text{Coste Justo} \approx \text{Intersección Base} + \sum (\text{Peso}_i \times \text{Atributo}_i)$$
Donde la **intersección (Intercept)** representa el derecho de suelo/siembra de ocupar una casilla del jardín, y cada peso representa el valor en Néctar de un punto de esa estadística.

Las torres que se desvían drásticamente de esta relación generan patologías graves:
- **Residuo (Residual) positivo ($\text{Justo} - \text{Real} > 0$):** La torre está **subcosteada (Undercosted)** (demasiado fuerte para lo que cuesta $\rightarrow$ amenaza de estrategia dominante).
- **Residuo negativo ($\text{Justo} - \text{Real} < 0$):** La torre está **sobrecosteada (Overcosted)** (demasiado débil para lo que cuesta $\rightarrow$ trampa de recursos inútil).

---

## 2. Conjunto Inicial de 12 Torres de Jardín

Se seleccionó un elenco de 12 torres guardianas con roles tácticos diferenciados (daño continuo, artillería, control de masas, daño melé concentrado y soporte):

| Nombre de la Torre | Rol Táctico | Coste Real | Daño por Segundo (DPS) | Rango (Casillas) | Radio de Área (AoE) | Ralentización (% Slow) |
|---|---|:---:|:---:|:---:|:---:|:---:|
| **Brote Guisante** | Hostigador básico inicial | **110** | 22 | 3.0 | 0.0 | 0% |
| **Cactus Espinoso** | DPS sostenido a distancia | **150** | 36 | 4.0 | 0.0 | 0% |
| **Planta Carnívora** | Daño melé masivo concentrado | **175** | 65 | 1.5 | 0.0 | 0% |
| **Rosa Francotiradora** | Francotirador aéreo/terrestre | **205** | 50 | 5.5 | 0.0 | 0% |
| **Seta Esporífera** | Salpicadura de veneno | **190** | 30 | 3.0 | 1.8 | 0% |
| **Calabaza Bomba** | Mortero explosivo de impacto | **230** | 45 | 2.5 | 2.4 | 0% |
| **Lirio Glacial** | Control de masas puro | **185** | 10 | 3.2 | 1.2 | 45% |
| **Girasol Radiante** | Economía y ralentización leve | **95** | 8 | 2.0 | 0.0 | 25% |
| **Diente de León Céfiro** | Antiaéreo y hostigador veloz | **190** | 25 | 5.0 | 1.0 | 10% |
| **Sauce Protector** | Bastión defensivo de área | **245** | 20 | 3.5 | 2.0 | 50% |
| **Mazorca Cañonera** | Artillería pesada masiva *(Sospechosa)* | **140** | 55 | 4.5 | 2.0 | 0% |
| **Orquídea Real** | Soporte de lujo místico *(Sospechosa)* | **310** | 22 | 3.5 | 0.8 | 20% |

---

## 3. Diagnóstico del Ajuste Robusto y Detección de Valores Atípicos

El script `cost_curve.py` se ejecutó con el modificador `--robust` para evitar que los **valores atípicos (Outliers)** deformen completamente el patrón general del resto de torres:

### Pesos Ajustados por Regresión (Coste en Néctar por Unidad de Atributo)
- **Intersección base (Intercept):** $+68.40\text{ Néctar}$ (coste de implantación en casilla).
- **DPS (Daño por segundo):** $+1.34\text{ Néctar por punto de DPS}$.
- **Rango (Alcance en casillas):** $+7.50\text{ Néctar por casilla de alcance}$.
- **Radio de Área (AoE):** $+21.22\text{ Néctar por casilla de radio de salpicadura}$.
- **Ralentización (% Slow):** $+1.29\text{ Néctar por cada 1% de reducción de velocidad}$.

### Tabla de Residuos y Veredictos del Script Oficial
*(Umbral automático de bandera: $\pm 1.5 \times \text{RMSE} = \pm 75.69\text{ Néctar}$)*

| Torre | Coste Real | Coste Justo | Residuo ($\text{Justo} - \text{Real}$) | Veredicto Oficial | Estado de Balance |
|---|:---:|:---:|:---:|---|---|
| **Mazorca Cañonera** | **140** | **218.40** | **$+78.40$** | `undercosted (too strong)` | **Desequilibrio crítico (Rota)** |
| **Orquídea Real** | **310** | **167.00** | **$-143.00$** | `overcosted (too weak)` | **Desequilibrio crítico (Trampa)** |
| Girasol Radiante | 95 | 126.45 | $+31.45$ | `on curve` | Dentro de rango natural |
| Brote Guisante | 110 | 120.42 | $+10.42$ | `on curve` | Equilibrada |
| Lirio Glacial | 185 | 189.45 | $+4.45$ | `on curve` | Equilibrada |
| Cactus Espinoso | 150 | 146.70 | $-3.30$ | `on curve` | Equilibrada |
| Planta Carnívora | 175 | 166.88 | $-8.12$ | `on curve` | Equilibrada |
| Diente de León Céfiro | 190 | 173.59 | $-16.41$ | `on curve` | Equilibrada |
| Sauce Protector | 245 | 228.56 | $-16.44$ | `on curve` | Equilibrada |
| Seta Esporífera | 190 | 169.36 | $-20.64$ | `on curve` | Equilibrada |
| Rosa Francotiradora | 205 | 176.74 | $-28.26$ | `on curve` | Equilibrada |
| Calabaza Bomba | 230 | 198.47 | $-31.53$ | `on curve` | Equilibrada |

---

## 4. Análisis Profundo de las Torres Mal Costeadas

### Anomalía 1: Mazorca Cañonera (Subcosteada / Rota)
- **Problema de diseño:** Ofrece estadísticas de nivel de artillería pesada (DPS 55, alcance 4.5 casillas, radio de explosión 2.0 casillas) por solo **140 de Néctar**. Su coste justo es de **218.40** en el modelo general y de **268.50** frente a las 10 torres base.
- **Impacto destructivo en el juego:**
  - Crea una **estrategia dominante (Dominant Strategy)** inmediata. Cualquier jugador que desbloquee la Mazorca Cañonera deja de utilizar torres de objetivo único como la *Rosa Francotiradora* (coste 205) o de impacto corto como la *Calabaza Bomba* (coste 230), ya que la Mazorca resuelve tanto enjambres como enemigos medianos a menor precio.
  - Provoca el "síndrome de agua en la grieta" (Soren Johnson): los jugadores optimizarán la diversión fuera del juego llenando el tablero de Mazorcas porque es matemáticamente superior.
- **Acción correctora propuesta:**
  - *Opción A (Ajuste de Coste - Recomendada):* Subir su coste de siembra de **140 a 270 de Néctar**.
  - *Opción B (Ajuste de Estadísticas):* Mantener el coste en 140 pero reducir su DPS de 55 a 30 y su radio de área de 2.0 a 1.2 casillas.

### Anomalía 2: Orquídea Real (Sobrecosteada / Trampa de Recursos)
- **Problema de diseño:** Comercializada como planta de prestigio místico de alto nivel con un coste prohibitivo de **310 de Néctar**, pero sus prestaciones reales (DPS 22, alcance 3.5, área 0.8 y ralentización del 20%) apenas justifican un coste justo de **167.00 de Néctar**.
- **Impacto destructivo en el juego:**
  - Funciona como una **trampa para novatos (Noob Trap)**. Los jugadores ahorran recursos durante oleadas críticas para plantar una Orquídea Real esperando resolver la partida, solo para ver cómo las plagas se escapan debido a su deficiente rendimiento de daño y control.
  - Provoca frustración y sensación de fracaso injusto, dañando la retención de usuarios en móvil y las reseñas en PC.
- **Acción correctora propuesta:**
  - *Opción A (Ajuste de Coste - Recomendada):* Rebajar su coste de **310 a 170 de Néctar**, colocándola a la par de torres de soporte táctico medio.
  - *Opción B (Revalorización de Estadísticas):* Mantener el coste en 310, pero dotarla de una habilidad de aura que otorgue $+30\%$ de daño a todas las plantas en 2 casillas a la redonda y aumentar su ralentización al $50\%$.

---

## 5. Validación del Modelo Rebalanceado

Se generó un conjunto corregido (`towers_rebalanced_data.csv`) aplicando las correcciones recomendadas (**Mazorca Cañonera coste 270**, **Orquídea Real coste 170**). Los resultados del script `cost_curve.py` demuestran la curación matemática del ecosistema:

```
Ajuste Inicial (Con Outliers):   R² = 0.212, RMSE = 50.46
Ajuste Rebalanceado:             R² = 0.999, RMSE = 1.50
```

### Tabla de Ajuste Post-Rebalanceo

| Torre | Coste Rebalanceado | Coste Justo | Residuo | Veredicto |
|---|:---:|:---:|:---:|---|
| **Brote Guisante** | 110 | 108.31 | $-1.69$ | `on curve` |
| **Cactus Espinoso** | 150 | 152.35 | $+2.35$ | `undercosted (too strong)` *(Marginal: $+2$ coste)* |
| **Planta Carnívora** | 175 | 174.79 | $-0.21$ | `on curve` |
| **Rosa Francotiradora** | 205 | 203.45 | $-1.55$ | `on curve` |
| **Seta Esporífera** | 190 | 187.72 | $-2.28$ | `overcosted (too weak)` *(Marginal: $-2$ coste)* |
| **Calabaza Bomba** | 230 | 232.27 | $+2.27$ | `undercosted (too strong)` *(Marginal: $+2$ coste)* |
| **Lirio Glacial** | 185 | 184.92 | $-0.08$ | `on curve` |
| **Girasol Radiante** | 95 | 95.89 | $+0.89$ | `on curve` |
| **Diente de León Céfiro** | 190 | 191.68 | $+1.68$ | `on curve` |
| **Sauce Protector** | 245 | 244.18 | $-0.82$ | `on curve` |
| **Mazorca Cañonera (Corregida)** | **270** | **268.45** | **$-1.55$** | `on curve` |
| **Orquídea Real (Corregida)** | **170** | **168.80** | **$-1.20$** | `on curve` |

Con este rebalanceo:
1. El error cuadrático medio cae de **50.46 a 1.50**, indicando que las 12 torres siguen una economía lógica y coherente.
2. Cada torre tiene ahora un nicho táctico definido donde ninguna anula a las demás.
3. Se cumplen plenamente los criterios de Sirlin para un balance competitivo saludable: **opciones viables, justicia táctica y ausencia de estrategia dominante**.

---

## 6. Plan de Telemetría para Operaciones en Vivo (LiveOps)

Tras implementar estos valores en el prototipo jugable, se recomienda monitorizar los siguientes indicadores de telemetría:
1. **Tasa de Elección (Pick Rate) por Torre:** Si una torre supera el $40\%$ de presencia en barajas activas o cae por debajo del $5\%$, debe revisarse su coste o debilidades de plagas.
2. **Tasa de Victoria (Win Rate) Condicionada:** Si plantar Mazorca Cañonera incrementa el win rate de los mapas en más de $15\%$ respecto a no plantarla, requiere un ajuste fino.
3. **Distribución de Uso por Habilidad del Jugador:** Verificar si la Orquídea Real es ignorada por novatos y veteranos por igual, lo que indicaría falta de identidad mecánica más allá de sus números.
