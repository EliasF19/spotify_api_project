# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 01:23:42 2024

@author: garpo
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Chargement des données depuis le CSV
df = pd.read_csv('data/top_hits.csv')


''' QUESTION a : La popularité d’un artiste est-elle corrélée à son nombre de followers ? Ou à la popularité de ses tracks ?''' 

# Calculer les coefficients de corrélation pour toutes les variables pertinentes
correlation_matrix = df[['artist_popularity', 'track_popularity', 'artist_followers']].corr()

# Visualisation des corrélations avec une heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', vmin=-1, vmax=1)
plt.title("Matrice de Corrélation")
plt.savefig('visuals/correlation_heatmap.png')
plt.show()

# Corrélation entre popularité et nombre de followers
plt.figure(figsize=(8, 6))
sns.scatterplot(x='artist_followers', y='artist_popularity', data=df)
plt.title('Corrélation : Popularité vs Nombre de Followers')
plt.xlabel('Nombre de Followers')
plt.ylabel('Popularité de l\'Artiste')
plt.grid(True)
plt.savefig('visuals/popularity_vs_followers.png')
plt.show()

# Corrélation entre popularité de l'artiste et popularité des tracks
plt.figure(figsize=(8, 6))
sns.scatterplot(x='artist_popularity', y='track_popularity', data=df)
plt.title('Corrélation : Popularité de l\'Artiste vs Popularité des Tracks')
plt.xlabel('Popularité de l\'Artiste')
plt.ylabel('Popularité des Tracks')
plt.grid(True)
plt.savefig('visuals/artist_vs_track_popularity.png')
plt.show()


'''QUESTION b : Y a-t-il une évolution des genres les plus écoutés entre 2019 et 2023 ?'''


# On extrait l'année de la date de sortie uniquement pour les dates entre 2019 et 2023
df['release_year'] = pd.to_datetime(df['release_date'], errors='coerce').dt.year  
df = df[(df['release_year'] >= 2019) & (df['release_year'] <= 2023)]  

# On remplace les genres manquants par 'Unknown' et on sépare les genres
df['artist_genres'] = df['artist_genres'].fillna('Unknown')
df = df.explode('artist_genres')  # Diviser les genres multiples dans une colonne en lignes distinctes

# On compte les genres par année
genre_counts = df.groupby(['release_year', 'artist_genres']).size().reset_index(name='count')

# On identifie les 10 genres les plus fréquents sur l'ensemble des années
top_genres = genre_counts.groupby('artist_genres')['count'].sum().nlargest(10).index
filtered_genres = genre_counts[genre_counts['artist_genres'].isin(top_genres)]  


# Visualisation de l'évolution des genres
plt.figure(figsize=(12, 8))
sns.lineplot(x='release_year', y='count', hue='artist_genres', data=filtered_genres)

plt.title('Évolution des genres les plus écoutés entre 2019 et 2023')
plt.xlabel('Année')
plt.ylabel("Nombre d'écoutes")

# On force l'affichage d'années entières sur l'axe des abscisses
plt.xticks(ticks=range(2019, 2024), labels=[str(year) for year in range(2019, 2024)])

plt.legend(title='Genres')
plt.grid(True)
plt.savefig('visuals/genres_evolution.png')
plt.show()


''' QUESTION 3 : Proposer des visualisations supplémentaires pouvant être intéressantes. '''

# Distribution des durées de tracks par année

plt.figure(figsize=(12, 6))
sns.boxplot(x='release_year', y='track_duration', data=df)
plt.title('Durée des Tracks par Année')
plt.xlabel('Année')
plt.ylabel('Durée (secondes)')

plt.grid(True)
plt.savefig('visuals/track_duration_by_year.png')
plt.show()





