# Projet d'Analyse des Tendances d'Achat des Clients

## Objectif
Un grand compte de vente de vélos souhaite analyser les données de ses clients pour comprendre leurs tendances d'achat. La segmentation des clients est une méthode d'analyse qui permet de regrouper les clients en fonction de leurs caractéristiques communes, telles que leurs besoins, leurs intérêts ou leur comportement d'achat.

Dans le cas de ce client, la segmentation des clients pourrait être effectuée en fonction des critères suivants :
- Nombre d'achats d'un modèle de vélos par sexe
- Calcul du nombre d'achats des modèles par Etat
- Histogramme du nombre d'achats d'un modèle de vélos par Etat
- Top 1 du modèle le plus vendus dans chaque Etat

## Données
Les sources de données sont des fichiers plats de type CSV :
- `bikes.csv` : Informations détaillées sur différents modèles de vélos, y compris leurs spécifications, prix, date de lancement et autres caractéristiques pertinentes.
- `bikeshops.csv` : Informations relatives aux commandes des distributeurs, y compris les quantités commandées, les dates de commande, les remises éventuellement appliquées et les détails du distributeur.
- `order.csv` : Historique complet des commandes passées, comprenant des informations telles que l'identifiant du client, l'identifiant du produit, la date de commande, la quantité et le montant total.

## Étapes du Projet
Ce projet se déroule en plusieurs étapes, comme décrit ci-dessous :

1. Collecte des données
-  Le client nous founit les données (fichiers CSV)

2. Nettoyer les Données
- Les données sont nettoyées pour supprimer les doublons, corriger les valeurs aberrantes et traiter les valeurs manquantes.

3. Auditer la Qualité des Données
- Une analyse préliminaire est effectuée pour évaluer l'exactitude, la complétude, la cohérence et la validité des données fournies.

4. Traitement des Données
- Apache Spark MLib est utilisé comme ETL pour traiter les données afin de réaliser la classification, la régression, la clustering et la prédiction.

5. Analyser les Données
- Les données sont analysées pour comprendre les tendances d'achat des clients avec PowerBI

## Contributeurs
Florence N KPEDJI

Rachda MOHAMED RACHIDY

Valentin GUERARD
