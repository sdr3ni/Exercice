import getpass
Password = getpass.getpass("définissez un mdp: ")

Vérification = ""

while Vérification != Password:
    Vérification = getpass.getpass("Saisissez votre mdp: ")
    if Vérification != Password:
        print("Mdp incorrect, réessayez.")

print("Mdp correct, Accès autorisé")



