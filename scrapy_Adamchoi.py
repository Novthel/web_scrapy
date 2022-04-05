"""
    La pagina web Adamchoi es una pagina que muestra las estadisticas de los partidos
    de futbol que se juegan en 42 ligas de todo el mundo.
    El programa tiene el objetivo de captar los datos de una liga previamente seleccionada y guardarlos en un archivo csv,
    Por este motivo se programara una busqueda automatica de la liga deseada

"""

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import pandas as pd


website = 'https://www.adamchoi.co.uk/teamgoals/detailed'
path = '/Users/NOVTHEL LTDA/Documents/PROYECTOS/chromedriver'

def search(country):
    #apertura del buscador chrome y obtencion de la website
    driver = webdriver.Chrome(path)
    driver.get(website)

    #seleccion del boton all-matches y programacion automatica (obtener un solo listado de encuentros local-visitante)
    boton_all_matches = driver.find_element_by_xpath('//label[@analytics-event="All matches"]')
    boton_all_matches.click()

    # seleccion del selector de pais y programacion automatica (obtener la liga deseada)
    select_country = Select(driver.find_element_by_id('country'))
    select_country.select_by_visible_text(f'{country}')
    


    time.sleep(10)

    # obtener la data
    data = []

    matches = driver.find_elements_by_tag_name('tr')
    for i in matches:
        data.append(i.text)

    driver.quit()

    df = pd.DataFrame({'matches':data})
    df.to_csv(f'{country}_league.csv', index=False)



if __name__ == "__main__":
    
    print(""" 
          1. England
          2. Spain
          3. Germany
          4. Italy
          5. France
          6. Portugal 
          """)
    
    liga = int(input('Elija la liga deseada: '))
    
    if liga == 1:
        country = 'England'
    elif liga == 2:
        country = 'Spain'
    elif liga == 3:
        country = 'Germany'
    elif liga == 4:
        country = 'Italy'
    elif liga == 5:
        country = 'France'
    elif liga == 6:
        country = 'Portugal'
    
    
    search(country)