# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 00:20:28 2024

@author: garpo
"""

import os
from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

# Chargement des variables d'environnement
load_dotenv()

# Récupération de mes identifiants
client_id = os.getenv('SPOTIPY_CLIENT_ID')
client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')

# Authentification
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
spotify = Spotify(auth_manager=auth_manager)

# On rend l'objet 'spotify' disponible pour d'autres modules
__all__ = ['spotify']

def test_connection():
    results = spotify.search(q="Top Hits", limit=1)
    print("Connexion réussie ! Voici un exemple de résultat :")
    print(results)

# Décommentez la ligne ci-dessous uniquement pour tester la connection
#test_connection()

