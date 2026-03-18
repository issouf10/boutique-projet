# script.py

# Initialisation des compteurs
longueur = 0
nb_mots = 1  # On commence à 1 car le premier mot n'a pas d'espace avant
nb_voyelles = 0

# Demande de saisie à l'utilisateur
phrase = input("Tape une phrase qui se termine par un point : ")

# Traitement caractère par caractère
for caractere in phrase:
    longueur += 1
    if caractere.lower() in "aeiouy":
        nb_voyelles += 1
    if caractere == " ":
        nb_mots += 1

# Affichage des résultats
print("Longueur de la phrase :", longueur)
print("Nombre de mots :", nb_mots)
print("Nombre de voyelles :", nb_voyelles)