# Spotify API Project

## Description
Ce projet utilise l'API Spotify pour récupérer, analyser et visualiser des données des playlists "Top Hits" de 2019 à 2023. Il explore les relations entre la popularité des artistes, leurs followers, et leurs tracks, ainsi que l'évolution des genres musicaux.

## Contenu
- **Données** : Les données consolidées sont dans le fichier `data/top_hits.csv`.
- **Visualisations** : Générées dans le dossier `visuals/`.
- **Scripts** : Tous les scripts Python sont dans le dossier `src/`.
### **1. `api_handler.py`**
**Rôle :**  
Ce script gère la connexion à l'API publique de Spotify. Il permet d'authentifier l'application et initialise un objet `Spotify` pour interagir avec l'API.

---

### **2. `data_retriever.py`**
**Rôle :**  
Ce script interroge l'API Spotify pour récupérer les données des playlists "Top Hits of YYYY" (de 2019 à 2023) et les sauvegarde dans un fichier consolidé au format CSV.

---

### **3. `data_analysis.py`**
**Rôle :**  
Ce script effectue l'analyse des données et génère des visualisations basées sur les données récupérées pour répondre aux questions du sujet.


## Installation
1. Clonez ce dépôt :

   git clone <URL>
   cd spotify_api_project

2. Installez les dépendances : 
  
  pip install -r requirements.txt


## Utilisation 

Exécutez avec python les scripts selon l'ordre suivant :

src/data_retriever.py : Récupération des données
src/data_analysis.py : Analyses et visualisations 

## Résultats : 
Les résultats/réponses sont décrits dans le fichier REPORT.md.