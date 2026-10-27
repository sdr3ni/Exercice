import sys

def lire_et_filtrer_fichier(input_file):
    """Étape 1 : Lecture tolérante et filtrage des trames GPS"""
    lines_filtrees = []
    
    with open(input_file, 'r', encoding='latin-1') as fichier:
        for ligne in fichier:
            if "GNSS_ACCESS_LIB" in ligne or "Trip Data" in ligne:
                lines_filtrees.append(ligne.strip())
                
    return lines_filtrees


def extraire_donnees_brutes(lines):
    """Étape 2 : Parsing avancé et gestion des exceptions"""
    records = []
    
    for line in lines:
        try:
            ts = line.split(']')[0].replace('[', '').split('.')[0]
            
            if ':' in line:
                parts = line.split(':')[-1]
            elif '--' in line:
                parts = line.split('--')[-1]
            else:
                parts = line.split('Data')[-1]
                
            items = parts.split('/')
            
            lat = float(items[0].replace('Lat', '').strip())
            lon = float(items[1].replace('Lon', '').strip())
            alt = float(items[2].replace('Alt', '').strip())
            
            records.append((ts, lat, lon, alt))
            
        except (ValueError, IndexError):
            continue
            
    return records


if __name__ == "__main__":
    
    # Lancement Étape 1
    lignes = lire_et_filtrer_fichier("input_log.txt")
    print(f"[ETAPE 1] Lignes retenues: {len(lignes)}")
    
    # Lancement Étape 2 sur les lignes récupérées à l'Étape 1
    donnees = extraire_donnees_brutes(lignes)
    print(f"[ETAPE 2] Données extraites avec succès: {len(donnees)}")
    
    # Affichage de contrôle
    if donnees:
        print(f"Exemple de la première donnée extraite : {donnees[0]}")  