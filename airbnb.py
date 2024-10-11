import pandas as pd
import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Configura las opciones del navegador para cambiar el agente de usuario.
# Parámetros:
#    opts (Options): Opciones del navegador que modifican su comportamiento.
opts = Options()
opts.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36")

# Inicia el navegador Chrome con las opciones especificadas.
# Parámetros:
#    service (Service): Servicio de ChromeDriver para gestionar el navegador.
#    options (Options): Opciones de Chrome, como el agente de usuario.
# Retorna:
#    driver (WebDriver): El controlador que permite interactuar con el navegador.
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=opts
)

# Navega a la página principal de Airbnb para los resultados de Barcelona.
# Parámetros:
#    URL (str): La URL de la página web de Airbnb que se va a visitar.
driver.get('https://www.airbnb.com/s/Barcelona--Spain/homes')

# Pausa la ejecución por 3 segundos para que la página cargue completamente.
# Parámetros:
#    tiempo (float): La cantidad de tiempo en segundos para detener la ejecución.
sleep(3)


# Inicializa las listas para almacenar los datos obtenidos de los listados de Airbnb.
# Listas:
#    titulos_totales (list): Almacena los títulos de las propiedades.
#    descripciones_totales (list): Almacena las descripciones de las propiedades.
#    precios_totales (list): Almacena los precios por noche de las propiedades.
#    calificaciones_totales (list): Almacena las calificaciones de las propiedades.
#    fechas_totales (list): Almacena las fechas relevantes.
titulos_totales = []
descripciones_totales = []
precios_totales = []
calificaciones_totales = []
fechas_totales = []

# Lista de los nombres de los meses en español, utilizada para identificar fechas en los anuncios.

meses = ['ene', 'feb', 'mar', 'abr', 'may', 'jun', 'jul', 'ago', 'sep', 'oct', 'nov', 'dic']

# Establece el número de páginas que se van a recorrer para extraer los datos.
paginas = 7

# Ciclo para recorrer las páginas de resultados y extraer datos de las propiedades.
# Parámetros:
#    i (int): Índice del ciclo que controla cuántas páginas se procesan.
for i in range(paginas):
    # Extrae los títulos de los listados de propiedades.
    # Parámetros:
    #    XPATH (str): La expresión XPath que localiza los títulos.
    titulos_anuncios = driver.find_elements(By.XPATH, '//div[@data-testid="listing-card-title"]')
    for titulo in titulos_anuncios:
        print(titulo.text)
        titulos_totales.append(titulo.text)

    # Extrae las descripciones de las propiedades.
    # Parámetros:
    #    XPATH (str): La expresión XPath que localiza las descripciones.
    descripcion_anuncios = driver.find_elements(By.XPATH, '//div[@itemprop="itemListElement"]')
    for descripcion in descripcion_anuncios:
        propiedad = descripcion.find_element(By.XPATH, './/meta[@itemprop="name"]')
        print(propiedad.text)
        descripciones_totales.append(propiedad.text)

    # Extrae los precios por noche de las propiedades.
    # Parámetros:
    #    XPATH (str): La expresión XPath que localiza los precios.
    precios_por_noche = driver.find_elements(By.XPATH, '//div[@data-testid="price-availability-row"]')
    for precio in precios_por_noche:
        print(precio.text)
        precios_totales.append(precio.text)

    # Extrae las calificaciones de las propiedades.
    # Parámetros:
    #    XPATH (str): La expresión XPath que localiza las calificaciones.
    calificaciones = driver.find_elements(By.XPATH, '//span[@class="a8jt5op atm_3f_idpfg4 atm_7h_hxbz6r atm_7i_ysn8ba atm_e2_t94yts atm_ks_zryt35 atm_l8_idpfg4 atm_vv_1q9ccgz atm_vy_t94yts au0q88m atm_mk_stnw88 atm_tk_idpfg4 dir dir-ltr"]')
    for calificacion in calificaciones:
        print(calificacion.text)
        calificaciones_totales.append(calificacion.text)

    # Extrae las fechas que se muestran en los listados.
    # Parámetros:
    #    XPATH (str): La expresión XPath que localiza las fechas.
    fechas = driver.find_elements(By.XPATH, '//div[@data-testid="listing-card-subtitle"]//span')
    for fecha in fechas:
        texto = fecha.text.lower()
        if any(mes in texto for mes in meses):  
            print(texto)
            fechas_totales.append(texto)

    # Intenta hacer clic en el botón "Siguiente" para cargar la siguiente página de resultados.
    # Parámetros:
    #    XPATH (str): La expresión XPath que localiza el botón "Siguiente".
    #    e (Exception): Excepción lanzada si no se encuentra el botón "Siguiente".
    try:
        siguiente_boton = driver.find_element(By.XPATH, '//a[@aria-label="Siguiente"]')
        siguiente_boton.click()  
        # Pausa entre 8 y 10 segundos para evitar detección de automatización.
        sleep(random.uniform(8.0, 10.0))  
    except Exception as e:
        print(f"No se pudo encontrar el botón 'Siguiente': {e}")
        break  

# Cierra el navegador una vez finalizada la recolección de datos.
driver.quit()



# Verifica y muestra las longitudes de las listas de datos recolectados.
print(f"Longitud de títulos: {len(titulos_totales)}")
print(f"Longitud de descripciones: {len(descripciones_totales)}")
print(f"Longitud de precios: {len(precios_totales)}")
print(f"Longitud de calificaciones: {len(calificaciones_totales)}")
print(f"Longitud de fechas: {len(fechas_totales)}")


# Encuentra la longitud máxima entre las listas recolectadas.
longitud_maxima = max(len(titulos_totales), len(descripciones_totales), len(precios_totales), len(calificaciones_totales), len(fechas_totales))

# Rellena las listas más cortas con valores vacíos para igualarlas en longitud.
titulos_totales += [''] * (longitud_maxima - len(titulos_totales))
descripciones_totales += [''] * (longitud_maxima - len(descripciones_totales))
precios_totales += [''] * (longitud_maxima - len(precios_totales))
calificaciones_totales += [''] * (longitud_maxima - len(calificaciones_totales))
fechas_totales += [''] * (longitud_maxima - len(fechas_totales))

# Crea un diccionario con los datos recolectados.
# Parámetros:
#    data (dict): Un diccionario que contiene las listas con los datos.
    
data = {
'Titulo': titulos_totales,
    'Descripcion': descripciones_totales,
    'Precio por Noche': precios_totales,
    'Calificacion': calificaciones_totales,
    'Fecha': fechas_totales
}

# Crea un DataFrame a partir del diccionario de datos.
# Parámetros:
#    df_airbnb (DataFrame): Un DataFrame que contiene los datos de los anuncios de Airbnb.
df_airbnb = pd.DataFrame(data)



# Guarda el DataFrame en un archivo CSV.
# Parámetros:
#    archivo (str): El nombre del archivo CSV donde se guardarán los datos.
df_airbnb.to_csv('propiedades_airbnb.csv', index=False)

