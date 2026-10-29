def generar_comprobante(datos):
    ancho = 50
    linea = "+" + "-" * ancho + "+"

    print("\n" + linea)
    print("|" + "PAWQRS - COMPROBANTE DE PQRS".center(ancho) + "|")
    print(linea)

    print("|" + f"Radicado: {datos['radicado']}".ljust(ancho) + "|")
    print("|" + f"Tipo: {datos['tipo']}".ljust(ancho) + "|")
    print("|" + f"Solicitante: {datos['solicitante']}".ljust(ancho) + "|")
    print("|" + f"Mascota: {datos['mascota']}".ljust(ancho) + "|")
    print("|" + f"Campus: {datos['campus']}".ljust(ancho) + "|")
    print("|" + f"Estado: {datos['estado']}".ljust(ancho) + "|")
    print("|" + f"Fecha máxima: {datos['fecha_maxima']}".ljust(ancho) + "|")

    print(linea)
