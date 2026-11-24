

# ==========================================
# MODULO DE ALMACENAMIENTO DE PAWQRS
# ==========================================

import os
import json
import csv
import unicodedata
from datetime import datetime


# ==========================================
# RUTAS DE ALMACENAMIENTO
# ==========================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.normpath(os.path.join(BASE_DIR, "..", "data"))

os.makedirs(DATA_DIR, exist_ok=True)


# ==========================================
# CONFIGURACION DE TIPOS DE PQRS
# ==========================================

TIPOS_PQRS = {
    "peticion": ("Peticion.txt", "PET"),
    "queja": ("Queja.txt", "QUE"),
    "reclamo": ("Reclamo.txt", "REC"),
    "sugerencia": ("Sugerencia.txt", "SUG")
}


# ==========================================
# ESTADOS VALIDOS
# ==========================================

ESTADOS_VALIDOS = {
    "registrada": "Registrada",
    "en proceso": "En proceso",
    "solucionada": "Solucionada"
}


# ==========================================
# ESTRUCTURA OFICIAL DE DATOS PQRS
# ==========================================

CAMPOS_PQRS = [
    "id",
    "radicado",
    "nombre_completo",
    "tipo_documento",
    "numero_documento",
    "tipo_telefono",
    "telefono_contacto",
    "correo_electronico",
    "direccion",
    "tipo_solicitud",
    "fecha_radicacion",
    "canal_recepcion",
    "asunto_titulo",
    "descripcion_detallada",
    "tipo_mascota",
    "campus_relacionado",
    "fecha_maxima_respuesta",
    "estado_peticion",
    "hora_radicacion",
    "fecha_solucion"
]


# ==========================================
# NORMALIZAR TEXTO
# ==========================================

def normalizar_texto(texto: str) -> str:
    """Normaliza textos para comparar sin diferencias de tildes."""

    texto = str(texto).strip().lower()
    texto = unicodedata.normalize("NFD", texto)

    return "".join(
        caracter for caracter in texto
        if unicodedata.category(caracter) != "Mn"
    )


# ==========================================
# OBTENER RUTA DEL ARCHIVO
# ==========================================

def obtener_ruta_archivo(tipo_pqrs: str) -> str:
    """Obtiene la ruta del archivo correspondiente al tipo de PQRS."""

    tipo = normalizar_texto(tipo_pqrs)

    if tipo not in TIPOS_PQRS:
        raise ValueError("El tipo de PQRS no es valido.")

    nombre_archivo = TIPOS_PQRS[tipo][0]

    return os.path.join(DATA_DIR, nombre_archivo)


# ==========================================
# GENERAR ID CONSECUTIVO POR TIPO DE PQRS
# ==========================================

def generar_siguiente_id(tipo_pqrs: str) -> int:
    """
    Genera un ID entero consecutivo e independiente
    para cada tipo de solicitud.
    """

    tipo = normalizar_texto(tipo_pqrs)

    if tipo not in TIPOS_PQRS:
        raise ValueError("El tipo de PQRS no es valido.")

    registros = leer_registros(tipo_pqrs)

    numeros = []

    for registro in registros:

        # Revisar ID existente
        try:
            numero_id = int(registro.get("id", 0))

            if numero_id > 0:
                numeros.append(numero_id)

        except (ValueError, TypeError):
            pass

        # Revisar radicados anteriores para evitar
        # repetir numeraciones de registros antiguos
        radicado = registro.get("radicado", "")
        prefijo = TIPOS_PQRS[tipo][1]

        if isinstance(radicado, str) and radicado.startswith(prefijo + "-"):
            try:
                numero_radicado = int(radicado.split("-")[1])

                if numero_radicado > 0:
                    numeros.append(numero_radicado)

            except (ValueError, IndexError):
                pass

    return max(numeros, default=0) + 1


# ==========================================
# GENERAR RADICADO A PARTIR DEL ID
# ==========================================

def generar_siguiente_radicado(tipo_pqrs: str) -> str:
    """Genera el radicado utilizando el ID consecutivo."""

    tipo = normalizar_texto(tipo_pqrs)

    if tipo not in TIPOS_PQRS:
        raise ValueError("El tipo de PQRS no es valido.")

    prefijo = TIPOS_PQRS[tipo][1]
    siguiente_id = generar_siguiente_id(tipo_pqrs)

    return f"{prefijo}-{siguiente_id:04d}"


# ==========================================
# GUARDAR REGISTROS DE PQRS
# ==========================================

def guardar_registro(datos: dict) -> bool:
    """Guarda una PQRS completa en el archivo TXT correspondiente."""

    try:

        tipo_pqrs = normalizar_texto(
            datos.get("tipo_solicitud", "")
        )

        ruta_archivo = obtener_ruta_archivo(tipo_pqrs)

        # Crear estructura oficial
        registro = {
            campo: datos.get(campo, "")
            for campo in CAMPOS_PQRS
        }

        # Generar ID entero consecutivo
        nuevo_id = generar_siguiente_id(tipo_pqrs)

        registro["id"] = nuevo_id

        # Generar radicado a partir del ID
        prefijo = TIPOS_PQRS[tipo_pqrs][1]

        registro["radicado"] = f"{prefijo}-{nuevo_id:04d}"

        # Validar estado inicial
        estado = normalizar_texto(
            registro.get("estado_peticion", "")
        )

        if not estado:
            estado = "registrada"

        if estado not in ESTADOS_VALIDOS:
            print("[ERROR] El estado indicado no es valido.")
            return False
            
        if estado != "registrada":
            print("[ERROR] Toda PQRS nueva debe empezar en estado Registrada.")
            return False 

        registro["estado_peticion"] = ESTADOS_VALIDOS[estado]
        
        # Toda PQRS nueva inicia sin fecha de solucion
        registro["fecha_solucion"] = ""

        # Guardar registro
        with open(
            ruta_archivo,
            mode="a",
            encoding="utf-8"
        ) as archivo:

            archivo.write(
                json.dumps(registro, ensure_ascii=False) + "\n"
            )

        print(
            f"[EXITO] Registro {registro['radicado']} "
            f"guardado correctamente. ID: {registro['id']}"
        )

        return True

    except (OSError, ValueError, TypeError) as error:

        print(f"[ERROR] No se pudo guardar el registro: {error}")

        return False


# ==========================================
# LEER REGISTROS DE PQRS
# ==========================================

def leer_registros(tipo_pqrs: str) -> list[dict]:
    """Lee los registros y los devuelve como una lista de diccionarios."""

    try:

        ruta_archivo = obtener_ruta_archivo(tipo_pqrs)

        if not os.path.exists(ruta_archivo):
            return []

        registros = []

        with open(
            ruta_archivo,
            mode="r",
            encoding="utf-8"
        ) as archivo:

            for numero_linea, linea in enumerate(archivo, start=1):

                if not linea.strip():
                    continue

                try:

                    registro = json.loads(linea)
                    registros.append(registro)

                except json.JSONDecodeError:

                    print(
                        f"[ADVERTENCIA] Registro incorrecto "
                        f"en la linea {numero_linea}."
                    )

        return registros

    except (OSError, ValueError) as error:

        print(f"[ERROR] No se pudieron leer los registros: {error}")

        return []


# ==========================================
# BUSCAR PQRS POR NUMERO DE RADICADO
# ==========================================

def buscar_por_radicado(
    tipo_pqrs: str,
    radicado_buscar: str
) -> dict | None:
    """Busca una PQRS mediante su numero de radicado."""

    registros = leer_registros(tipo_pqrs)

    for registro in registros:

        if registro.get("radicado") == radicado_buscar:
            return registro

    return None


# ==========================================
# ACTUALIZAR ESTADO DE UNA PQRS
# ==========================================


def actualizar_estado(
    tipo_pqrs: str,
    radicado: str,
    nuevo_estado: str
) -> bool:
    """Actualiza el estado de una PQRS """

    estado_normalizado = normalizar_texto(nuevo_estado)

    if estado_normalizado not in ESTADOS_VALIDOS:
        print("[ERROR] El estado indicado no es valido.")
        return False

    try:
        ruta_archivo = obtener_ruta_archivo(tipo_pqrs)

        registros = leer_registros(tipo_pqrs)

        encontrado = False

        for registro in registros:

            if registro.get("radicado") == radicado:

                # Obtener el estado actual
                estado_actual = normalizar_texto(
                    registro.get("estado_peticion", "")
                )

                # Definir transiciones permitidas
                transiciones = {
                    "registrada": "en proceso",
                    "en proceso": "solucionada"
                }

                # Validar transicion
                if transiciones.get(estado_actual) != estado_normalizado:
                    print("[ERROR] Transicion de estado no permitida.")
                    return False

                # Actualizar estado
                registro["estado_peticion"] = ESTADOS_VALIDOS[
                    estado_normalizado
                ]

                # Registrar fecha de solucion
                if estado_normalizado == "solucionada":
                    registro["fecha_solucion"] = datetime.now().strftime(
                        "%Y-%m-%d %H:%M:%S"
                    )
                else:
                    registro["fecha_solucion"] = ""

                encontrado = True
                break

        if not encontrado:
            print("[ERROR] No se encontro el radicado.")
            return False

        # Guardar cambios en el archivo
        with open(
            ruta_archivo,
            mode="w",
            encoding="utf-8"
        ) as archivo:

            for registro in registros:
                archivo.write(
                    json.dumps(registro, ensure_ascii=False) + "\n"
                )

        print("[EXITO] Estado actualizado correctamente.")
        return True

    except (OSError, ValueError) as error:
        print(f"[ERROR] No se pudo actualizar: {error}")
        return False

# ==========================================
# GUARDAR ACTAS DE REUNIONES
# ==========================================

def guardar_acta(
    fecha: str,
    asistentes: str,
    temas: str,
    decisiones: str,
    tareas: str,
    responsables: str,
    compromisos: str
) -> bool:
    """Guarda los datos de una reunion en Actas.txt."""

    ruta_archivo = os.path.join(DATA_DIR, "Actas.txt")

    datos_acta = [
        fecha,
        asistentes,
        temas,
        decisiones,
        tareas,
        responsables,
        compromisos
    ]

    try:

        with open(
            ruta_archivo,
            mode="a",
            encoding="utf-8",
            newline=""
        ) as archivo:

            escritor = csv.writer(archivo, delimiter=";")

            escritor.writerow(datos_acta)

        print("[EXITO] Acta guardada correctamente.")

        return True

    except OSError as error:

        print(f"[ERROR] No se pudo guardar el acta: {error}")

        return False
