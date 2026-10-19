# Informe técnico — Consolidación de reportes de ventas

**Para:** Gerencia de RetailAndina S.A. · **De:** Equipo de Business Intelligence
**Fecha:** _19__/_10__/2026 · **Asunto:** Primer análisis de los reportes de ventas (semana 39)

---

## Resumen ejecutivo

Tras auditar la consistencia de los datos de ventas en formatos CSV, JSON y Excel, se confirmó que las 5 sucursales coinciden plenamente en todas las fuentes, sumando un total de $60,040 en ingresos. Por su simplicidad operativa y rendimiento, se sugiere adoptar la entrega en archivos CSV.

## 1. ¿Los tres formatos contienen la misma información?

*Carga los tres archivos (CSV, JSON y Excel) en Python y en R, y compara dimensiones y estructura. Completa la tabla:*

| Formato | Origen | Filas | Columnas | Lectura en código |
|---|---|---|---|---|
| CSV | ERP de sucursales |5 |4 |ventas = pd.read_csv("data/ventas.csv") / ventas <- read_csv("data/ventas.csv")
| JSON | API de fidelización |5 | 4| datos= json.load(f)+ventas=pd.json_normalize(datos)  / ventas<- fromJSON("data/ventas.json")
| Excel | Consolidado de finanzas |5 | 4| ventas = pd.read_excel("data/ventas.xlsx", sheet_name="ventas")  /  ventas <- read_excel("data/ventas.xlsx", sheet="ventas")

*Responde: ¿la estructura interna del archivo (texto plano, anidada, binaria) cambia el contenido?*

No, la estructura interna del archivo no cambia el contenido. Durante la consolidacion  de los reportes de ventas se evidenció que todos los formatos contienen 5 filas y 4 columnas.

## 2. Tipos de datos y calidad

*Inspecciona los tipos que infiere cada lenguaje. Completa la tabla y comenta si los tipos son los esperados para cada variable:*

| Variable | Tipo inferido (Python) | Tipo inferido (R) | Interpretación |
|---|---|---|---|
| `ventas` |int64 |double |Numérica continua representa ingresos monetarios |
| `clientes` |int64 |double |Numérica discreta número de clientes |
| `sucursal` |object |character |Categórica nominal etiquetas de ciudad |
| `region` |object |character |Categórica nominal etiquetas de región|

*¿Qué habría indicado un dato sucio si, por ejemplo, `ventas` llegara como texto?*

Habría indicado la presencia de datos sucios como caracteres no numéricos  como $, comas, valores vacíos N/A, lo que impediría tratar la variable como numérica continua para realizar operaciones matemáticas. Por ello, se debe aplicar un proceso de limpieza.

## 3. Particularidades técnicas encontradas

*Anota qué encontraste al leer cada formato (una nota por formato): ¿el JSON llegó como tabla? ¿hubo que indicar una hoja en el Excel? ¿cómo se expresan las categóricas en cada lenguaje?*

CSV: Fue el formato más ligero y rápido de procesar en los dos lenguajes.

JSON: Requirió aplanamiento en python para transformar la estructura anidada en una tabla.

Excel: Requirió colocar explícitamente el nombre de la hoja en este caso ventas para evitar leer hojas vacías.

## 4. Indicadores para la reunión del lunes

*Calcula los indicadores con los datos consolidados y completa la tabla:*

| Indicador | Valor |
|---|---|
| Venta promedio por sucursal |12.008 |
| Ticket promedio (ventas ÷ clientes) |38.07229 |
| Sucursal con mayor venta |Guayaquil Centro  |
| Sucursal con menor venta |Cuenca  |
| Región con mayor venta total |Sierra  |

## 5. Conclusiones y recomendación

1.Se garantiza que los tres archivos de reporte están sincronizados,son consistentes y no presentan diferencias numéricas en los resultados calculdos en ambos programas. 

2.Se recomienda principalmente hacer un mayor uso de CSV  JSON para automatizaciones, ya que Excel consume más recursos de memoria.

3.Se evidenció que la región Sierra concentra la mayor venta total con $30,860, pero la sucursal líder es Guayaquil Centro con $15,200. Se recomienda revisar la estrategia comercial en Cuenca por registrar la venta más baja de la red con $8,540.