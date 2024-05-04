import sqlite3 as sql


class Manager:
    def __init__(self, idManager, nom, prenom, email, mot_de_passe):
        self.idManager = idManager
        self.nom = nom
        self.prenom = prenom
        self.email = email
        self.mot_de_passe = mot_de_passe

    def getManager(self):
        return {
            "id" : self.idManager,
            "nom"  : self.nom,
            "prenom": self.prenom,
            "email": self.email,
            "password" : self.mot_de_passe
        }

    def get_cars(self):
        conn = sql.connect("loc.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM cars")
        cars = cursor.fetchall()
        conn.close()
        return cars

    def add_car(self, car_details):
        conn = sql.connect("loc.db")
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO cars (marque, modele, immatriculation, categorie, prix, disponibilite) VALUES (?, ?, ?, ?, ?, ?)",
            (
                car_details["marque"],
                car_details["modele"],
                car_details["immatriculation"],
                car_details["categorie"],
                car_details["prix"],
                car_details["disponibilite"],
            ),
        )
        conn.commit()
        conn.close()

    def modify_car(self, car_id, car_details):
        conn = sql.connect("loc.db")
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE cars SET marque=?, modele=?, immatriculation=?, categorie=?, prix=?, disponibilite=? WHERE id=?",
            (
                car_details["marque"],
                car_details["modele"],
                car_details["immatriculation"],
                car_details["categorie"],
                car_details["prix"],
                car_details["disponibilite"],
                car_id,
            ),
        )
        conn.commit()
        conn.close()

    def delete_car(self, car_id):
        conn = sql.connect("loc.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM cars WHERE id=?", (car_id,))
        conn.commit()
        conn.close()

    def get_reservations(self):
        conn = sql.connect("loc.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM reservations")
        reservations = cursor.fetchall()
        conn.close()
        return reservations

    def accept_reservation(self, reservation_id):
        conn = sql.connect("loc.db")
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE reservations SET status='Accepted' WHERE id=?", (reservation_id,)
        )
        conn.commit()
        conn.close()

    def refuse_reservation(self, reservation_id):
        conn = sql.connect("loc.db")
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE reservations SET status='Refused' WHERE id=?", (reservation_id,)
        )
        conn.commit()
        conn.close()
