# Semana 8 — El archivo está vivo

## Nuestro encargo

Una red de hospitales nos contrata como **analistas de datos**. Necesita un
informe que siga siendo correcto cuando recibe nuevas atenciones. Los
registros son ficticios: sus pacientes tienen códigos, nombres y cédulas inventados. Los nombres
de medicamentos son datos para contar, no recomendaciones de tratamiento.

Nos piden responder: **¿cuántas veces aparece cada nombre de medicamento y
qué cambia cuando crece la fuente?** Construiremos un solo programa y lo
ejecutaremos de nuevo después de cada publicación. Nuestra meta común es
recorrer los registros, construir un diccionario contador y justificar sus
cifras. La lectura de JSON por API ya está preparada en `fuente.py`.

## Abrimos el caso

1. Descomprimimos todo `semana08_material_estudiante.zip` en una carpeta.
   Encontraremos esta guía, `analisis_en_vivo.py`, `fuente.py` y dos JSON de
   respaldo.
2. Abrimos la carpeta en VS Code o Thonny y ejecutamos
   `analisis_en_vivo.py`. Leemos el origen, la cantidad de registros y las
   equivalencias publicadas.
3. Escribimos nuestro análisis debajo de «Comencemos aquí». `fuente.py` ya
   nos entrega `registros` y `equivalencias`. Lo dejamos preparado tal como
   está y trabajamos con los datos recibidos.

Si aparece «copia local de respaldo», avisamos en la reunión: esa copia puede
representar otra versión. Cuando aparece «JSON públicos de GitHub», estamos
leyendo la fuente publicada. Observamos cómo `json.load()` convierte esa
respuesta en datos de Python; en esta sesión nos concentramos en analizarlos.

Cada atención contiene código, fecha, sede, hospital, código, nombre y cédula
ficticios del paciente, grupo de edad, diagnóstico, canal, estado y una lista
`medicamentos`. Una atención puede mencionar varios nombres. Un mismo
paciente ficticio puede aparecer en varias atenciones con el mismo nombre y la
misma cédula `FIC-...`; esta marca no tiene formato de cédula real.

## 1. Miramos una muestra

Mostramos hasta tres registros numerados. Usamos `range()` para recorrer las
posiciones que existan y presentamos el código, hospital, nombre y cédula del paciente,
diagnóstico y lista de medicamentos. Nuestro ciclo debe funcionar si la
fuente tiene dos o tres registros.

Antes de ejecutar, predecimos qué posiciones existen cuando solo hay dos.
Cuando recibamos `REG-003`, comparamos el `paciente_id`, nombre y cédula de
ambos registros.
Explicamos por qué tres atenciones pueden corresponder a dos pacientes.

## 2. Construimos el informe

Preparamos `conteo_literal = {}` y `total_menciones = 0`. Construimos juntos
el patrón del diccionario contador, incluso si no resolvimos el caso de
incidencias de la semana 7.

1. Con un `for`, visitamos cada registro.
2. Dentro de cada registro, con otro `for`, visitamos todos los nombres de su
   lista `medicamentos`.
3. Si un nombre exacto aún no tiene clave, la creamos con valor cero.
   Aumentamos esa clave y `total_menciones` una vez por nombre leído.
4. Mostramos el diccionario y el total. Comprobamos que la suma de sus valores
   coincide con `total_menciones`.

Mientras dos compañeros preparan un análisis y dos preguntas en una sala de
Webex, construimos el contador en la reunión principal. Al regresar, oímos
la propuesta, elegimos **una pregunta** y buscamos registros que permitan
responderla. Nuestra entrega común sigue siendo el informe de medicamentos.

Si la comprobación falla, seguimos dos vueltas de la traza proyectada:
identificamos qué nombre leímos, qué clave aumentamos y cuánto vale después.

## 3. El archivo cambia

Antes de cada nueva lectura, predecimos qué puede cambiar: registros,
menciones o claves. Ejecutamos **el mismo programa** y explicamos una
diferencia con un código de registro concreto.

Comparamos nuestras claves con las tres vistas del panel:

| Vista | Qué se considera igual |
|---|---|
| Texto literal | Solo nombres escritos exactamente igual. Es nuestro conteo. |
| Mayúsculas iguales | Los espacios exteriores y las mayúsculas/minúsculas se igualan con `strip().casefold()`. |
| Equivalencias | Una regla publicada reúne nombres alternativos bajo una clave común. |

Predecimos qué ocurre con `PARACETAMOL` y `paracetamol` en nuestro diccionario
literal. Observamos qué cambia al igualar mayúsculas y qué exige una regla
explícita, como una diferencia de acento o un nombre alternativo. Distinguimos
**claves** de **menciones**: agrupar nombres puede cambiar las claves sin
cambiar cuántas menciones recorrimos.

Las etapas de 20, 50 y 100 registros ponen a prueba **nuestro mismo
programa**. No escribimos un ejercicio nuevo por cada etapa. También
contrastamos atenciones y pacientes distintos: aclaramos qué cuenta cada
cifra antes de interpretarla.

## Si avanzamos antes

Podemos elegir **una** ampliación:

- Construimos `conteo_unificado`: limpiamos cada nombre con
  `strip().casefold()`, consultamos `equivalencias` y comprobamos que la suma
  todavía coincide con `total_menciones`.
- Usamos un `while` para consultar varios nombres hasta escribir `fin`.
  Pedimos la siguiente consulta dentro del ciclo, sin descargar la API en
  cada vuelta.
- Programamos una respuesta a la pregunta elegida sobre hospitales,
  diagnósticos o pacientes que reaparecen. Primero definimos si contamos
  atenciones o pacientes distintos.

Estas ampliaciones enriquecen el informe; nuestra entrega común no depende
de terminarlas.

## Si perdemos la conexión

Recibimos dos JSON de respaldo actualizados, reemplazamos los de nuestra
carpeta y cambiamos `USAR_RESPALDO` a `True` en `analisis_en_vivo.py`.
Indicamos que usamos una copia local y cuál versión recibimos.

## Entregamos nuestra evidencia

Entregamos `analisis_en_vivo.py` ejecutable y respondemos brevemente:

1. ¿Qué hace una vuelta de cada `for` y qué representa una clave?
2. ¿Por qué nuestra muestra con `range()` funciona con dos registros?
3. ¿Por qué la suma del diccionario coincide con `total_menciones`?
4. ¿Qué cambió tras una publicación? Citamos un registro que lo demuestre.
5. ¿Por qué contar atenciones puede dar otra cifra que contar pacientes?

Si realizamos una ampliación, la incluimos en el mismo archivo y explicamos
qué aporta al informe.
