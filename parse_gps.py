import sys

def lire_et_filtrer_fichier(input_file):
    lines_filtrees = []
    
    with open(input_file, 'r', encoding='latin-1') as fichier:

        for ligne in fichier:
            
            if "GNSS_ACCESS_LIB" in ligne or "Trip Data" in ligne:
                
                lines_filtrees.append(ligne.strip())
                
    return lines_filtrees

def extraire_donnees_brutes(lines):
    records = []
    
    for line in lines:
       
        try:
            ts = line.split(']')[0].replace('[', '').split('.')[0]
            
            if ':' in line:
                parts = line.split(':')[-1]
            else:
                parts = line.split('Data')[-1]
            
            items = parts.split('/')
            
            lat = float(items[0].replace('Lat', '').strip())
            lon = float(items[1].replace('Lon', '').strip())
            alt = float(items[2].replace('Alt', '').strip())
            
            records.append((ts, lat, lon, alt))
            
        except (ValueError, IndexError):

            pass
            
    return records

if __name__ == "__main__":
    lignes = lire_et_filtrer_fichier("input_log.txt")
    print(f"[ETAPE 1] Lignes retenues: {len(lignes)}")
    
    donnees = extraire_donnees_brutes(lignes)
    print(f"[ETAPE 2] Données extraites avec succès: {len(donnees)}")
    
    if donnees:
        print(f"Exemple de la première ligne : {donnees[0]}")


