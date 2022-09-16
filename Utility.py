from dataclasses import field
import pandas as pd 
import requests 
#declaration variables 
url =  "https://opendata.paris.fr/api/records/1.0/search/?dataset=chantiers-perturbants&q=&rows=4&facet=cp_arrondissement&facet=typologie&facet=maitre_ouvrage&facet=objet&facet=impact_circulation&facet=niveau_perturbation&facet=statut&facet=description"

# fetch data 
response = requests.get(url)
response.raise_for_status()
contenu = response.json()
records = contenu["records"]
# Transformation 

df = pd.DataFrame.from_dict(records)

df_cleaned = df["fields"]

dict_fields = df_cleaned.to_dict()
dict_values = dict_fields.values()

df_final = pd.DataFrame.from_dict(dict_values)

print(df_final)
