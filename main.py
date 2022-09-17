import functions

#declaration variable 
url =  "https://opendata.paris.fr/api/records/1.0/search/?dataset=chantiers-perturbants&q=&rows=100&facet=cp_arrondissement&facet=typologie&facet=maitre_ouvrage&facet=objet&facet=impact_circulation&facet=niveau_perturbation&facet=statut&facet=description"
record = "records"
field = "fields"
file_name = "cleaned_data.csv"

#ETL 
#Fetch data 
records = functions.fetch_data(url,record)
#Transform data 
df_fields = functions.transform_data(records,field)
#Load data 
load_file = functions.load_data(file_name,df_fields)