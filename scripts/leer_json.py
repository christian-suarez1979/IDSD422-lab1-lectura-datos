# leer_json.py — Cargar el reporte JSON de la API (Python)
# Completa los pasos marcados con TODO. Ejecuta desde la raíz del repositorio:
#   python scripts/leer_json.py

# TODO 1: importa json y pandas
# TODO 2: carga data/ventas.json con json.load
# TODO 3: convierte la lista de diccionarios en un DataFrame
#         (recuerda del cap. 2: el JSON no llega como tabla directa)
# TODO 4: imprime las dimensiones y las primeras filas
import json
import pandas as pd

with open("data/ventas.json", encoding="utf-8") as f:
  datos= json.load(f)

  ventas=pd.json_normalize(datos)
#imprimir los primeros elementos
print(ventas.head())
#imprimir las dimensiones(filas y comlumnas)
print("Dimensiones: " , ventas.shape)
#imprimir los tipos de columna
print("\nTipos de columna")
print(ventas.dtypes)