
name: Pruebas del proyecto PAWQRS

on:
  push:
  pull_request:

jobs:
  pruebas:
    runs-on: ubuntu-latest

    steps:
      - name: Descargar repositorio
        uses: actions/checkout@v4

      - name: Configurar Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Comprobar sintaxis
        run: python -m py_compile src/archivos.py

      - name: Ejecutar pruebas
        run: python src/pruebas_archivos.py
