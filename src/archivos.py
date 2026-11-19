
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
    "sugerencia": ("Sugerencia.txt", "SUG"),
    "felicitacion": ("Felicitacion.txt", "FEL")
}


def normalizar_texto(texto: str) -> str:
    """Normaliza textos para comparar tipos sin diferencias de tildes."""
    texto = str(texto).strip().lower()
    texto = unicodedata.normalize("NFD", texto)
    return "".join(
        caracter for caracter in texto
        if unicodedata.category(caracter) != "Mn"
    )


def obtener_ruta_archivo(tipo_pqrs: str) -> str:
    """Obtiene la ruta del archivo correspondiente al tipo de PQRS."""

    tipo = normalizar_texto(tipo_pqrs)

    if tipo not in TIPOS_PQRS:
        raise ValueError("El tipo de PQRS no es valido.")

    nombre_archivo = TIPOS_PQRS[tipo][0]

    return os.path.join(DATA_DIR, nombre_archivo)


# ==========================================
# GENERACION DE RADICADOS CONSECUTIVOS
# ==========================================

def generar_siguiente_radicado(tipo_pqrs: str) -> str:
    """Genera un radicado consecutivo independiente por tipo de PQRS."""

    tipo = normalizar_texto(tipo_pqrs)

    if tipo not in TIPOS_PQRS:
        raise ValueError("El tipo de PQRS no es valido.")

    prefijo = TIPOS_PQRS[tipo][1]
    registros = leer_registros(tipo_pqrs)

    numeros = []

    for registro in registros:
        radicado = registro.get("radicado", "")

        if radicado.startswith(prefijo + "-"):
            try:
                numero = int(radicado.split("-")[1])
                numeros.append(numero)
            except (ValueError, IndexError):
                continue

    siguiente = max(numeros, default=0) + 1

    return f"{prefijo}-{siguiente:03d}"


# ==========================================
# GUARDAR REGISTROS DE PQRS
# ==========================================

def guardar_registro(datos: dict) -> bool:
    """Guarda una PQRS completa en el archivo TXT correspondiente."""

    try:
        tipo_pqrs = datos.get("tipo", "")
        ruta_archivo = obtener_ruta_archivo(tipo_pqrs)

        registro = datos.copy()

        if not registro.get("radicado"):
            registro["radicado"] = generar_siguiente_radicado(
                tipo_pqrs
            )

        if buscar_por_radicado(
            tipo_pqrs, registro["radicado"]
        ) is not None:
            print("[ERROR] El radicado ya existe.")
            return False

        registro.setdefault("estado", "Registrada")
        registro.setdefault("fecha_solucion", "")

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
            "guardado correctamente."
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
    """Busca y devuelve una PQRS completa mediante su radicado."""

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
    """Actualiza el estado y la fecha de solucion de una PQRS."""

    estados_validos = {
        "registrada": "Registrada",
        "en proceso": "En proceso",
        "solucionada": "Solucionada",
        "cerrada": "Cerrada"
    }

    estado_normalizado = normalizar_texto(nuevo_estado)

    if estado_normalizado not in estados_validos:
        print("[ERROR] El estado indicado no es valido.")
        return False

    try:
        ruta_archivo = obtener_ruta_archivo(tipo_pqrs)
        registros = leer_registros(tipo_pqrs)

        encontrado = False

        for registro in registros:
            if registro.get("radicado") == radicado:

                registro["estado"] = estados_validos[
                    estado_normalizado
                ]

                if estado_normalizado == "solucionada":
                    registro["fecha_solucion"] = (
                        datetime.now().strftime("%Y-%m-%d")
                    )

                encontrado = True
                break

        if not encontrado:
            print("[ERROR] No se encontro el radicado.")
            return False

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
    """Guarda los datos de una reunion en el archivo Actas.txt."""

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

