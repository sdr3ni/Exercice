import sys
import math

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

def nettoyer_et_dedoublonner(records):
    cleaned = []
    for ts, lat, lon, alt in records:
        if math.isnan(lat) or math.isnan(lon) or math.isnan(alt):
            continue
            
        lat_r = round(lat, 2)
        lon_r = round(lon, 2)
        alt_r = round(alt, 2)
        
        if cleaned:
            last_lat = cleaned[-1][1]
            last_lon = cleaned[-1][2]
            if abs(lat_r - last_lat) <= 1.0 and abs(lon_r - last_lon) <= 1.0:
                continue
                
        cleaned.append((ts, lat_r, lon_r, alt_r))
    return cleaned

if __name__ == "__main__":
    lignes = lire_et_filtrer_fichier("input_log.txt")
    print(f"[ETAPE 1] Lignes retenues: {len(lignes)}")
    
    donnees = extraire_donnees_brutes(lignes)
    print(f"[ETAPE 2] Données extraites avec succès: {len(donnees)}")
    
    donnees_propres = nettoyer_et_dedoublonner(donnees)
    print(f"[ETAPE 3] Points nettoyés et dédoublonnés: {len(donnees_propres)}")