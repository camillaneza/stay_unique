# stay_unique

# Proyecto de Scraping de Airbnb

Este proyecto tiene como objetivo extraer datos de propiedades de Airbnb en Barcelona, realizar un proceso de ETL (Extracción, Transformación y Carga) y llevar a cabo un análisis exploratorio de datos (EDA) de dos datasets proporcionados; uno de propiedades (Properties) y otro de reservas (Bookings), con información de propiedades vacacionales recopilada en el último año.

## Configuración del Entorno:

Para configurar el entorno y ejecutar el proyecto, siga estos pasos:

1. **Instalar Python:**
Asegúrate de tener instalada la versión 3.7 o superior de Python.

2. **Crear un entorno virtual:** (opcional, pero recomendado):
   *```bash*
   *python -m venv venv*
   *source venv/bin/activate*  # Para Linux/Mac
   *venv\Scripts\activate*  # Para Windows

3. **Instalar las dependencias:** 
Utiliza pip para instalar las bibliotecas necesarias:
*pip install pandas selenium webdriver-manager*

4. **Configuración del WebDriver:**
Este proyecto utiliza Chrome como navegador. Asegúrese de tener la última versión de Chrome instalada y que el WebDriver se instale automáticamente con webdriver-manager.

## Ejecución de Scripts:
Para ejecutar el script de scraping, sigue estos pasos:

1. Asegúrese de estar en el directorio donde se encuentra el script airbnb.py.

2. Ejecuta el script utilizando el siguiente comando:
*python airbnb.py*

## Decisiones de Limpieza de Datos:
Durante el proceso de limpieza de datos, se tomarán las siguientes decisiones:

1. **Manejo de longitudes desiguales:** Se verificaron las longitudes de las listas de datos extraídos. En caso de que las longitudes fueran desiguales, se rellenaron las listas más cortas con valores vacíos para evitar errores al crear el DataFrame de pandas.

2. **Eliminación de datos irrelevantes:** Se eliminaron datos que no cumplieron con los criterios de interés (por ejemplo, propiedades sin precios o calificaciones).

## Descripción del Pipeline de ETL:
El pipeline de ETL implementado consta de las siguientes etapas:

1. **Extracción:** Se utiliza Selenium para navegar por las páginas de Airbnb y extraer datos relevantes como títulos, descripciones, precios, calificaciones y fechas de las propiedades.

2. **Transformación:** Los datos extraídos se almacenan en listas. Se realiza una limpieza para asegurarse de que todas las listas tengan la misma longitud antes de crear el DataFrame.

3. **Carga:** Finalmente, el DataFrame se guarda en un archivo CSV para su posterior análisis.

## Retos y problemas encontrados:
Durante el proceso de desarrollo, se encontraron los siguientes retos:

1. **Cambio en la estructura de la página:** En ocasiones, la estructura del HTML de la página de Airbnb puede cambiar, lo que requiere ajustes en las expresiones XPath utilizadas para extraer datos. Se implementarán controles para manejar excepciones si los elementos no se encuentran.

2. **Tiempos de espera:** La carga de la página puede variar, lo que puede provocar que el script sleep con un rango aleatorio para mitigar

3. **Longitudes desiguales en listas:** Al extraer datos, se encontró que algunas listas

## Procesos de ETL y EDA de datasets proporcionados:
Se realizó el proceso de ETL y EDA de cada datasets, inspeccionando y analizando exhaustivamente cada columna, eliminando valores duplicados, cambiando ciertos valores equívocos, cambiando a tipo datetime las columnas que contenian fechas, se analizaron valores atípicos, se unieron ambos dataframes y se analizaron los valores de distintas variables. Luego, se guardo en un CSV como *"archivo_final.csv".*

