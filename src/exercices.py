import sqlite3

# Connexion à la base de données SQLite
connexion = sqlite3.connect('simplon-sqlite-2.db')
curseur = connexion.cursor()

# Exerecice 1 :Les clients ayant consenti à recevoir des communications marketing.
curseur.execute("SELECT * FROM Clients WHERE consentement_marketing = 1")
clients_consentants = curseur.fetchall()
print("Clients ayant consenti à recevoir des communications marketing:")
print()

for client in clients_consentants:
    print(client)


# Exercice 2 : Les commandes d'un client spécifique.
curseur.execute("SELECT * FROM Commandes WHERE client_id = 5")
commandes_client = curseur.fetchall()
print("\nCommandes du client avec l'ID 5:")
print()
for commande in commandes_client:
    print(commande)


# Exercice 3 : Le montant total des commandes du client avec ID n° 61 .
curseur.execute("SELECT SUM(montant) FROM Commandes WHERE client_id = 61")
montant_total = curseur.fetchone()[0]
print(f"\nMontant total des commandes du client avec ID 61: {montant_total} euros")
print()

# Exercice 4 : Les clients ayant passé des commandes de plus de 100 euros.
curseur.execute('''
    SELECT DISTINCT Clients.*
    FROM Clients
    JOIN Commandes ON Clients.client_id = Commandes.client_id
    WHERE Commandes.montant > 100
''')
clients_100 = curseur.fetchall()
print("\nClients ayant passé des commandes de plus de 100 euros:")
print()
for client in clients_100:
    print(client)


# Exercice 5 : Les clients ayant passé des commandes après le 01/01/2023.
curseur.execute('''
    SELECT DISTINCT Clients.*
    FROM Clients
    JOIN Commandes ON Clients.client_id = Commandes.client_id
    WHERE Commandes.date_commande > '2023-01-01'
''')
clients_apres_2023 = curseur.fetchall()
print("\nClients ayant passé des commandes après le 01/01/2023:")
print()
for client in clients_apres_2023:
    print(client)


# Fermer la connexion à la base de données
connexion.close()
