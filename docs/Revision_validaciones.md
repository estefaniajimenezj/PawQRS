# Revisión de validaciones — PawQRS

- *Responsable:* Daniela Zapata Henao
- *Archivo revisado:* src/validaciones.py
- *Estado:* Revisión completada
- *Fecha:* 25 de noviembre de 2026

## 1. Objetivo

Verificar que el módulo src/validaciones.py acepte los formatos de entrada permitidos y rechace los datos incorrectos antes de registrar o actualizar una PQRS en el sistema, usando únicamente la biblioteca estándar de Python.

## 2. Reglas revisadas en src/validaciones.py

| Campo | Regla implementada |
| :--- | :--- |
| *Nombre completo* | Entre 3 y 100 caracteres; acepta letras (con tildes y ñ), espacios, apóstrofes y guiones. |
| *Tipo de documento* | Solo CC, TI, CE, PP o NIT. |
| *Número de documento* | Entre 3 y 15 dígitos numéricos. |
| *Tipo de teléfono* | Solo Celular, Fijo, Corporativo u Otro. |
| *Teléfono* | Exactamente 10 dígitos numéricos (aplica también para tipo Fijo). |
| *Correo electrónico* | Un solo @, dominio con punto, sin espacios y máximo 254 caracteres. |
| *Dirección* | Campo opcional (permite cadena vacía ""); si se escribe, debe tener entre 5 y 200 caracteres válidos. |
| *Tipo de PQRS* | Solo Petición, Queja, Reclamo o Sugerencia. |
| *Canal de recepción* | Presencial, Correo electrónico, Página web, Teléfono, Redes sociales u Otro. |
| *Asunto o título* | Entre 5 y 150 caracteres y signos básicos de puntuación. |
| *Descripción* | Entre 20 y 2.000 caracteres útiles (sin contar espacios al inicio o al final). |
| *Mascota* | Solo Perro o Gato. |
| *Campus* | Una de las nueve sedes configuradas para Medellín (no distingue mayúsculas ni espacios externos). |
| *Estado* | Solo Registrada, En proceso o Solucionada. |
| *Transición de estado* | Orden estricto: Registrada -> En proceso -> Solucionada (no permite saltar de Registrada a Solucionada). |

Las funciones validar_fecha y validar_hora están disponibles en el módulo para formato de fecha y hora, aunque en el flujo principal de src/main.py la fecha de registro se genera automáticamente con la zona horaria America/Bogota.

## 3. Resultados de las pruebas ejecutadas (V01 – V19)

Las pruebas se ejecutaron directamente desde la terminal de Codespaces en la rama integracion-pawqrs-24nov invocando las funciones de src/validaciones.py, sin modificar los archivos .txt de la carpeta data/:

| Caso | Función | Dato probado | Esperado | Resultado obtenido |
| :--- | :--- | :--- | :--- | :--- |
| *V01* | validar_nombre | "Ana María" | True (Acepta) | True — OK |
| *V02* | validar_nombre | "Ana123" | False (Rechaza) | False — OK |
| *V03* | validar_documento | "12345678" | True (Acepta) | True — OK |
| *V04* | validar_documento | "ABC123" | False (Rechaza) | False — OK |
| *V05* | validar_telefono | "3001234567" | True (Acepta) | True — OK |
| *V06* | validar_telefono | "3012345" | False (Rechaza) | False — OK |
| *V07* | validar_correo | "prueba@correo.com" | True (Acepta) | True — OK |
| *V08* | validar_correo | "prueba@correo" | False (Rechaza) | False — OK |
| *V09* | validar_direccion | "" (vacía) | True (Acepta) | True — OK |
| *V10* | validar_direccion | "Calle 10 # 20-30" | True (Acepta) | True — OK |
| *V11* | validar_direccion | "ABC" | False (Rechaza) | False — OK |
| *V12* | validar_titulo | "Consulta veterinaria" | True (Acepta) | True — OK |
| *V13* | validar_descripcion | "Necesito información sobre la atención de mi mascota." | True (Acepta) | True — OK |
| *V14* | validar_descripcion | "Hola" | False (Rechaza) | False — OK |
| *V15* | validar_mascota | "Gato" | True (Acepta) | True — OK |
| *V16* | validar_mascota | "Conejo" | False (Rechaza) | False — OK |
| *V17* | validar_estado | "Solucionada" | True (Acepta) | True — OK |
| *V18* | validar_transicion_estado | ("Registrada", "Solucionada") | False (Rechaza) | False — OK |
| *V19* | validar_transicion_estado | ("Registrada", "En proceso") | True (Acepta) | True — OK |

## 4. Diferencia entre validar la dirección y mostrar N/A

validar_direccion("") devuelve True porque la dirección es opcional al registrar una PQRS. Mostrar el texto N/A cuando el campo quedó vacío no hace parte de validaciones.py, sino de la visualización en consola y comprobante:
- En src/main.py se imprime N/A al consultar la PQRS si no hay dirección.
- En src/radicado.py también se muestra N/A al generar el comprobante.

## 5. Verificaciones adicionales en el código

- [x] Revisé las opciones de los menús en src/main.py y coinciden con los valores válidos de validaciones.py.
- [x] Confirmé que cuando se ingresa un dato inválido el programa vuelve a pedirlo sin cerrarse.
- [x] Probé dirección vacía (V09), válida (V10) e inválida por corta (V11).
- [x] Comprobé que N/A se maneja en src/main.py y src/radicado.py.
- [x] Revisé las funciones validar_fecha y validar_hora dentro de src/validaciones.py.
- [x] Confirmé que ningún archivo de data/ fue modificado durante las pruebas.

## 6. Conclusión

- *Pruebas ejecutadas:* 19 (V01 a V19).
- *Aprobadas:* 19 de 19 (OK).
- *Con fallos:* 0.
- *Ajustes realizados:* En una revisión previa se corrigió el formato de las listas canales_validos y campuses_validos en src/validaciones.py. En esta ejecución todas las funciones respondieron según lo esperado y el módulo quedó listo para la entrega.
-