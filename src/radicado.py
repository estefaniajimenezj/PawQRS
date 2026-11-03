if __name__ == "__main__":

    print("REGISTRO DE PQRS")
    print("-------------------------")

    datos = {
        "radicado": input("Ingrese el numero de radicado: "),
        "tipo": input("Ingrese el tipo de PQRS: "),
        "solicitante": input("Nombre del solicitante: "),
        "mascota": input("Nombre de la mascota: "),
        "campus": input("Ingrese el campus: "),
        "estado": input("Estado de la PQRS: "),
        "fecha_maxima": input("Fecha maxima de respuesta: ")
    }

    generar_comprobante(datos)

   
