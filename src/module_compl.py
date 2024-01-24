# WEBSCRAPPING MODULE
from bs4 import BeautifulSoup
import requests
import pandas as pd

############################## WEBSCRAPPING INFORMATION METEO
url = "https://www.lameteoagricole.net/meteo-heure-par-heure/Bordeaux-33000.html"
navigator = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1)'
meteo_agricole = requests.get(url, headers={'User-Agent': navigator})
soup = BeautifulSoup(meteo_agricole.text, 'html.parser')
page = soup.find_all('table', {"id" : "heures-table"})
############### JOUR
nom_jour = soup.find_all('span', {"class" : "fw-bold text-shade-3"})
num_jour = soup.find_all('span', {"class" : "fs-5 mb-2 text-shade-3"})
heure = soup.find_all('span', {"class" : "fs-5 mt-1 mb-2"})
############### TEMPERATURE 
temperature = soup.find_all('span', {"class" : "fw-bold fs-4 text-warning"})
############### PRECIPITATION
precipitation = soup.find_all('span', {"class" : "text-gray-200"})
############### CREATION DATAFRAME
df_meteo = pd.DataFrame()
df_meteo['nom_jour'] = [str(jour).split('>')[1].split('<')[0] for jour in nom_jour]
df_meteo['num_jour'] = [str(num).split('>')[1].split('<')[0] for num in num_jour]
df_meteo['heure'] = [str(h).split('>')[1].split('<')[0] for h in heure]
df_meteo['temperature'] = [str(temp).split('>')[1].split('<')[0] for temp in temperature]
df_meteo['temp_unit'] = '°C'
df_meteo['pluie'] = [str(precip).split('fw-bold">')[1].split('</span><span')[0] for precip in precipitation if "Précipitations" in str(precip)]
df_meteo['pluie_unit'] = 'mm'