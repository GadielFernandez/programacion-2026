# Investigación: cazadores de errores

**Valor y fecha de entrega:** [completar según la actividad en Moodle]

## ¿De qué se trata?
Un programa que "no funciona" casi nunca es un misterio: da un mensaje, o da un resultado raro.
Usted se convierte en **cazador de errores**: ejecuta ocho programas rotos (de varios temas de Python,
no solo de Pandas), descubre qué pasa, lo explica con sus palabras y lo corrige. Al final resuelve un reto corto.

## Parte A — Bitácora de errores (carpeta `A_errores/`)
Hay ocho archivos, `e01` a `e08`, cada uno con **un solo error**. Para cada uno:

1. **Ejecute** el programa y copie el mensaje que aparece (o anote el resultado raro).
2. **Clasifique** el error: sintaxis, nombre, tipo, índice, clave, lógico (sin mensaje)…
3. **Explique la causa** con sus propias palabras.
4. **Corrija** el archivo y compruebe que imprime la SALIDA ESPERADA de su encabezado.
5. **Anote** todo en la bitácora (documento de Word `Plantilla_Bitacora_Investigacion_Semana11.docx`) e **investigue** en la documentación oficial de Python lo que no entienda.

Dos errores **no muestran mensaje** (`e06` y `e07`): hay que darse cuenta de que algo está mal sin que Python lo avise.

## Parte B — Reto (`reto.py`)
Complete `resumen_grupo_b`: devuelve una **tupla** `(cantidad, promedio)` con los estudiantes del grupo B
que tienen examen mayor o igual a 70 y el promedio del examen de todo el grupo B (2 decimales).

## Cómo comprobar su trabajo
Desde la carpeta `material_investigacion`:

```bash
python verificar.py
```

Le dice qué archivos ya pasan y le da una pista de lo que falta; no entrega la solución.

## Qué se entrega
1. La bitácora en Word, completa (un cuadro por error) con **mínimo tres fuentes citadas en APA**.
2. Los ocho archivos `eNN` corregidos y `reto.py` completado.
3. Captura de pantalla de `python verificar.py`.
4. Reflexión de 3 a 5 líneas: ¿qué error fue el más difícil de encontrar y por qué?

## Rúbrica (100 puntos)
| Criterio | Puntos |
|---|---:|
| Clasificación y explicación de los errores | 25 |
| Correcciones que funcionan | 25 |
| Fuentes y citas | 15 |
| Reto | 25 |
| Reflexión y claridad | 10 |

## Reglas de trabajo
Escriba usted las explicaciones y las correcciones. Si usa ayuda (compañero, documentación, IA), debe poder
**explicar en voz alta** cada error de su bitácora y cada línea de su reto.
