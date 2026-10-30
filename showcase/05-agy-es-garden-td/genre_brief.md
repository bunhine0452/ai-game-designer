# Brief de Género: Jardín de Guardianes

**Documento de Diseño de Género para Plataformas Móvil y PC**  
*Título provisional:* **Jardín de Guardianes**  
*Género principal:* **Defensa de torres (Tower Defense)**  
*Formato:* Multiplataforma (Móvil iOS/Android y PC Steam)  

---

## 1. Identificación del Género y Marco Conceptual

*Jardín de Guardianes* se sitúa en el núcleo del género de **defensa de torres (Tower Defense)** con una estructura híbrida de caminos tácticos fijos combinada con gestión ambiental viva y un **bucle meta (Meta Loop)** de progresión botánica.

### Bucle Principal (Core Loop)
El flujo momento a momento sigue la cadencia clásica perfeccionada del género:
$$\text{Vista previa de la oleada} \longrightarrow \text{Inversión de Néctar (colocación/mejora)} \longrightarrow \text{Resolución dinámica de la oleada (con microhabilidades)} \longrightarrow \text{Cosecha de recursos} \longrightarrow \text{Adaptación táctica y siguiente oleada}$$

### Pilares de Diseño (Design Pillars)
1. **Ecosistema Simbiótico:** Las plantas no son torretas mecánicas aisladas; cooperan mediante polinización cruzada, raíces compartidas y sinergias elementales (Agua, Clorofila, Espinas y Polen).
2. **Claridad Táctica Inmediata:** Legibilidad instantánea tanto en pantallas móviles pequeñas como en monitores de PC de alta resolución.
3. **Agencia Activa:** El jugador nunca es un espectador pasivo durante la oleada; cuenta con habilidades de jardinero y selección priorizada de objetivos.

---

## 2. Convenciones que Respetar (Expectativas Fundamentales)

En el diseño de una **defensa de torres (Tower Defense)**, los jugadores veteranos y noveles comparten alfabetización lúdica. Violar estas expectativas genera frustración e incomprensión:

1. **Arquetipos de Torres Claros e Inmediatamente Legibles:**
   - *Daño a objetivo único:* Proyectiles continuos de cadencia media/alta para desgastar unidades estándar.
   - *Daño en área (Area of Effect - AoE):* Explosiones o salpicaduras lentas para castigar enjambres de plagas.
   - *Control de masas (Crowd Control - CC):* Ralentización (savia o rocío helado), aturdimiento y enredo de raíces.
   - *Soporte y Economía:* Unidades generadoras de moneda activa como el girasol o potenciadores de aura.
   *Norma:* Ninguna torre debe ocultar su función básica tras nombres abstractos; la silueta vegetal debe comunicar su rol de un vistazo.

2. **Telegrafiado (Telegraphed) Riguroso de Amenazas y Rutas:**
   - Visualización explícita del camino que seguirán las plagas antes de que comience la oleada.
   - Indicadores previos de composición de la oleada (por ejemplo: iconos que avisan de orugas blindadas, pulgones rápidos o polillas voladoras).
   - El jugador debe saber exactamente *a qué se enfrenta* para que la derrota se sienta siempre como un error propio de planificación y nunca como una trampa injusta.

3. **Retroalimentación Espacial y Rangos Transparentes:**
   - Mostrar el círculo de alcance exacto y la zona de impacto al tocar/hacer clic en una casilla o en una planta antes de gastar recursos.
   - Cojines de colisión claros: no permitir solapamientos confusos entre torres o sobre la ruta de plagas, salvo que se trate de plantas de suelo específicas (como enredaderas trampa).

4. **Tolerancia a Fugas (Vidas de la Huerta) y Ritmo de Oleadas:**
   - Contador de fugas permisible (típicamente 10-20 vidas/flores del huerto), permitiendo errores parciales sin provocar un reinicio total inmediato.
   - Botón de aceleración ($1\times$, $2\times$, $3\times$) y pausa táctica disponible tanto en móvil como en PC.

---

## 3. Convenciones que Romper (Oportunidades de Diferenciación)

Para evitar ser un clon genérico de *Plants vs. Zombies* o *Kingdom Rush*, *Jardín de Guardianes* rompe convenciones específicas apoyándose en su temática orgánica:

### Oportunidad 1: Romper la Torre Estática e Inanimada $\rightarrow$ Simbiosis y Polinización de Vecindad
- *Convención clásica:* Cada torre actúa de forma matemática independiente en su rango circular.
- *Innovación:* **Simbiosis Vegetal**. Las plantas que comparten casillas adyacentes generan lazos de micelio y polen. Colocar una planta de flor junto a un cactus espinoso añade veneno de polen a sus espinas; un lirio de agua junto a un brote amplía la cadencia de disparo. El posicionamiento se convierte en un rompecabezas de combinatoria botánica y no solo de cobertura geométrica.

### Oportunidad 2: Romper la Moneda Abstracta Estática $\rightarrow$ Ciclo Biológico de Recursos (Sol y Agua Subterránea)
- *Convención clásica:* El oro se obtiene pasivamente por muerte de enemigos y se acumula indefinidamente sin interacción con el mapa.
- *Innovación:* **Gestión de Recursos Vivos**. Existen dos monedas con dinámicas opuestas:
  - *Néctar Solar (moneda rápida):* Generado por flores diurnas y bajas de enemigos, decae si no se invierte rápidamente, incentivando el gasto activo.
  - *Agua de Riego (moneda de flujo/sumidero):* Un recurso que fluye por canales del jardín. Ciertas torres de alto impacto demandan conexión a la red de humedad del suelo, añadiendo una capa de logística territorial.

### Oportunidad 3: Romper la Pasividad con Herramientas de Jardinero
- *Convención clásica:* Esperar a que la barra de tiempo o los disparos automáticos limpien la oleada.
- *Innovación:* **Herramientas de Terreno en Tiempo Real**. El jugador puede podar (recuperar el 80% de recursos al instante para reubicar), abonar (sobrecargar temporalmente una planta con un toque/clic) o fertilizar casillas de tierra para aumentar permanentemente las estadísticas de quien se plante allí.

---

## 4. Forma del Ritmo (Pacing) y Curva de Interés (Interest Curve)

El **ritmo (Pacing)** se diseña en dos escalas complementarias: dentro del nivel individual y a lo largo de la campaña.

```
Intensidad
  ▲
  │                                           [Clímax: Jefe Pulgón Titán]
  │                                                       ▲
  │                            [Oleada 7: Enjambre Mixto] │
  │                                        ▲              │
  │                   [Oleada 4: Aéreos]   │   (Alivio)   │
  │                           ▲            │     ▼        │
  │        [Oleada 1: Lenta]  │  (Alivio)  │              │
  │               ▲           │    ▼       │              │
  │ (Planificación)    (Alivio)                           │    [Victoria]
──┴───────●───────────────●────────────────●──────────────●─────────► Tiempo
```

### Ritmo en el Nivel (Nivel típico de 10 oleadas, duración 4–6 minutos)
1. **Fase de siembra inicial (0–30 s):** Tensión baja. El jugador analiza la ruta, coloca sus plantas iniciales económicas y ofensivas básicas.
2. **Oleadas 1 a 3 (Enseñanza / Contacto):** Tensión ascendente suave. Plagas lentas que validan la defensa básica.
3. **Oleadas 4 a 6 (Adaptación y Ruptura):** Primer pico de tensión. Se introducen plagas voladoras o con coraza dura que esquivan la estrategia inicial, forzando la compra de torres especializadas.
4. **Oleadas 7 a 9 (Saturación y Prueba de Resistencia):** Combinación de enjambres rápidos y tanques pesados. Exige uso de microhabilidades y gestión del agua.
5. **Oleada 10 (Clímax):** Entrada del jefe de bioma (ej. Caracol Acorazado o Avispón Reina) con habilidades de alteración de terreno.
6. **Resolución y Alivio:** Cosecha de semillas y **esencia botánica (XP)** para el progreso meta.

### Ritmo de Campaña
- Cadencia de introducción: una torre o plaga nueva cada 1 o 2 niveles (siguiendo la regla de oro de George Fan en *Plants vs. Zombies*).
- Biomas estructurados:
  - *Mundo 1: El Huerto Soleado* (Mecánicas puras y fundamentos).
  - *Mundo 2: El Invernadero Brumoso* (Gestión de humedad y plagas aéreas).
  - *Mundo 3: La Jungla Tropical* (Simbiosis botánica y terreno fértil).
  - *Mundo 4: El Pantano Umbrío* (Plagas resistentes, hongos y raíces subterráneas).

---

## 5. Lista de Fallos Típicos del Género (Failure Modes Checklist)

A continuación se auditan los fallos de diseño más comunes en el género, evaluando el estado de riesgo para *Jardín de Guardianes* y la solución aplicada:

| Fallo Común de Género | Nivel de Riesgo | Causa Raíz en TD | Mitigación Concreta en Jardín de Guardianes |
|---|---|---|---|
| **Estrategia dominante (Dominant Strategy)** | **ALTO RIESGO** | Una combinación de torre/colocación es tan rentable que anula cualquier otra decisión. | Auditoría matemática con **curva de coste (Cost Curve)** para evitar unidades subcosteadas; matriz intransitiva de debilidades de plagas (p. ej., orugas blindadas reducen 70% daño cortante pero son vulnerables a ácido de setas). |
| **Observación pasiva (Passive Watching)** | **ALTO RIESGO** | Oleadas largas sin decisiones intermedias provocan aburrimiento y desconexión. | Microhabilidades de jardinero (abono exprés, poda y trasplante activo) y selector de objetivo prioritario en tiempo real (más cercano, más fuerte, aéreos). |
| **Fallo ilegible (Unreadable Failure)** | **MEDIO** | Los enemigos traspasan la meta sin que el jugador comprenda qué falló en su línea defensiva. | Iconografía de daño flotante codificada por colores (gris = daño mitigado por armadura; rojo = crítico/vulnerable; azul = ralentización). Repetición de los últimos 5 segundos en cámara lenta si se pierde el nivel. |
| **Sobrecarga de información (Information Overload)** | **MEDIO** | Entregar demasiadas opciones de torres simultáneas abruma al jugador en fases tempranas. | Límite estricto de baraja/semillero activo (máximo 5 a 7 plantas por partida), desbloqueadas de 1 en 1 a lo largo de la campaña. |
| **Saturación visual en fase tardía (Visual Clutter)** | **ALTO RIESGO** | Decenas de proyectiles y partículas simultáneas provocan caídas de tasa de fotogramas (FPS) en móviles y caos en pantalla. | Sistema de proyectiles agrupados y límite de partículas en renderizado móvil; efectos de área marcados en el suelo en lugar de proyectiles infinitos. |
| **Fricción de control móvil vs. PC** | **MEDIO** | Controles pensados solo para ratón que se sienten torpes en pantalla táctil o viceversa. | En móvil: arrastre y suelta magnético con área de toque amplia. En PC: atajos de teclado numérico (1–7 para seleccionar planta, Espacio para pausar/acelerar). |

---

## 6. Juegos de Referencia y Lecciones Aprendidas

| Título de Referencia | Mecánica Sobresaliente | Lección de Diseño Clave para Jardín de Guardianes |
|---|---|---|
| **Plants vs. Zombies** | Curva de aprendizaje y carisma visual. | **Pedagogía invisible:** jamás abrumar al jugador; cada nivel presenta un solo elemento nuevo y lo convierte en el problema central de ese mapa. |
| **Kingdom Rush** | Microgestión activa y héroes. | **Agencia constante:** el juego no se juega solo; las habilidades activas de recarga corta mantienen las manos en la pantalla. |
| **Bloons TD 6** | Ramas de mejora y sinergias profundas. | **Diversidad de variantes:** cada torre debe tener roles claramente diferenciados en sus niveles avanzados (p. ej., control vs. DPS puro). |
| **Defense Grid: The Awakening** | Geometría y legibilidad de ruta. | **La spatialidad como puzle:** el valor de una posición depende directamente de cuánto tiempo tiene la torre para disparar a lo largo del trazado. |

---

## 7. Preguntas de Diseño Abiertas para el Equipo

1. ¿Permitiremos que las plagas ataquen y devoren las plantas (estilo carril PvZ) o las plantas serán inmunes e intangibles en los márgenes del camino (estilo clásico Kingdom Rush/Bloons)?  
   *Recomendación:* Intangibles en el borde para el 90% de las torres, pero con plantas de bloqueo especiales (Calabazas, Enredaderas) que se coloquen dentro de la ruta y tengan barra de salud.
2. ¿Cómo se equilibra la duración de la partida entre móvil (3–4 minutos) y PC (6–8 minutos)?  
   *Recomendación:* Misma estructura de oleadas, pero con selector de velocidad $2\times$ activable desde la oleada 1 en móvil y campañas de desafíos extendidos en PC.
3. ¿El sistema de energía o vidas meta debe existir en la versión móvil?  
   *Recomendación ética:* Evitar sistemas punitivos de energía que impidan jugar; monetizar mediante cosméticos de jardín y expansiones de niveles prémium.
