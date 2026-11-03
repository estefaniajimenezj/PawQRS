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
    
    def validar_correo(correo: str) -> bool:
    if not isinstance(correo, str) or len(correo.strip()) < 5:
        return False
    correo_limpio = correo.strip()
    if "@" not in correo_limpio:
        return False
    partes = correo_limpio.split("@")
    return len(partes) == 2 and len(partes[0]) > 0 and "." in partes[1]
    
def validar_direccion(direccion: str) -> bool:
    return isinstance(direccion, str) and len(direccion.strip()) >= 5

def validar_tipo_pqrs(tipo: str) -> bool:
    if not isinstance(tipo, str):
        return False
    tipos_validos = ["peticion", "queja", "reclamo", "sugerencia", "felicitacion"]
    return tipo.strip().lower() in tipos_validos
