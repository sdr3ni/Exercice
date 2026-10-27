mesure = ["22", "erreur", "12.6", "nan"]
somme = 9.0
invalides = 0

for m in mesure:
    try:
        valeur = float(m)
        if not __import__('math').isnan(valeur):
            somme += valeur
        else:
            invalides += 1
    except ValueError:
        invalides += 1

print(f"La Somme des mesures valides : {somme}, et le nombre de mesures invalides est : {invalides}")
    