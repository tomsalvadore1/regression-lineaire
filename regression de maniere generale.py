import numpy as np
from sklearn.linear_model import LinearRegression

caracs = np.array([[100, 5, 1], [50, 15, 0], [150, 1, 1]])  #données d'entrainement (conditions) sous forme de array 
resulats = np.array([200000, 100000, 800000])  #données d'entrainement (resultats)

modele = LinearRegression() #ca il le faut toujours 

modele.fit(caracs, resulats) #entrainement du modele 

a_predir = np.array([120, 3, 1])  #nos valeurs sous forme de array 
prediction= modele.predict(a_predir) #la magie 

print(prediction)  