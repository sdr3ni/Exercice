while True:
    premier = int(input("Entrer un premier nombre à additionner: "))
    deuxieme = int(input("Entrer un deuxième nombre à additionner: "))

    print(f"Somme: {premier + deuxieme}")
    
    continuer = input("Voulez-vous faire une autre addition ? (oui/non) : ").strip().lower()
    
    if continuer == "non" or "d":
        print("Fin du programme.")
        break