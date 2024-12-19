# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 00:38:33 2024

@author: garpo
"""

import os
import csv
from src.api_handler import spotify  # On importe l'objet 'spotify' connecté depuis le fichier api_handler.py

def get_top_hits(year):
    """Récupère la playlist 'Top Hits of YYYY' et les informations associées"""
    query = f"Top Hits of {year}"
    results = spotify.search(q=query, type="playlist", limit=1)
    
    if results['playlists']['items']:
        playlist_id = results['playlists']['items'][0]['id']
        return spotify.playlist_items(playlist_id)
    else:
        print(f"Aucune playlist trouvée pour {year}")
        return None

def extract_data_from_playlist(playlist_data):
    """Extrait les informations des artistes et tracks de la playlist"""
    extracted_data = []

    for item in playlist_data['items']:
        track = item['track']
        if track is None:  # Au cas où certaines playlists contiennent des entrées vides
            continue

        artist = track['artists'][0]  # On prend le nom de l'artiste principal
        artist_info = spotify.artist(artist['id'])

        data = {
            'artist_name': artist['name'],
            'artist_followers': artist_info['followers']['total'],
            'artist_genres': ", ".join(artist_info['genres']),
            'artist_popularity': artist_info['popularity'],
            'track_name': track['name'],
            'album_name': track['album']['name'],
            'release_date': track['album']['release_date'],
            'track_duration': track['duration_ms'] // 1000,  # On converti en secondes
            'track_popularity': track['popularity']
        }

        extracted_data.append(data)
    
    return extracted_data

def save_to_csv(data, filename):
    """Sauvegarde les données extraites dans un fichier CSV"""
    
    os.makedirs('data', exist_ok=True)  # Crée le dossier data s'il n'existe pas

    with open(f"data/{filename}", mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

def main():
    """Récupère les playlists des années 2019 à 2023 et les sauvegarde dans un fichier CSV dans le dossier data/"""
    all_data = []

    for year in range(2019, 2024):
        print(f"Récupération des données pour l'année {year}...")
        playlist_data = get_top_hits(year)
        if playlist_data:
            extracted_data = extract_data_from_playlist(playlist_data)
            all_data.extend(extracted_data)

    if all_data:
        save_to_csv(all_data, "top_hits.csv")
        print("Les données ont été sauvegardées dans le fichier data/top_hits.csv.")

if __name__ == "__main__":
    main()
