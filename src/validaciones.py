 #Módulo de Validaciones y Calidad de Datos
from datetime import datetime

def validar_nombre(nombre: str) -> bool:
    if not isinstance(nombre, str):
        return False
    nombre_limpio = nombre.strip()
    if len(nombre_limpio) < 3 or len(nombre_limpio) > 100:
        return False
    for caracter in nombre_limpio:
        if not (caracter.isalpha() or caracter in [" ", "'", "-"]):
            return False
    return True

def validar_tipo_documento(tipo_documento: str) -> bool:
    if not isinstance(tipo_documento, str):
        return False
    tipos_validos = ["CC", "TI", "CE", "PP", "NIT"]
    return tipo_documento.strip().upper() in tipos_validos

def validar_documento(numero_documento: str) -> bool:
    if not isinstance(numero_documento, str):
        return False
    doc = numero_documento.strip()
    return doc.isdigit() and (3 <= len(doc) <= 15)
