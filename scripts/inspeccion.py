# inspeccion.py — Tipos, columna derivada e indicadores (Python)
# Completa los pasos marcados con TODO. Ejecuta desde la raíz del repositorio:
#   python scripts/inspeccion.py

# TODO 1: carga data/ventas.csv
# TODO 2: imprime los tipos (dtypes) de cada columna
# TODO 3: crea la columna derivada "ticket" = ventas / clientes
# TODO 4: calcula e imprime:
#         - venta promedio por sucursal
#         - ticket promedio (ventas totales / clientes totales)
#         - sucursal con mayor y menor venta
#         - región con mayor venta total
# inspeccion.py – Tipos, columna derivada e indicadores (Python)
# Completa los pasos marcados con TODO. Ejecuta desde la raíz del repositorio:
# python scripts/inspeccion.py

import pandas as pd


ventas = pd.read_csv("data/ventas.csv")
ventas["ticket"] = ventas["ventas"] / ventas["clientes"]
print(ventas.head())
print("\n")

print("--- TIPOS DE COLUMNA ---")
print(ventas.dtypes)
print("\n -----------------")



print("--- INDICADORES ---")
# - venta promedio por sucursal
print("Venta promedio por sucursal:", ventas["ventas"].mean())

ticket_promedio_global = ventas["ventas"].sum() / ventas["clientes"].sum()
print("Ticket promedio global:", ticket_promedio_global)

sucursal_mayor = ventas.loc[ventas["ventas"].idxmax(), "sucursal"]
sucursal_menor = ventas.loc[ventas["ventas"].idxmin(), "sucursal"]
print(f"Sucursal con mayor venta: {sucursal_mayor}")
print(f"Sucursal con menor venta: {sucursal_menor}")


ventas_por_region = ventas.groupby("region")["ventas"].sum()
region_mayor_venta = ventas_por_region.idxmax()
print(f"Región con mayor venta total: {region_mayor_venta}")

