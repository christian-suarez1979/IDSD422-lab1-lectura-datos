# inspeccion.R — Tipos, columna derivada e indicadores (R)
# Completa los pasos marcados con TODO. Ejecuta desde la raíz del repositorio:
#   Rscript scripts/inspeccion.R

# TODO 1: carga data/ventas.csv
# TODO 2: imprime la estructura (str) para ver los tipos
#         (fija si region llegó como character o factor)
# TODO 3: crea la columna derivada "ticket" = ventas / clientes
# TODO 4: calcula e imprime:
#         - venta promedio por sucursal (aggregate o dplyr)
#         - ticket promedio (ventas totales / clientes totales)
#         - sucursal con mayor y menor venta
#         - región con mayor venta total
# inspeccion.R – Tipos, columna derivada e indicadores (R)
# Completa los pasos marcados con TODO. Ejecuta desde la raíz del repositorio:
# Rscript scripts/inspeccion.R

library(readr)

ventas <- read_csv("data/ventas.csv")
ventas$ticket <- ventas$ventas / ventas$clientes

print(head(ventas))
cat("\n")

print("--- ESTRUCTURA DE DATOS ---")
str(ventas)


ventas$ticket <- ventas$ventas / ventas$clientes

print("--- INDICADORES ---")

venta_promedio_sucursal <- mean(ventas$ventas)
cat("Venta promedio por sucursal:", venta_promedio_sucursal, "\n")


ticket_promedio_global <- sum(ventas$ventas) / sum(ventas$clientes)
cat("Ticket promedio global:", ticket_promedio_global, "\n")


sucursal_mayor <- ventas$sucursal[which.max(ventas$ventas)]
sucursal_menor <- ventas$sucursal[which.min(ventas$ventas)]
cat("Sucursal con mayor venta:", sucursal_mayor, "\n")
cat("Sucursal con menor venta:", sucursal_menor, "\n")

ventas_por_region <- tapply(ventas$ventas, ventas$region, sum)
region_mayor_venta <- names(ventas_por_region)[which.max(ventas_por_region)]
cat("Región con mayor venta total:", region_mayor_venta, "\n")
