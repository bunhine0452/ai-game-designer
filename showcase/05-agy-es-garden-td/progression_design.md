# Diseño de la Curva de Progresión de Torres (30 Niveles)

**Proyecto:** Jardín de Guardianes  
**Módulo:** Progresión de Maestría de Torres (30 Niveles)  
**Herramienta de cálculo:** `scripts/progression_curve.py`  
**Archivos de datos asociados:** [`tower_progression.csv`](tower_progression.csv) y [`tower_progression_report.md`](tower_progression_report.md)

---

## 1. Objetivos de Experiencia y Filosofía del Modelo

En un juego de **defensa de torres (Tower Defense)** para móvil y PC, los números de la **curva de progresión (Progression Curve)** definen directamente la psicología del jugador. Un error frecuente es diseñar tablas de experiencia abstractas sin calibrar el **tiempo por nivel (Time per Level)** real de juego.

### Metas de Diseño
1. **Sensación inicial rápida:** El nivel $1 \rightarrow 2$ debe completarse en la primera sesión corta de juego ($\approx 6$ minutos), recompensando al usuario con dopamina temprana y desbloqueos inmediatos.
2. **Capacidad total de juego (Total Cap Time):** Alcanzar el **nivel máximo (Level Cap)** (nivel 30) de una planta guardiana debe requerir aproximadamente **24 a 26 horas de juego activo**, un rango ideal para jugadores en PC y sesiones acumuladas en móvil.
3. **Distribución justa del esfuerzo:** El 50% de la experiencia acumulada debe alcanzarse alrededor del $75\% - 80\%$ del rango total de niveles (nivel 24), evitando que la mitad del juego se sienta estancada.
4. **Ausencia de muros artificiales:** Ningún salto entre niveles consecutivos debe superar una tasa de crecimiento de tiempo de $1.5\times$ (**muro de nivel (Level Wall)**). La subida más lenta no debe superar los 90–95 minutos por nivel en el juego tardío.

---

## 2. Formulación Matemática del Modelo

El modelo seleccionado es una **curva polinómica (Polynomial Curve)** con desplazamiento lateral (**desplazamiento (Offset)**), combinada con un crecimiento orgánico de los ingresos de recursos:

### Fórmula de Experiencia Requerida
$$\text{XP}(L \rightarrow L+1) = \text{base} \times \left( \frac{L + c}{1 + c} \right)^p$$
- $\text{base} = 120\text{ Esencia Botánica (XP para nivel 1}\rightarrow\text{2)}$
- $c = 4\text{ (Desplazamiento para suavizar los primeros 5 niveles)}$
- $p = 2.1\text{ (Exponente polinómico de crecimiento)}$

### Modelo de Ingresos por Hora (Income Model)
A medida que el jugador avanza de bioma (del Huerto al Pantano), supera oleadas con multiplicadores y completa desafíos de maestría, el rendimiento por hora crece:
$$\text{Ingreso}(L) = 1200 \times (1.045)^{L-1}\text{ XP/hora}$$
- Ingreso en nivel 1: $1.200\text{ XP/h}$
- Ingreso en nivel 30: $4.115\text{ XP/h}$ ($+243\%$ gracias a biomas de mayor dificultad)

---

## 3. Resumen de Métricas Clave

| Métrica de Progresión | Valor del Modelo | Evaluación de Diseño |
|---|---|---|
| **Experiencia Total (Nivel 1 a 30)** | **70.253 XP** | Volumen equilibrado para economía de recompensas. |
| **Tiempo Nivel $1 \rightarrow 2$** | **0.10 h (6.0 min)** | Perfecto para retención y primera sesión en móvil. |
| **Tiempo Nivel $29 \rightarrow 30$** | **1.53 h (92.0 min)** | Satisfactorio para maestría máxima sin volverse tedioso. |
| **Tiempo Total al Nivel Máximo** | **24.90 horas** | Cumple el objetivo de 25 horas por torre. |
| **Nivel del 50% de XP (Half-XP)** | **Nivel 24 de 30 (80%)** | Distribución armónica: fase inicial fluida, fase final de prestigio. |
| **Nivel más lento** | **92 min (Nivel 29)** | Muy por debajo del umbral de fatiga (120 min). |
| **Mayor salto de tiempo entre niveles** | **$1.40\times$ (Nivel 2 vs 1)** | Suave; ningún nivel genera frustración por bloqueo. |

---

## 4. Tabla Completa de Progresión (Niveles 1 a 30)

Los datos exactos generados por el script oficial se detallan a continuación:

| Nivel ($L$) | XP al Siguiente | XP Acumulada | Ratio Crecimiento | Ingreso (XP/h) | Horas en este Nivel | Horas Acumuladas | Hitos de Maestría Botánica |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|---|
| **1** | 120 | 0 | — | 1200.0 | 0.100 (6 min) | 0.00 | Planta desbloqueada (Semilla básica) |
| **2** | 176 | 120 | 1.467 | 1254.0 | 0.140 (8 min) | 0.10 | $+5\%$ Cadencia de disparo |
| **3** | 243 | 296 | 1.382 | 1310.4 | 0.186 (11 min) | 0.24 | $+5\%$ Rango de cobertura |
| **4** | 322 | 539 | 1.325 | 1369.4 | 0.235 (14 min) | 0.43 | Reducción de coste de siembra $-5$ |
| **5** | 412 | 861 | 1.281 | 1431.0 | 0.288 (17 min) | 0.66 | **Hito Menor:** Habilidad Pasiva de Riego |
| **6** | 514 | 1273 | 1.247 | 1495.4 | 0.344 (20 min) | 0.95 | $+6\%$ Daño base |
| **7** | 628 | 1787 | 1.221 | 1562.7 | 0.402 (24 min) | 1.29 | $+5\%$ Duración de ralentización |
| **8** | 754 | 2415 | 1.200 | 1633.0 | 0.461 (28 min) | 1.70 | Radio de salpicadura $+0.2$ casillas |
| **9** | 892 | 3169 | 1.183 | 1706.5 | 0.523 (31 min) | 2.16 | Descuento de mejora en partida |
| **10** | 1043 | 4063 | 1.168 | 1783.3 | 0.585 (35 min) | 2.68 | **Hito Mayor 1:** Rama de Especialización A/B |
| **11** | 1206 | 5106 | 1.156 | 1863.6 | 0.647 (39 min) | 3.27 | $+7\%$ Daño contra blindados |
| **12** | 1381 | 6312 | 1.145 | 1947.4 | 0.709 (42 min) | 3.91 | Penetración de armadura ligera |
| **13** | 1569 | 7693 | 1.136 | 2035.1 | 0.771 (46 min) | 4.62 | Aura de polen a plantas adyacentes |
| **14** | 1770 | 9262 | 1.128 | 2126.6 | 0.832 (50 min) | 5.39 | $+8\%$ Daño crítico botánico |
| **15** | 1983 | 11032 | 1.120 | 2222.3 | 0.892 (53 min) | 6.23 | **Hito Menor:** Resistencia a toxinas de plagas |
| **16** | 2206 | 13015 | 1.114 | 2322.4 | 0.950 (57 min) | 7.12 | $+10\%$ Daño a objetivos en vuelo |
| **17** | 2445 | 15221 | 1.108 | 2426.9 | 1.007 (60 min) | 8.07 | Recarga acelerada en suelo fértil |
| **18** | 2697 | 17666 | 1.103 | 2536.1 | 1.063 (64 min) | 9.08 | Daño residual por espinas persistentes |
| **19** | 2962 | 20363 | 1.098 | 2650.2 | 1.118 (67 min) | 10.14 | Generación extra de Néctar por baja |
| **20** | 3239 | 23325 | 1.094 | 2769.4 | 1.170 (70 min) | 11.26 | **Hito Mayor 2:** Mutación Clorofílica Activa |
| **21** | 3530 | 26564 | 1.090 | 2894.1 | 1.220 (73 min) | 12.43 | Alcance máximo $+0.5$ casillas |
| **22** | 3833 | 30094 | 1.086 | 3024.3 | 1.267 (76 min) | 13.65 | $+12\%$ Daño a jefes y tanques |
| **23** | 4150 | 33927 | 1.083 | 3160.4 | 1.313 (79 min) | 14.92 | Reducción de tiempo de siembra en $20\%$ |
| **24** | 4480 | 38077 | 1.079 | 3302.6 | 1.356 (81 min) | 16.23 | **Punto de Medio Camino:** 50% XP Total |
| **25** | 4822 | 42557 | 1.076 | 3451.2 | 1.397 (84 min) | 17.59 | **Hito Menor:** Superfertilización inicial |
| **26** | 5178 | 47379 | 1.074 | 3606.6 | 1.436 (86 min) | 18.99 | Disparo quíntuple en oleadas de jefe |
| **27** | 5547 | 52557 | 1.071 | 3768.8 | 1.472 (88 min) | 20.42 | Inmunidad total a aturdimientos |
| **28** | 5928 | 58104 | 1.069 | 3938.4 | 1.505 (90 min) | 21.89 | Aura de soporte extendida (2 casillas) |
| **29** | 6313 | 64032 | 1.067 | 4115.6 | 1.534 (92 min) | 23.40 | Daño puro (ignora 100% armadura de plaga) |
| **30** | — | **70.253** | — | — | — | **24.93** | **Corona Botánica:** Título de Guardián Antiguo y aspecto dorado |

---

## 5. Comparación con Otras Familias de Curvas

Para validar la elección del modelo polinómico, se analizó el comportamiento de las cuatro familias matemáticas fijando la misma ancla inicial (120 XP) y el mismo total (70.253 XP):

| Familia de Curva | Parámetro Ajustado | Tiempo al Nivel Máximo | Nivel más Lento | Sensación en el Jugador |
|---|---|:---:|:---:|---|
| **Polinómica (Poly)** *(Elegida)* | $p = 2.1, c = 4$ | **24.9 h** | **92 min** | **Ideal:** Progresión fluida, subidas constantes, fase final desafiante sin muros insalvables. |
| **Lineal (Linear)** | $\text{Paso} = 164.5$ | 26.9 h | 71 min | **Monótona:** Niveles medios (12 a 20) se sienten lentos y los finales demasiado rápidos por la inflación de ingresos. |
| **Exponencial (Exp)** | Crecimiento $= 1.173$ | 22.5 h | **153 min** | **Punitiva:** Inicio hiperexplosivo pero crea un muro descomunal en los niveles 26–30 (más de 2.5 horas por nivel). |
| **Logística (Logistic)** | Ratio cap $= 62.5$ | 25.0 h | 87 min | **Irregular:** Comienzo lento, meseta intermedia con salto abrupto y fase final sin recompensa de esfuerzo. |

---

## 6. Integración en el Bucle Meta (Meta Loop)

1. **Fuentes de Esencia (Faucets):**
   - Completar oleadas: $70\%$ del XP total obtenido.
   - Victorias perfectas (0 fugas): Bono del $+20\%$.
   - Misiones diarias del huerto: Bonos fijos que reducen la fatiga en jugadores de móvil.
2. **Sumideros de Esencia (Sinks):**
   - La Esencia se invierte de forma individual en cada guardián, incentivando el juego variado con distintas plantas en lugar de invertir todo en una sola torre.
3. **Mecánica de Ponerse al Día (Catch-Up):**
   - Torres rezagadas (por debajo del nivel promedio de la cuenta) reciben una bonificación de "Abono Rápido" ($+50\%$ XP) hasta alcanzar el nivel medio del equipo, facilitando probar nuevas estrategias en mundos avanzados.
