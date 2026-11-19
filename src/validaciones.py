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

def validar_tipo_telefono(tipo_telefono: str) -> bool:
    if not isinstance(tipo_telefono, str):
        return False
    tipos_validos = ["celular", "fijo", "corporativo", "otro"]
    return tipo_telefono.strip().lower() in tipos_validos

def validar_telefono(telefono: str) -> bool:
    if not isinstance(telefono, str):
        return False
    tel = telefono.strip()
    return tel.isdigit() and len(tel) == 10

def validar_correo(correo: str) -> bool:
    if not isinstance(correo, str):
        return False
    correo_limpio = correo.strip()
    if len(correo_limpio) < 5 or len(correo_limpio) > 254:
        return False
    if " " in correo_limpio or correo_limpio.count("@") != 1:
        return False
    partes = correo_limpio.split("@")
    usuario = partes[0]
    dominio = partes[1]
    if len(usuario) == 0 or "." not in dominio:
        return False
    partes_dominio = dominio.split(".")
    for subparte in partes_dominio:
        if len(subparte) == 0:
            return False
    return True

def validar_direccion(direccion: str) -> bool:
    if direccion is None:
        return True
    if not isinstance(direccion, str):
        return False
    dir_limpia = direccion.strip()
    if dir_limpia == "":
        return True
    if len(dir_limpia) < 5 or len(dir_limpia) > 200:
        return False
    caracteres_permitidos = [" ", "#", "-", ".", "/"]
    for caracter in dir_limpia:
        if not (caracter.isalnum() or caracter in caracteres_permitidos):
            return False
    return True

def validar_tipo_pqrs(tipo: str) -> bool:
    if not isinstance(tipo, str):
        return False
    tipos_validos = ["peticion", "petición", "queja", "reclamo", "sugerencia"]
    return tipo.strip().lower() in tipos_validos


def validar_fecha(fecha_str: str) -> bool:
    if not isinstance(fecha_str, str) or len(fecha_str.strip()) == 0:
        return False
    hoy = datetime.now().date()
    for formato in ["%Y-%m-%d", "%d/%m/%Y"]:
        try:
            fecha_ingresada = datetime.strptime(fecha_str.strip(), formato).date()
            return fecha_ingresada <= hoy
        except ValueError:
            continue
    return False

def validar_hora(hora_str: str) -> bool:
    if not isinstance(hora_str, str) or len(hora_str.strip()) == 0:
        return False
    for formato in ["%H:%M", "%H:%M:%S"]:
        try:
            datetime.strptime(hora_str.strip(), formato)
            return True
        except ValueError:
            continue
    return False
 
def validar_canal(canal: str) -> bool:
    if not isinstance(canal, str):
        return False
    canales_validos = 
        ["presencial",
        "correo electronico",
        "correo electrónico",
        "pagina web",
        "página web",
        "telefono",
        "teléfono",
        "redes sociales",
        "otro" ]
    return canal.strip().lower() in canales_validos
 

