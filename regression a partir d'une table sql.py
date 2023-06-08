import pandas as pd
from sklearn.linear_model import LinearRegression
import sqlite3

connexion = sqlite3.connect('prix_maison.db') #on se connecte 

query = "SELECT superficie, distance centre ville, nombre etage, prix FROM table" #on place une requete sql pour selectionner les colonnes d'interet 
data = pd.read_sql_query(query, connexion) #on place le resultat de la requete dans une variable 

info = data[['superficie', 'distance centre ville', 'nombre etage']] #on isole les colonnes d'interet
resultat = data['prix']# de la colonne des resulytats 

model = LinearRegression()

model.fit(info, resultat) #on entraine le modele 

infos_nous = [[float(input()), float(input()), float(input())]]  # on rentre nos valeurs a nous 
resultat_nous = model.predict(infos_nous) #la magie se fait 

print(resultat_nous)