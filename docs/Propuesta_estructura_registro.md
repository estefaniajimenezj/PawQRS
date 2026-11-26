# Propuesta de estructura de datos de PawQRS

- id
- nombre_completo
- tipo_documento
- numero_documento
- tipo_telefono
- telefono_contacto
- correo_electronico
- direccion
- tipo_solicitud
- fecha_radicacion
- canal_recepcion
- asunto_titulo
- descripcion_detallada
- tipo_mascota
- campus_relacionado
- fecha_maxima_respuesta
- estado_peticion
- hora_radicacion
- fecha_solucion

## Aprobación de la estructura de datos ##

La estructura común de 19 campos fue revisada y acordada por los cinco integrantes del equipo PawQRS durante la reunión de coordinación.

Esta estructura será utilizada como referencia para el desarrollo y la integración de los módulos main.py, validaciones.py, archivos.py, radicado.py y reportes.py.

Cualquier modificación posterior de los nombres o tipos de datos deberá ser comunicada y acordada con el equipo para evitar incompatibilidades entre los módulos.

## Actualización de la estructura de datos

La propuesta inicial de PawQRS contemplaba 19 campos.

Durante la integración del sistema se incorporó el campo `radicado`, por lo que la estructura actual contiene 20 campos.

El campo `id` corresponde al identificador numérico consecutivo, mientras que `radicado` permite identificar la solicitud mediante un código como PET-0001, QUE-0001, REC-0001 o SUG-0001.

Esta actualización conserva la propuesta original y documenta la evolución del proyecto.