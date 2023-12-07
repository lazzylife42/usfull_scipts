import hashlib

hash_a_trouver = "4e2de42b4851d607e6ed588ac2ad24b3"

# Ouvrir le fichier password.txt et lire chaque mot de passe
with open("passwords.txt", "r") as file:
    for line in file:
        mot_de_passe = line.strip()
        hashed = hashlib.md5(mot_de_passe.encode()).hexdigest()
        if hashed == hash_a_trouver:
            print(f"Mot de passe correspondant trouvé : {mot_de_passe}")
            break

