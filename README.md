# Examen práctico de Python

## Simulación de datos — Plataforma de cuidado animal

Contexto

Una empresa dedicada al cuidado y bienestar animal está desarrollando una plataforma digital para administrar información relacionada con mascotas, propietarios y servicios ofrecidos.

Antes de implementar una base de datos real, el equipo necesita generar información simulada que permita probar posteriormente procesos de análisis, limpieza, validación y transformación de datos.

La tarea consiste en desarrollar un programa en Python capaz de simular un conjunto de datos relacionado con una plataforma de cuidado animal.

---

Objetivo

Construir un simulador de datos utilizando Python que genere información ficticia de mascotas y servicios asociados, aplicando funciones, estructuras de datos, ciclos, condicionales y las librerías "random" y "faker".

---

Cantidad de datos

El programa deberá generar exactamente:

1000 registros simulados.

Cada registro deberá representar una mascota dentro de la plataforma.

---

Estructura de los datos

Los datos deberán almacenarse en una:

Lista de diccionarios.

Cada diccionario deberá contener exactamente 10 atributos:

1. "id_mascota"
2. "nombre_mascota"
3. "especie"
4. "raza"
5. "edad"
6. "peso"
7. "nombre_propietario"
8. "ciudad"
9. "tipo_servicio"
10. "costo_servicio"

---

Descripción de los atributos

id_mascota

Identificador único del registro.

nombre_mascota

Nombre ficticio de la mascota.

especie

Tipo de animal registrado en la plataforma.

La plataforma puede manejar diferentes especies como perros, gatos, aves, conejos u otros animales domésticos.

raza

Raza correspondiente a la mascota.

Se espera coherencia entre la especie y la raza registrada.

edad

Edad de la mascota expresada en años.

peso

Peso aproximado de la mascota.

nombre_propietario

Nombre completo de la persona responsable de la mascota.

ciudad

Ciudad donde se encuentra registrado el propietario.

tipo_servicio

Servicio solicitado para la mascota.

La plataforma puede ofrecer servicios como consulta veterinaria, vacunación, peluquería, guardería, paseo o desparasitación.

costo_servicio

Valor asociado al servicio recibido.

---

Librerías obligatorias

Para realizar la simulación deberán utilizarse las librerías:

- "random"
- "faker"

"Faker" deberá utilizarse para generar información ficticia relacionada con personas u otros datos que el estudiante considere apropiados.

"random" deberá utilizarse para seleccionar, variar o generar información aleatoria dentro de la simulación.

---

Organización del proyecto

El proyecto deberá estar dividido obligatoriamente en dos archivos:

"main.py"

Será el archivo principal encargado de ejecutar el programa.

"simulador.py"

Contendrá las funciones necesarias para generar y modificar los datos simulados.

---

Uso de funciones

La solución deberá desarrollarse mediante funciones.

Como mínimo, el programa deberá permitir:

- Generar un registro individual.
- Generar los 1000 registros.
- Ensuciar los datos generados.

Los estudiantes pueden crear funciones adicionales si consideran que mejoran la organización de la solución.

---

Ensuciamiento de los datos 💩

Después de generar los registros correctamente, el programa deberá introducir errores intencionales en una parte de los datos.

El objetivo es simular situaciones reales en las cuales la información almacenada puede presentar problemas de calidad.

No todos los registros deberán contener errores.

Los errores deberán introducirse de forma aleatoria.

---

Tipos de errores

El conjunto de datos deberá contener como mínimo 5 tipos diferentes de problemas de calidad.

Entre los posibles problemas pueden encontrarse:

- Valores nulos.
- Cadenas vacías.
- Espacios innecesarios en textos.
- Diferencias entre mayúsculas y minúsculas.
- Errores ortográficos.
- Valores numéricos negativos.
- Valores numéricos fuera de rangos razonables.
- Datos escritos con tipos incorrectos.
- Servicios sin información.
- Ciudades incorrectamente escritas.
- Registros duplicados.
- Datos inconsistentes entre diferentes atributos.

El estudiante deberá decidir cómo implementar estos errores dentro de la simulación.

---

Porcentaje de datos con errores

Se recomienda que aproximadamente entre un 10 % y un 20 % de los registros presenten algún problema de calidad.

La selección de los registros que serán modificados deberá realizarse de manera aleatoria.

---

Requisitos técnicos

La solución deberá cumplir obligatoriamente con los siguientes requisitos:

1. Utilizar Python.
2. Utilizar "random".
3. Utilizar "faker".
4. Generar exactamente 1000 registros.
5. Utilizar una lista como estructura principal.
6. Cada elemento de la lista deberá ser un diccionario.
7. Cada diccionario deberá contener exactamente 10 atributos.
8. Utilizar funciones.
9. Separar la solución en "main.py" y "simulador.py".
10. Implementar una función encargada de ensuciar los datos.
11. Implementar mínimo 5 tipos diferentes de errores.
12. Introducir los errores de manera aleatoria.
13. Mantener coherencia razonable entre los datos generados antes del proceso de ensuciamiento.
14. El programa deberá ejecutarse correctamente desde "main.py".

---

Restricciones

Durante el desarrollo del ejercicio no se permite:

- Crear manualmente los 1000 registros.
- Descargar conjuntos de datos previamente construidos.
- Utilizar bases de datos.
- Utilizar Pandas para generar los registros.
- Copiar datasets existentes desde Internet.

La construcción de los datos deberá realizarse mediante programación.

---

Entrega

Cada estudiante deberá entregar únicamente los siguientes archivos:

- "main.py"
- "simulador.py"

Ambos archivos deberán funcionar conjuntamente.

Al ejecutar "main.py", el programa deberá generar los 1000 registros simulados correspondientes a la plataforma de cuidado animal.

---

Criterios de evaluación

Se tendrá en cuenta:

- Correcta utilización de funciones.
- Uso adecuado de listas y diccionarios.
- Uso correcto de "random".
- Uso correcto de "faker".
- Generación de los 1000 registros.
- Calidad y coherencia de los datos simulados.
- Correcta separación entre "main.py" y "simulador.py".
- Implementación del ensuciamiento de datos.
- Variedad de errores introducidos.
- Organización y legibilidad del código.
- Capacidad del programa para ejecutarse sin errores.
