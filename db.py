import sqlite3 as sql

connexion = sql.connect("loc.db")
cursor = connexion.cursor()

# cursor.execute("""CREATE TABLE client (
#                 id_client INTEGER PRIMARY KEY AUTOINCREMENT,
#                 nom TEXT NOT NULL,
#                 prenom TEXT NOT NULL,
#                 email TEXT NOT NULL,
#                 telephone TEXT NOT NULL)""")

# cursor.execute(
#     """CREATE TABLE voiture (
#                 id_voiture INTEGER PRIMARY KEY AUTOINCREMENT,
#                 marque TEXT NOT NULL,
#                 modele TEXT NOT NULL,
#                 immatriculation TEXT NOT NULL,
#                 categorie TEXT NOT NULL,
#                 prix TEXT NOT NULL,
#                 disponibilite TEXT NOT NULL,
#                 image_url TEXT)"""
# )

# cursor.execute("""CREATE TABLE manager (
#                idManger  INTEGER PRIMARY KEY AUTOINCREMENT,
#                nom TEXT NOT NULL,
#                prenom TEXT NOT NULL,
#                email TEXT NOT NULL,
#                mot_de_passe TEXT  NOT NULL) """)
# cursor.execute(
#     """CREATE TABLE IF NOT EXISTS reservation (
#                 id_reservation INTEGER PRIMARY KEY AUTOINCREMENT,
#                 id_client INTEGER,
#                 id_voiture INTEGER,
#                 status TEXT NOT NULL,
#                 FOREIGN KEY (id_client) REFERENCES client (id_client),
#                 FOREIGN KEY (id_voiture) REFERENCES voiture (id_voiture))"""
# )

# cars_data = [
#     (
#         "Toyota",
#         "Corolla",
#         "1234 AB 56",
#         "Compacte",
#         "25000",
#         "Disponible",
#         "/static/images/AttitudeBlack.png",
#     ),
#     (
#         "Honda",
#         "Civic",
#         "5678 CD 90",
#         "Compacte",
#         "27000",
#         "Disponible",
#         "/static/images/honda_cevic.jpg",
#     ),
#     (
#         "Ford",
#         "Focus",
#         "2468 EF 12",
#         "Compacte",
#         "23000",
#         "Non disponible",
#         "/static/images/2018-ford-focus-s_1.png",
#     ),
#     (
#         "BMW",
#         "X5",
#         "1357 GH 34",
#         "SUV",
#         "50000",
#         "Disponible",
#         "/static/images/bmwx5.jpg",
#     ),
#     (
#         "Mercedes",
#         "C-Class",
#         "9876 IJ 78",
#         "Berline",
#         "40000",
#         "Non disponible",
#         "/static/images/cclass.png",
#     ),
# ]

# cursor.executemany(
#     "INSERT INTO voiture (marque, modele, immatriculation, categorie, prix, disponibilite, image_url) VALUES (?, ?, ?, ?, ?, ?, ?)",
#     cars_data,
# )

# connexion.commit()
# connexion.close()
# users = [
#     ("John", "Doe", "john@example.com", "password123"),
#     ("Jane", "Smith", "jane@example.com", "letmein"),
#     ("Alice", "Jones", "alice@example.com", "p@ssw0rd"),
#     ("Bob", "Brown", "bob@example.com", "secret"),
# ]

# cursor.executemany(
#     "INSERT INTO manager (nom, prenom, email, mot_de_passe) VALUES (?, ?, ?, ?)", users
# )
# users = [
#     ("John", "Doe", "john@example.com", "1234567890"),
#     ("Jane", "Smith", "jane@example.com", "9876543210"),
#     ("Alice", "Jones", "alice@example.com", "5551234567"),
#     ("Bob", "Brown", "bob@example.com", "7890123456"),
#     ("Emma", "Johnson", "emma@example.com", "2345678901"),
#     ("Michael", "Williams", "michael@example.com", "6789012345"),
#     ("Sophia", "Brown", "sophia@example.com", "3456789012"),
#     ("Matthew", "Davis", "matthew@example.com", "8901234567"),
#     ("Olivia", "Miller", "olivia@example.com", "4567890123"),
#     ("James", "Wilson", "james@example.com", "9012345678"),
# ]

# # Insert the users into the client table
# cursor.executemany(
#     "INSERT INTO client (nom, prenom, email, telephone) VALUES (?, ?, ?, ?)", users
# )

# cursor.execute(
#     """
# CREATE TABLE IF NOT EXISTS administrateur (
#     id_admin INTEGER PRIMARY KEY AUTOINCREMENT,
#     nom TEXT NOT NULL,
#     prenom TEXT NOT NULL,
#     email TEXT NOT NULL UNIQUE,
#     mot_de_passe TEXT NOT NULL
# )
# """
# )
# admin_data = ("John", "Doe", "john.doe@example.com", "password123")

# insert_query = """
# INSERT INTO administrateur (nom, prenom, email, mot_de_passe)
# VALUES (?, ?, ?, ?)
# """

# cursor.execute(insert_query, admin_data)
# newManager = (
#     "Bouih", "Abde", "bouihabdessamad5@gmail.com", "abde"
# )
# insert_query = """
# INSERT INTO manager (nom, prenom, email, mot_de_passe)
# VALUES (?, ?, ?, ?)
# """
# cursor.execute(insert_query, newManager)

# connexion.commit()
# connexion.close()

# print('secus')

# cursor.execute("""DROP TABLE reservation""")
cursor.execute(
    """
    CREATE TABLE reservation (
        reservation_id INTEGER PRIMARY KEY AUTOINCREMENT,
        car_id INTEGER,
        nom TEXT,
        prenom TEXT,
        email TEXT,
        telephone TEXT,
        status TEXT DEFAULT 'Pending',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(car_id) REFERENCES voiture(id_voiture)
    )
"""
)

print("Success")
