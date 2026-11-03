# Ruta dinámica a la carpeta data
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "..", "data")


# ==========================================
# FUNCIONES PARA MANEJO DE PQRS
# ==========================================
def guardar_registro(tipo_pqrs: str, radicado: str, cliente: str, detalle: str) -> bool:
    """Guarda un registro de PQRS delimitado por pipe (|)."""
    nombre_archivo = f"{tipo_pqrs.capitalize()}.txt"
    ruta_archivo = os.path.normpath(os.path.join(DATA_DIR, nombre_archivo))
    linea = f"{radicado}|{cliente}|{detalle}\n"

    try:
        with open(ruta_archivo, mode="a", encoding="utf-8") as archivo:
            archivo.write(linea)
        print(f"[ÉXITO] Registro {radicado} guardado en {nombre_archivo}.")
        return True
    except Exception as e:
        print(f"[ERROR] No se pudo guardar: {e}")
        return False


def leer_registros(tipo_pqrs: str) -> list[str]:
    """Lee todas las líneas de un archivo de PQRS."""
    nombre_archivo = f"{tipo_pqrs.capitalize()}.txt"
    ruta_archivo = os.path.normpath(os.path.join(DATA_DIR, nombre_archivo))

    if not os.path.exists(ruta_archivo):
        return []

    try:
        with open(ruta_archivo, mode="r", encoding="utf-8") as archivo:
            return [linea.strip() for linea in archivo if linea.strip()]
    except Exception as e:
        print(f"[ERROR] No se pudo leer: {e}")
        return []


def buscar_por_radicado(tipo_pqrs: str, radicado_buscar: str) -> dict | None:
    """Busca una PQRS por su número de radicado."""
    lineas = leer_registros(tipo_pqrs)
    for linea in lineas:
        campos = linea.split("|")
        if len(campos) >= 3 and campos[0] == radicado_buscar:
            return {
                "radicado": campos[0],
                "cliente": campos[1],
                "detalle": campos[2]
            }
    return None


# ==========================================
# FUNCIONES PARA ACTAS DE REUNIONES
# ==========================================
def guardar_acta(fecha: str, asistentes: str, temas: str, decisiones: str, tareas: str, responsables: str, compromisos: str) -> bool:
    """Guarda un acta delimitada por punto y coma (;) en Actas.txt."""
    ruta_archivo = os.path.normpath(os.path.join(DATA_DIR, "Actas.txt"))
    linea = f"{fecha};{asistentes};{temas};{decisiones};{tareas};{responsables};{compromisos}\n"

    try:
        with open(ruta_archivo, mode="a", encoding="utf-8") as archivo:
            archivo.write(linea)
        print("[ÉXITO] Acta guardada correctamente.")
        return True
    except Exception as e:
        print(f"[ERROR] No se pudo guardar el acta: {e}")
        return False


# ==========================================
# PRUEBAS AUTOMÁTICAS
# ==========================================
if __name__ == "__main__":
    print("--- Probando PQRS ---")
    guardar_registro("Peticion", "PET-001", "Santiago Lopez", "Solicitud de prueba")
    print(buscar_por_radicado("Peticion", "PET-001"))

    print("\n--- Probando Actas ---")
    guardar_acta(
        "2026-11-03",
        "Santiago Lopez, Equipo",
        "Revisión de avance",
        "Archivos listos",
        "Subir a GitHub",
        "Santiago",
        "Entregar esta semana"
    )
