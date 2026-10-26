Nom = str(input("Inscrivez notre nom: "))
Age = int(input("Inscrivez votre âge: "))

if Age >= 18 :
    print(f"{Nom} est éligible au vote")

else:
    print(f"{Nom} n'est pas éligible au vote")