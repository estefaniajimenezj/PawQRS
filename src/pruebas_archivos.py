
import tempfile
import archivos


# ==========================================
# PRUEBAS DEL MODULO DE ALMACENAMIENTO PAWQRS
# ==========================================

# Crear una carpeta temporal para no modificar
# los archivos reales del proyecto.

with tempfile.TemporaryDirectory() as carpeta_temporal:

    archivos.DATA_DIR = carpeta_temporal

    print("\n========== INICIO DE LAS PRUEBAS ==========\n")

    # --------------------------------------
    # PRUEBA 1: GUARDAR UNA PETICION
    # --------------------------------------

    datos = {
        "tipo_solicitud": "peticion",
        "nombre_completo": "Usuario de prueba",
        "estado_peticion": ""
    }

    resultado = archivos.guardar_registro(datos)

    assert resultado is True

    registro = archivos.buscar_por_radicado(
        "peticion", "PET-0001"
    )

    assert registro is not None
    assert registro["id"] == 1
    assert isinstance(registro["id"], int)
    assert registro["estado_peticion"] == "Registrada"
    assert registro["fecha_solucion"] == ""

    print("PRUEBA 1 SUPERADA: Registro inicial correcto.")

    # --------------------------------------
    # PRUEBA 2: ID CONSECUTIVO
    # --------------------------------------

    resultado = archivos.guardar_registro(datos)

    assert resultado is True

    segundo = archivos.buscar_por_radicado(
        "peticion", "PET-0002"
    )

    assert segundo is not None
    assert segundo["id"] == 2

    print("PRUEBA 2 SUPERADA: IDs consecutivos.")

    # --------------------------------------
    # PRUEBA 3: ID INDEPENDIENTE POR TIPO
    # --------------------------------------

    datos_queja = {
        "tipo_solicitud": "queja",
        "nombre_completo": "Usuario de prueba"
    }

    resultado = archivos.guardar_registro(datos_queja)

    assert resultado is True

    queja = archivos.buscar_por_radicado(
        "queja", "QUE-0001"
    )

    assert queja is not None
    assert queja["id"] == 1

    print("PRUEBA 3 SUPERADA: Numeracion independiente.")

    # --------------------------------------
    # PRUEBA 4: RECHAZAR TRANSICION INCORRECTA
    # --------------------------------------

    resultado = archivos.actualizar_estado(
        "peticion",
        "PET-0001",
        "Solucionada"
    )

    assert resultado is False

    registro = archivos.buscar_por_radicado(
        "peticion", "PET-0001"
    )

    assert registro["estado_peticion"] == "Registrada"

    print("PRUEBA 4 SUPERADA: Transicion incorrecta rechazada.")

    # --------------------------------------
    # PRUEBA 5: CAMBIAR A EN PROCESO
    # --------------------------------------

    resultado = archivos.actualizar_estado(
        "peticion",
        "PET-0001",
        "En proceso"
    )

    assert resultado is True

    registro = archivos.buscar_por_radicado(
        "peticion", "PET-0001"
    )

    assert registro["estado_peticion"] == "En proceso"
    assert registro["fecha_solucion"] == ""

    print("PRUEBA 5 SUPERADA: Cambio a En proceso.")

    # --------------------------------------
    # PRUEBA 6: CAMBIAR A SOLUCIONADA
    # --------------------------------------

    resultado = archivos.actualizar_estado(
        "peticion",
        "PET-0001",
        "Solucionada"
    )

    assert resultado is True

    registro = archivos.buscar_por_radicado(
        "peticion", "PET-0001"
    )

    assert registro["estado_peticion"] == "Solucionada"
    assert registro["fecha_solucion"] != ""

    print("PRUEBA 6 SUPERADA: Fecha de solucion registrada.")

    # --------------------------------------
    # PRUEBA 7: RECHAZAR ESTADO NO PERMITIDO
    # --------------------------------------

    resultado = archivos.actualizar_estado(
        "peticion",
        "PET-0001",
        "Cerrado"
    )

    assert resultado is False

    print("PRUEBA 7 SUPERADA: Estado no permitido rechazado.")

    # --------------------------------------
    # PRUEBA 8: RECHAZAR RETROCESO DE ESTADO
    # --------------------------------------

    resultado = archivos.actualizar_estado(
        "peticion",
        "PET-0001",
        "En proceso"
    )

    assert resultado is False

    registro = archivos.buscar_por_radicado(
        "peticion", "PET-0001"
    )

    assert registro["estado_peticion"] == "Solucionada"

    print("PRUEBA 8 SUPERADA: No se permite retroceder de estado.")

    print("\n========== TODAS LAS PRUEBAS FUERON SUPERADAS ==========\n")
