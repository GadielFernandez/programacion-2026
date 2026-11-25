# Semana 11 — Repaso de fundamentos y Pandas con notas de estudiantes

Hoy analizamos las notas de 15 estudiantes ficticios (`notas.csv`): tarea, práctica, proyecto,
examen y asistencia. El objetivo no es memorizar sintaxis, sino **leer código, predecir qué hace
y escribirlo con sus propias palabras**.

## Antes de empezar

1. Instale Pandas si falta: `python -m pip install pandas`.
2. Trabaje siempre desde esta carpeta (`material_estudiante`).

## En clase (≈ 160 min, con 20 min de receso aparte)

| Bloque | Min | Dónde | Qué hace |
|---|---:|---|---|
| Apertura y pregunta generadora | 10 | — | ¿Cómo estar seguros de lo que hará un programa antes de ejecutarlo? |
| Quiz de predicción | 20 | Socrative | Prediga la salida de fragmentos de código antes de ejecutarlos. |
| Preparación | 5 | — | Pandas instalado y carpeta abierta en Visual Studio Code. |
| Etapa 1: Pandas por niveles (1 a 4) | 35 | `1_filtros_pandas/` | Código suelto: cargar, una columna, varias columnas, calcular. |
| *Receso* | *20* | | |
| Etapa 1: Pandas por niveles (5 a 10) | 45 | `1_filtros_pandas/` | Funciones en cascada: primera función, columna nueva, filtrar, dos condiciones, agrupar y reporte final. |
| Etapa 2: traducir entre lentes | 15 | `2_traducir.py` | Nativo → Pandas y Pandas → nativo. |
| Presentación de la investigación | 10 | `material_investigacion/CONSIGNA_INVESTIGACION.md` | Se modelan dos errores en vivo. |
| Cierre | 10 | Socrative | Autoevaluación y reflexión. |

### Cómo se trabaja la etapa 1
Cada nivel es un archivo de menos de 30 líneas. Empezamos desde cero: primero qué es una tabla y cómo
se toma una columna. Los **niveles 1 a 4 son código suelto** (usted escribe líneas, sin funciones). **Desde el
nivel 5 el código se guarda en funciones que trabajan en cascada**: cada una llama a la anterior. El docente
resuelve un ejemplo **en vivo con otros datos**; usted resuelve el suyo con las notas. Cada nivel pide menos
ayuda que el anterior:

| Niveles | Ayuda |
|---|---|
| 1 a 5 | Completar huecos (`____`) |
| 6 y 7 | Solo una pista |
| 8 a 10 | Solo el enunciado |

Ejecute su nivel desde la carpeta `material_estudiante` y compruébelo:

```bash
python 1_filtros_pandas/nivel_6_columna_nueva.py
python verificar.py n6
```

`verificar.py` acepta `n1` a `n10` (niveles de la etapa 1) y `e2` (traducir); sin argumento revisa todo. Le da una pista si falla,
pero no la solución.

## Después de la clase: la Investigación
La parte de **errores** y el **reto** se trabajan en la investigación, en su propia carpeta
(`material_investigacion/`), con consigna, bitácora en Word y verificador propios.

## Reglas de trabajo

- **Primero predice, después ejecuta.** Equivocarse al predecir también enseña.
- Si usa ayuda (compañero, documentación, IA), debe poder **explicar en voz alta cada línea** que entrega.

## Qué se entrega de la clase (portafolio)

1. Los diez niveles de `1_filtros_pandas/` y `2_traducir.py` completados.
2. Captura de `python verificar.py`.
3. Reflexión de 3 líneas: ¿qué predicción del quiz falló y por qué?

La entrega de errores y reto va con la investigación.
