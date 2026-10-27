import csv
import hashlib
import math
import sys


PRECISION = 6      
SEUIL_DEDOUBL = 0.0005   

INPUT_FILE = "input_log.txt"
OUTPUT_FILE = "output_cleaned.csv"


# --- ETAPE 1 
def lire_et_filtrer_fichier(input_file):
    lines_filtrees = []
    with open(input_file, "r", encoding="latin-1", errors="replace") as f:
        for line in f:
            if "GNSS_ACCESS_LIB" in line or "Trip Data" in line:
                lines_filtrees.append(line.strip())
    return lines_filtrees


# --- ETAPE 2
def extraire_donnees_brutes(lines):
    """Retourne une liste de tuples (index, timestamp, lat, lon, source).

    Deux formats coexistent dans le dump :
      A) CSV : 1176,2019/10/25,12:57:06.597179,"45.766214, 4.834682",GNSS_ACCESS_LIB
      B) Trip Data : latitude et longitude sur DEUX lignes consécutives, sans
         index ni horodatage -> index/timestamp laissés vides (rien n'est inventé).
    """
    records = []
    lat_en_attente = None

    for line in lines:
        try:
            if line.startswith("Trip Data"):
                valeur = line.split(":")[-1].strip()
                if "Latitude" in line:
                    lat_en_attente = float(valeur)
                elif "Longitude" in line:
                    if lat_en_attente is None:
                        continue 
                    records.append(("", "", lat_en_attente, float(valeur), "TRIP_DATA"))
                    lat_en_attente = None
            else:
                lat_en_attente = None
                champs = next(csv.reader([line]))
                index, date, heure, coords, source = champs  
                timestamp = date.replace("/", "-") + " " + heure.split(".")[0]
                lat_s, lon_s = coords.split(",")
                records.append((int(index), timestamp, float(lat_s), float(lon_s), source))
        except (ValueError, IndexError, StopIteration):
            continue  
    return records


# --- ETAPE 3
def nettoyer_et_dedoublonner(records):
    cleaned = []
    for index, ts, lat, lon, source in records:
        if math.isnan(lat) or math.isnan(lon):
            continue
        lat_r, lon_r = round(lat, PRECISION), round(lon, PRECISION)
        if cleaned:
            last_lat, last_lon = cleaned[-1][2], cleaned[-1][3]
            if abs(lat_r - last_lat) <= SEUIL_DEDOUBL and abs(lon_r - last_lon) <= SEUIL_DEDOUBL:
                continue
        cleaned.append((index, ts, lat_r, lon_r, source))
    return cleaned


# --- ETAPE 4
def exporter_et_hasher(cleaned_records, output_file=OUTPUT_FILE):
    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["index", "timestamp", "latitude", "longitude", "source"])
        writer.writerows(cleaned_records)

    h = hashlib.sha256()
    with open(output_file, "rb") as f:
        for bloc in iter(lambda: f.read(8192), b""):
            h.update(bloc)
    sha256_hash = h.hexdigest()

    print(f"SHA-256: {sha256_hash}")
    print(f"FLAG: FLAG_OCLCC_{sha256_hash[:12]}")
    return sha256_hash


if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else INPUT_FILE

    lignes = lire_et_filtrer_fichier(input_file)
    print(f"[ETAPE 1] Lignes retenues : {len(lignes)}")

    brutes = extraire_donnees_brutes(lignes)
    print(f"[ETAPE 2] Enregistrements extraits : {len(brutes)}")

    propres = nettoyer_et_dedoublonner(brutes)
    print(f"[ETAPE 3] Points nettoyés et dédoublonnés : {len(propres)}")

    exporter_et_hasher(propres)