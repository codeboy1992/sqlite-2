import sqlite3
import csv

# Connexion à la base de données
connexion = sqlite3.connect('simplon-sqlite-2.db')
curseur = connexion.cursor()

# Création de la table Clients (si elle n'existe pas déjà)
curseur.execute('''
CREATE TABLE IF NOT EXISTS Clients (
    client_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT NOT NULL,
    prenom TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    telephone TEXT,
    date_naissance DATE,
    adresse TEXT,
    consentement_marketing BOOLEAN NOT NULL
);
''')

# Création de la table Commandes
curseur.execute('''
CREATE TABLE IF NOT EXISTS Commandes (
    commande_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER,
    produit TEXT,
    montant REAL,
    date_commande TEXT,
    FOREIGN KEY (client_id) REFERENCES Clients(client_id)
);
''')

# Importer les données du fichier CSV Clients
with open('C:/Users/yohan/sqlite-2/data/jeu-de-donnees-clients-66fed38c68779376654152.csv', newline='', encoding='utf-8') as fichier_csv:
    lecteur_csv = csv.reader(fichier_csv)
    next(lecteur_csv)  # Sauter l'en-tête
    for ligne in lecteur_csv:
        # Vérifier si l'email existe déjà
        curseur.execute('SELECT * FROM Clients WHERE email = ?', (ligne[3],))
        result = curseur.fetchone()

        # Si l'email n'existe pas, insérer
        if result is None:
            curseur.execute('INSERT INTO Clients (nom, prenom, email, consentement_marketing) VALUES (?, ?, ?, ?)', ligne[1:5])
        else:
            print(f"L'email {ligne[3]} existe déjà.")

# Importer les données du fichier CSV Commandes
with open('C:/Users/yohan/sqlite-2/data/jeu-de-donnees-commandes-66fe65226fdb5678959707.csv', newline='', encoding='utf-8') as fichier_csv:
    lecteur_csv = csv.reader(fichier_csv)
    next(lecteur_csv)  # Sauter l'en-tête
    for ligne in lecteur_csv:
        curseur.execute('INSERT INTO Commandes (client_id, produit, montant, date_commande) VALUES (?, ?, ?, ?)', ligne)

# Sauvegarder les modifications dans la base de données
connexion.commit()

# Vérification après insertion
curseur.execute("SELECT * FROM Clients")
clients = curseur.fetchall()
print("Clients insérés :")
for client in clients:
    print(client)

curseur.execute("SELECT * FROM Commandes")
commandes = curseur.fetchall()
print("Commandes insérées :")
for commande in commandes:
    print(commande)

# Fermer la connexion
connexion.close()
