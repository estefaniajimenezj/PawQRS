# PawQRS — Plan de versionado y control de cambios

**Proyecto integrador:** Algoritmia y Programación 2026-2  
**Institución:** Universidad de Antioquia — Ingeniería Industrial  
**Sistema:** PawQRS, gestor de Peticiones, Quejas, Reclamos y Sugerencias  
**Responsable de revisión y entrega:** Santiago Franco López  
**Rama revisada:** `integracion-pawqrs-24nov`  
**Fecha de consulta del repositorio:** 26 de noviembre de 2026  
**Estado:** En revisión final.

> **Importante:** las versiones 0.1.0 a 1.0.0 de este plan son hitos propuestos para documentar la evolución de PawQRS. No deben confundirse con etiquetas o versiones oficiales ya publicadas en GitHub. La versión final 1.0.0 queda sujeta a la aprobación del equipo y la entrega.

## 1. Objetivo

El objetivo de este documento es llevar un registro de las versiones de PawQRS y de los cambios realizados durante su desarrollo. También se busca establecer cómo se guardan las modificaciones, cómo se realizan las pruebas y qué aspectos se deben revisar antes de entregar la versión final del sistema.

## 2. Herramientas y organización del proyecto

Para el desarrollo y seguimiento de PawQRS se utilizaron las siguientes herramientas:

- **Git:** permite registrar los cambios realizados en el código y los documentos mediante *commits*.
- **GitHub:** se utiliza para almacenar el repositorio, compartir los avances y revisar las modificaciones realizadas por los integrantes.
- **Rama `integracion-pawqrs-24nov`:** contiene los cambios que se están revisando para la entrega final.
- **Rama `main`:** corresponde a la rama principal del proyecto, donde todavía no se ha integrado la última versión.
- **Pull Request #1:** se creó para integrar los cambios de la rama de integración a `main`. Actualmente permanece en borrador y sin fusionar.
- **GitHub Actions:** permite ejecutar automáticamente la revisión de sintaxis y las ocho pruebas del módulo de almacenamiento.

**Repositorio:** https://github.com/estefaniajimenezj/PawQRS  
**Pull Request de integración:** https://github.com/estefaniajimenezj/PawQRS/pull/1

## 3. Plan de versiones propuesto

Para organizar el desarrollo del sistema se establecieron las siguientes versiones propuestas, teniendo en cuenta las funcionalidades incorporadas en cada etapa.

| Versión propuesta | Etapa del proyecto | Características principales | Situación |
|---|---|---|---|
| `0.1.0` | Planeación y diseño | Identidad PawQRS, organización del equipo, README, visión, requisitos y cronograma. | Etapa realizada. |
| `0.2.0` | Desarrollo de módulos | Funciones de validación, archivos TXT, radicados, comprobantes y reportes. | Etapa realizada. |
| `0.3.0` | Integración funcional | Menú de consola que conecta el registro, las consultas, la actualización de estados y las estadísticas. | Etapa realizada. |
| `0.4.0` | Ajustes, pruebas y documentación | Menús numerados, zona horaria de Colombia, ocho pruebas automáticas, mejoras en los comprobantes y documentos de revisión. | En revisión final. |
| `1.0.0` | Entrega académica | Versión final revisada, probada y aprobada por el equipo. | **Pendiente de aprobación.** |

### 3.1. Forma de interpretar las versiones

Se propone utilizar tres números con el formato `mayor.menor.corrección`:

- **Primer número (mayor):** identifica cambios importantes en el sistema.
- **Segundo número (menor):** indica la incorporación de nuevas funcionalidades.
- **Tercer número (corrección):** identifica ajustes y correcciones de errores.

Por ejemplo, una versión `1.0.1` podría utilizarse para corregir un error sin agregar nuevas funcionalidades.

Este formato permite organizar los cambios y mantener un seguimiento de la evolución del programa. No es obligatorio crear etiquetas oficiales en GitHub para utilizarlo como referencia dentro del proyecto.

## 4. Historial de cambios en GitHub

Durante el desarrollo de PawQRS se realizaron diferentes modificaciones, las cuales quedaron registradas en el historial de *commits* de la rama de integración. Estos registros permiten observar los avances realizados y no equivalen a etiquetas oficiales de versión.

| Fecha | Commit | Cambio realizado |
|---|---|---|
| 24 nov. 2026 | `9afe592` | Integración del menú de registro, consulta, actualización y reportes. |
| 24 nov. 2026 | `6449484` | Incorporación de pruebas automáticas. |
| 24 nov. 2026 | `949900f` | Pruebas del módulo de almacenamiento. |
| 25 nov. 2026 | `8bcf25a` | Adaptación de fecha y hora a la zona horaria de Colombia. |
| 25 nov. 2026 | `1b3f562` | Presentación de `N/A` al consultar una dirección vacía. |
| 25 nov. 2026 | `3212682` | Opción para visualizar el comprobante durante la consulta. |
| 25 nov. 2026 | `8085d3f` | Centrado de títulos en el comprobante. |
| 25 nov. 2026 | `cf01d30` | Incorporación de la revisión de validaciones. |
| 25–26 nov. 2026 | `412d9f3` / `d96d2dd` | Incorporación del manual de usuario y capturas de pantalla. |

**Consulta del historial:** https://github.com/estefaniajimenezj/PawQRS/commits/integracion-pawqrs-24nov/

## 5. Procedimiento de control de cambios

Para mantener organizado el trabajo y evitar inconvenientes durante el desarrollo, se estableció el siguiente procedimiento:

1. **Organización:** revisar qué archivo o módulo tiene asignado cada integrante antes de comenzar a trabajar.
2. **Actualización:** confirmar que se está trabajando en la rama correspondiente y revisar los cambios recientes.
3. **Modificación:** realizar los cambios acordados para el módulo o documento asignado.
4. **Verificación:** ejecutar las pruebas relacionadas con las modificaciones realizadas.
5. **Registro:** guardar los cambios mediante un *commit* con un mensaje que describa lo realizado.
6. **Integración:** subir los cambios a la rama de integración, de acuerdo con la coordinación del equipo.
7. **Revisión final:** comprobar que los cambios y las pruebas estén correctos antes de aprobar la integración a `main`.

También se debe tener cuidado de no subir archivos de prueba, datos ficticios de la carpeta `data/`, carpetas `__pycache__/`, archivos `.pyc` ni comprobantes temporales. En caso de presentarse conflictos de sincronización, se deben revisar y solucionar sin utilizar `git push --force`.

## 6. Verificación del funcionamiento

### 6.1. Ocho pruebas automáticas existentes

Las pruebas del archivo `src/pruebas_archivos.py` utilizan una carpeta temporal; por ello no necesitan escribir datos de prueba en los cuatro archivos principales de `data/`.

| N.º | Prueba | Qué verifica / resultado esperado |
|---|---|---|
| 1 | Guardar una Petición | Genera un ID correcto, asigna el estado Registrada y deja vacía la fecha de solución. |
| 2 | Consecutivo de Peticiones | Después de `PET-0001`, se genera `PET-0002`. |
| 3 | Numeración por tipo | La primera Queja puede tener el radicado `QUE-0001`. |
| 4 | Rechazar un salto de estado | No permite pasar directamente de Registrada a Solucionada. |
| 5 | Cambio a En proceso | Actualiza el estado cuando la transición es válida. |
| 6 | Cambio a Solucionada | Guarda automáticamente la fecha de solución. |
| 7 | Rechazar estado no permitido | No acepta un estado como Cerrado. |
| 8 | Rechazar retroceso | No permite regresar de Solucionada a En proceso. |

### 6.2. Verificación del funcionamiento

Para comprobar el estado del proyecto se ejecutan dos comandos desde la terminal de Codespaces, ubicándose primero en la carpeta principal de PawQRS.

**Primera comprobación: revisión de sintaxis**

```bash
python -m py_compile src/*.py
```

Si el comando termina y aparece nuevamente el símbolo de la terminal sin mostrar errores, la revisión de sintaxis se realizó correctamente.

**Segunda comprobación: ejecución de las pruebas**

```bash
python src/pruebas_archivos.py
```

La ejecución se considera exitosa cuando aparece el siguiente mensaje:

```text
========== TODAS LAS PRUEBAS FUERON SUPERADAS ==========
```

Algunas pruebas pueden mostrar mensajes `[ERROR]`, ya que buscan comprobar que el sistema rechace estados incorrectos. Esto no significa que las pruebas hayan fallado, siempre que se muestre el mensaje final de éxito.

### 6.3. Verificación mediante GitHub Actions

En la consulta realizada el 26 de noviembre de 2026, la ejecución automática correspondiente al último *commit* observado, `d96d2dd`, aparecía completada correctamente con el resultado `success`.

**Enlace de la ejecución:** https://github.com/estefaniajimenezj/PawQRS/actions/runs/45742008913

### 6.4. Registro de verificación personal

Las siguientes comprobaciones se registraron el 27 de noviembre de 2026:

| Verificación | Fecha | Resultado observado por Santiago | Evidencia |
|---|---|---|---|
| Revisión de sintaxis | 27-11-2026 | Completada. La sintaxis es correcta. | Resultado de la ejecución en la terminal. |
| Ocho pruebas automáticas | 27-11-2026 | Completadas. | Ejecución finalizada con el mensaje de éxito. |
| Revisión del último GitHub Actions | 27-11-2026 | Completada. | Enlace a la ejecución consultada. |

## 7. Alcance de las pruebas

Las ocho pruebas automáticas se enfocan principalmente en el almacenamiento de las solicitudes, la generación de radicados y el control de los cambios de estado.

Sin embargo, estas pruebas no comprueban todos los componentes del programa. Por ejemplo, no verifican completamente los datos de los formularios, el funcionamiento de los menús, la presentación de los comprobantes ni los cálculos estadísticos.

Por esta razón, también se tienen en cuenta las revisiones realizadas por los integrantes del equipo, incluyendo las pruebas de funcionamiento general del sistema.

## 8. Criterios para aprobar la versión final

Para considerar terminada y aprobar la versión `1.0.0` de PawQRS, se deben cumplir las siguientes condiciones:

- El menú permite registrar y consultar solicitudes, actualizar estados, generar estadísticas y salir del programa.
- Los cuatro tipos de PQRS generan radicados independientes y almacenan la información en sus respectivos archivos TXT.
- Los comprobantes contienen la información requerida y mantienen el ancho establecido de 120 caracteres.
- La revisión de sintaxis y las ocho pruebas automáticas terminan correctamente.
- El manual de usuario, los documentos de revisión y el plan de versionado se encuentran disponibles en la carpeta `docs/`.
- Los integrantes del equipo han revisado el Pull Request y están de acuerdo con la integración final a `main`.

Mientras existan condiciones pendientes, la versión `1.0.0` continuará como una propuesta de entrega y no se considerará aprobada.

## 9. Mejoras futuras

Aunque el sistema cuenta con las funcionalidades principales para su entrega académica, se identifican algunas mejoras que podrían desarrollarse posteriormente:

- Ampliar las pruebas automáticas para incluir validaciones de datos, comprobantes y estadísticas.
- Mejorar el manejo de fechas incompletas o inconsistentes en los reportes.
- Incorporar mecanismos sencillos para realizar copias de seguridad de los archivos de datos.
- Evaluar la posibilidad de implementar una interfaz gráfica en futuras etapas del proyecto.

Estas mejoras se plantean como posibles trabajos posteriores y no corresponden a funcionalidades que se encuentren actualmente implementadas.

## 10. Revisión y aprobación

| Información | Registro |
|---|---|
| Responsable de revisión y entrega | Santiago Franco López |
| Rama revisada | `integracion-pawqrs-24nov` |
| Último *commit* observado | `d96d2dd` |
| Fecha de consulta del repositorio | 26 de noviembre de 2026 |
| Fecha de verificación personal | 27 de noviembre de 2026 |
| Resultado de las pruebas realizadas | Completadas, según el registro de verificación personal. |
| Aprobación del equipo | Pendiente. |
| Estado de la versión `1.0.0` | Pendiente de revisión y aprobación del equipo. |

Una vez que el equipo revise el contenido y confirme el cumplimiento de los criterios establecidos, se podrá aprobar la versión final y realizar la integración correspondiente a `main`.
