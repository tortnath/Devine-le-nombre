import random
#Génère un nombre aléatoire entre 1 et 100

nombre_secret = random.randint(1,100)

print(" Bienvenue dans le jeu : devine le nombre ! ")
print(" J'ai choisi un nombre entre 1 et 100. Peux-tu le retrouver ? ")


#Boucle jusqu'à ce que l'utilisateur trouve le bon nombre
essais = 0

while True:
	proposition = int(input(" Entre ta proposition ? "))
	essais +=1
	
	if proposition < nombre_secret :
		print(" C'est plus grand ! ")
	elif proposition > nombre_secret :
		print(" C'est plus petit ! ")
	else : 
		print(" Bravo ! Tu as trouvé le nombre secret ! ")
		break