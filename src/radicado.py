
from pathlib import Path
import textwrap
import unicodedata

ANCHO = 120


def texto_ascii(valor):
    texto = unicodedata.normalize("NFKD", str(valor))
    texto = texto.encode("ascii", "ignore").decode("ascii")
    texto = texto.replace("|", "/")
    texto = " ".join(texto.split())
    return texto


def fila(texto=""):
    texto = texto_ascii(texto)
    return "| " + texto.ljust(ANCHO - 4) + " |"


def filas_campo(etiqueta, valor):
    contenido = f"{etiqueta}: {valor}"

    partes = textwrap.wrap(
        texto_ascii(contenido),
        width=ANCHO - 4,
        break_long_words=True,
        break_on_hyphens=False,
        replace_whitespace=True,
        drop_whitespace=True)

    return [fila(parte) for parte in (partes or [""])]


def generar_comprobante(datos):
    tipo = str(datos["tipo_solicitud"]).strip()

    codigos = {"Peticion": "PET",
        "Queja": "QUE",
        "Reclamo": "REC",
        "Sugerencia": "SUG"}

    tipo_normalizado = texto_ascii(tipo).capitalize()

    if tipo_normalizado not in codigos:
        raise ValueError("Tipo de solicitud no valido")

    identificador = int(datos["id"])

    if identificador < 1:
        raise ValueError("El identificador debe ser positivo")

    codigo = codigos[tipo_normalizado]
    radicado = f"{codigo}-{identificador:04d}"

    borde = "+" + "-" * (ANCHO - 2) + "+"

    lineas = [borde,
        fila("PAWQRS - GESTOR DE PQRS"),
        fila("COMPROBANTE DE RADICACION PQRS"),
        borde]

    campos = [
        ("ID de registro", datos["id"]),
        ("Radicado", radicado),
        ("Tipo de solicitud", tipo),
        ("Fecha de radicacion", datos["fecha_radicacion"]),
        ("Hora de radicacion", datos["hora_radicacion"]),
        ("Estado", datos["estado_peticion"]),
        ("Fecha maxima de respuesta", datos["fecha_maxima_respuesta"]),
        ("Nombre completo", datos["nombre_completo"]),
        ("Tipo de documento", datos["tipo_documento"]),
        ("Numero de documento", datos["numero_documento"]),
        ("Tipo de telefono", datos["tipo_telefono"]),
        ("Telefono de contacto", datos["telefono_contacto"]),
        ("Correo electronico", datos["correo_electronico"]),
        ("Direccion", datos.get("direccion") or "N/A"),
        ("Canal de recepcion", datos["canal_recepcion"]),
        ("Tipo de mascota", datos["tipo_mascota"]),
        ("Campus relacionado", datos["campus_relacionado"]),
        ("Asunto", datos["asunto_titulo"])]

    for etiqueta, valor in campos:
        lineas.extend(filas_campo(etiqueta, valor))

    lineas.append(borde)

    if not all(len(linea) == ANCHO for linea in lineas):
        raise ValueError("Las lineas deben tener 120 caracteres")

    carpeta = (
        Path(__file__).resolve().parent.parent
        / "data"
        / "comprobantes")

    carpeta.mkdir(parents=True, exist_ok=True)

    ruta = carpeta / f"Comprobante_{codigo}_{identificador:04d}.txt"

    contenido = "\n".join(lineas) + "\n"

    with open(ruta, "w", encoding="ascii", newline="\n") as archivo:
        archivo.write(contenido)

    print(contenido, end="")
    print("Comprobante guardado en:", ruta)

    return ruta

    


   