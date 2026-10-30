# Jardín de Guardianes: Diseño de Género, Progresión y Equilibrio Económico

Bienvenido a la documentación técnica y de diseño de sistemas para **Jardín de Guardianes**, un juego de **defensa de torres (Tower Defense)** con temática botánica diseñado para dispositivos móviles y PC.

Este repositorio contiene los análisis de género, el modelado matemático de la curva de progresión de 30 niveles para las torres y la auditoría formal de costes de unidades mediante modelos de regresión lineal robusta.

---

## 📁 Índice y Lista de Archivos Creados

A continuación se detalla el inventario de archivos generados para este proyecto:

| Archivo | Tipo | Descripción y Propósito |
|---|---|---|
| [`genre_brief.md`](genre_brief.md) | Documento Markdown | **Brief de Género Completo:** Pilares de diseño, bucle principal, convenciones a respetar, oportunidades de diferenciación botánica (simbiosis y recursos vivos), forma del ritmo (pacing) y checklist de mitigación de los 6 fallos típicos del género. |
| [`progression_design.md`](progression_design.md) | Documento Markdown | **Análisis de Progresión de Torres (30 Niveles):** Diseño de la experiencia de subida de nivel, formulación polinómica, desglose de tiempo por nivel, hitos de maestría botánica y comparativa entre familias de curvas. |
| [`tower_progression.csv`](tower_progression.csv) | Tabla de Datos CSV | **Datos Brutos de Progresión (30 Niveles):** Columnas con nivel, XP requerida, XP acumulada, ratio de crecimiento, ingreso horario de esencia y horas de juego por nivel. |
| [`tower_progression_report.md`](tower_progression_report.md) | Reporte Markdown | **Reporte Oficial del Script de Progresión:** Diagnósticos automáticos de tiempo total (24.9 h), nivel del 50% de XP (nivel 24) y verificación de ausencia de muros artificiales. |
| [`cost_curve_analysis.md`](cost_curve_analysis.md) | Documento Markdown | **Análisis de la Curva de Costes y Equilibrio:** Examen de las 12 torres, desglose de pesos de atributos, diagnóstico detallado de las 2 torres mal costeadas y propuesta de rebalanceo antes/después. |
| [`towers_cost_data.csv`](towers_cost_data.csv) | Tabla de Datos CSV | **Base de Datos Inicial de 12 Torres:** Parámetros de combate de las plantas guardianas (`name,cost,dps,range,aoe_radius,slow_pct`). |
| [`towers_cost_data_fit.csv`](towers_cost_data_fit.csv) | Tabla de Datos CSV | **Resultados del Ajuste Lineal Robusto Inicial:** Comparación entre coste real y coste justo, cálculo de residuos y veredictos automáticos. |
| [`towers_cost_data_report.md`](towers_cost_data_report.md) | Reporte Markdown | **Reporte Oficial del Script de Costes:** Detección de valores atípicos iniciales (Mazorca Cañonera y Orquídea Real). |
| [`towers_rebalanced_data.csv`](towers_rebalanced_data.csv) | Tabla de Datos CSV | **Base de Datos de 12 Torres Rebalanceadas:** Valores ajustados con Mazorca Cañonera a coste 270 y Orquídea Real a coste 170. |
| [`towers_rebalanced_data_report.md`](towers_rebalanced_data_report.md) | Reporte Markdown | **Reporte Oficial Post-Rebalanceo:** Demostración matemática del nuevo ajuste ($R^2 = 0.999$, $\text{RMSE} = 1.50$). |
| [`README.md`](README.md) | Documento Markdown | **Punto de Entrada del Proyecto:** Resumen ejecutivo, índice de archivos y síntesis de conclusiones. |

---

## 🎯 Conclusiones Principales del Proyecto

### 1. Conclusiones del Brief de Género
- **Respeto a la Alfabetización del Jugador:** Se preservan intactas las convenciones clave que evitan la frustración: arquetipos visuales inmediatos (un brote dispara rápido, un cactus penetra blindajes, un lirio congela), telegrafiado riguroso de rutas y composiciones de oleadas, rangos geométricos claros y una tolerancia a fugas de 10 a 20 flores.
- **Diferenciación Orgánica sin Fricción:** Para distanciarse de los clones tradicionales, se rompen tres convenciones mediante pilares botánicos:
  1. *Simbiosis y Polinización de Vecindad:* Las torres interactúan con sus vecinas inmediatas (polen venenoso, aceleración de clorofila), transformando la cuadrícula en un puzle espacial vivo.
  2. *Moneda de Doble Flujo:* Néctar Solar (gasto rápido dinámico) y Canales de Riego (logística de terreno para torres de alto nivel).
  3. *Herramientas Activas de Jardinero:* El jugador poda para reubicar al 80% del valor, abona para sobrecargar en momentos de clímax y fertiliza casillas, eliminando por completo la observación pasiva.
- **Blindaje contra Fallos Críticos:** El diseño cuenta con un plan de acción concreto contra la saturación visual móvil (proyectiles agrupados), la sobrecarga de información (límite de 5 a 7 plantas por baraja) y la falta de claridad en las derrotas (código de color en el daño flotante).

### 2. Conclusiones del Diseño de Progresión (30 Niveles)
- **Modelado Basado en Tiempo, no en Números Ciegos:** La curva polinómica calibrada ($\text{base}=120$, $\text{offset}=4$, $\text{exponente}=2.1$) combinada con un crecimiento de ingresos del $4.5\%$ por nivel genera una experiencia de **24.9 horas de juego activo por guardián**.
- **Distribución Psicológica Ideal:**
  - Nivel $1 \rightarrow 2$ en **6 minutos** (recompensa inmediata en la primera sesión móvil).
  - Nivel $24$ marca el **50% de la XP total acumulada** ($80\%$ del rango de niveles), garantizando que el juego medio avance de forma dinámica y la fase final funcione como meta de prestigio.
  - El nivel más lento requiere **92 minutos** (Nivel 29), permaneciendo dentro de límites saludables y evitando los muros artificiales de las curvas puramente exponenciales (que exigirían 153 min por nivel).
- **Hitos de Juego Tangibles:** Cada 5 niveles el jugador desbloquea habilidades activas, ramas de mutación A/B o pasivas de resistencia, evitando niveles "vacíos".

### 3. Conclusiones del Análisis de Costes y Equilibrio Numérico
- **Detección Inequívoca de Dos Patologías Críticas:**
  1. **Mazorca Cañonera (Subcosteada / Rota):** Costaba **140 de Néctar**, cuando su coste justo era de **218.40 a 268.50**. Proporcionaba daño masivo de artillería a precio de ganga, lo que en producción habría destruido la diversidad táctica al convertirse en una estrategia dominante incuestionable.
  2. **Orquídea Real (Sobrecosteada / Trampa de Novatos):** Costaba **310 de Néctar**, cuando su rendimiento apenas justificaba un valor de **167.00 a 168.80**. Actuaba como una trampa punitiva que frustraba al jugador al no poder frenar las oleadas pese a su alto desembolso.
- **Resolución Matemática Eficaz:**
  - Al reajustar los costes a **270 para la Mazorca Cañonera** y **170 para la Orquídea Real**, el coeficiente de determinación saltó de un pobre **$R^2 = 0.212$** a un extraordinario **$R^2 = 0.999$**, reduciendo el error cuadrático medio ($\text{RMSE}$) de **50.46 a solo 1.50**.
  - Las 12 torres quedan perfectamente alineadas a lo largo de la curva de coste transitivo, garantizando que cada gasto adicional de Néctar compre una ventaja justa y proporcional.

---

## 🚀 Próximos Pasos Recomendados

1. **Prueba de Pacing con Curva de Interés (`fun-curve`):** Trazar la intensidad beat-by-beat del Mundo 1 (Huerto Soleado) para validar la colocación de picos de tensión y fases de alivio en las oleadas 4, 7 y 10.
2. **Implementación de Prototipo en Motor (Unity / Godot / Web):** Integrar las tablas CSV (`towers_rebalanced_data.csv` y `tower_progression.csv`) directamente en los ScriptableObjects o tablas de configuración de datos del juego.
3. **Monitoreo de Telemetría Temprana:** Comprobar en pruebas de juego cerradas que la tasa de elección (*Pick Rate*) de la Mazorca Cañonera rebalanceada se mantenga entre el $15\%$ y el $25\%$, confirmando que es una opción viable pero ya no dominante.
