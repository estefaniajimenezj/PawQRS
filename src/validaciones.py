# Módulo de Validaciones y Calidad de Datos 

def validar_nombre(nombre: str) -> bool:
    if not isinstance(nombre, str) or len(nombre.strip()) < 2:
        return False
    return nombre.replace(" ", "").isalpha()

def validar_documento(documento: str) -> bool:
    doc = str(documento).strip()
    return doc.isdigit() and (6 <= len(doc) <= 11)

def validar_telefono(telefono: str) -> bool:
    tel = str(telefono).strip()
    return tel.isdigit() and (7 <= len(tel) <= 10)
