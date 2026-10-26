conversion = int(input("Donnez une durée en seconde: "))
Heure = conversion // 3600
reste = conversion % 3600 
minutes = reste // 60
seconde = reste % 60

print(f"{Heure}h {minutes}min {seconde}s")


