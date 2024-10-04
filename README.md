# Projet de Gestion de Base de Données avec SQLite

## Description

Ce projet consiste en la création et la gestion d'une base de données SQLite pour gérer des **Clients** et leurs **Commandes** dans le cadre d'une campagne marketing. L'application permet d'importer des données depuis des fichiers CSV, de les insérer dans une base de données SQLite, et d'exécuter des requêtes SQL pour extraire des informations clés.

### Fonctionnalités
- **Création des tables Clients et Commandes** avec les contraintes définies dans le Modèle Physique des Données (MPD).
- **Importation de données** depuis des fichiers CSV.
- **Exécution de requêtes SQL** pour extraire des informations telles que les clients ayant consenti à recevoir des communications marketing ou les commandes d'un client spécifique.
  
## Modèle de données

Le modèle de données est composé de deux tables :

### Table `Clients`
- `client_id` (INTEGER, clé primaire)
- `nom` (TEXT, obligatoire)
- `prenom` (TEXT, obligatoire)
- `email` (TEXT, unique, obligatoire)
- `telephone` (TEXT)
- `date_naissance` (DATE)
- `adresse` (TEXT)
- `consentement_marketing` (BOOLEAN, obligatoire)

### Table `Commandes`
- `commande_id` (INTEGER, clé primaire)
- `client_id` (INTEGER, clé étrangère, référence à `Clients`)
- `produit` (TEXT, obligatoire)
- `montant` (REAL, obligatoire)
- `date_commande` (TEXT, obligatoire)

## Installation

### Prérequis
- **Python 3.10+**
- **SQLite3**

### Étapes d'installation

1. Cloner ce dépôt :
   ```bash
   git clone https://github.com/tonnomdeprojet/sqlite-project.git
