# Sujet Spotify API

# Introduction

L’objectif de ce test technique est la réalisation d’un script Python permettant de récupérer et d’analyser des données disponibles sur l’API publique de Spotify (disponible [ici](https://developer.spotify.com/documentation/web-api)). La durée de réalisation de ce test ne devrait pas excéder une demi-journée. 

# Objectifs

1. Télécharger et formater les tracks présents dans les playlists réalisées par Spotify “**Top Hits of YYYY**” sur les hits des 5 dernières années (2019 à 2023). On souhaite récupérer notamment : 
    1. Les informations liées aux artistes (nom de l’artiste, nombre de followers, genres associés à l’artiste, popularité de l’artiste)
    2. Les informations liées aux tracks (nom du track, nom de l’album associé, date de sortie de l’album, durée du track, popularité du track)
2. Proposer une (ou plusieurs) visualisation(s) permettant de répondre aux questions suivantes : 
    1. La popularité d’un artiste est-elle corrélée à son nombre de followers ? Ou à la popularité de ses tracks ? 
    2. Y a-t-il une évolution des genres les plus écoutés entre 2019 et 2023 ?
3. **(Optionnel, libre**) Proposer des visualisations supplémentaires pouvant être intéressantes. 

Pour les visualisations, elles doivent être accompagnées de **courts textes explicatifs** répondant aux questions. 

# Critères d’évaluation

- Ton code doit être développé dans le but d’être **relu et exécuté facilement** sur un système utilisant Python 3.8
- Utilisation de bibliothèques publiques uniquement
- Le code doit être versionné via Git