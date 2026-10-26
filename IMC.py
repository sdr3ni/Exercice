Poids = float(input ("Entrez votre poids: "))
Taille = float(input ("Entrez votre taille: "))

if Taille > 0:
    imc = Poids/ (Taille ** 2)
    print(f"Votre IMC: {imc:.2f}")

else:
    print("Met une vraie taille gros")