import sqlite3 as sql
from voiture import Voiture

class Client:
    def __init__(self, id_client, nom, prenom, email, telephone):
        self.id_client = id_client
        self.nom = nom
        self.prenom = prenom
        self.email = email
        self.telephone = telephone
        self.reservations = []
    def getClients(self):
        return {
            "id Client" : self.id_client,
            "nom" : self.nom,
            "prenom" : self.prenom,
            "email": self.email,
            "tel": self.telephone
        }
    def get_reservations(self):
        conn = sql.connect("loc.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM reservations WHERE client_id=?", (self.id,))
        reservations = cursor.fetchall()
        conn.close()
        return reservations

    def reserver_voiture(self, voiture_id):
        conn = sql.connect("loc.db")
        cursor = conn.cursor()
        cursor.execute(
            "SELECT disponibilite FROM voiture WHERE id_voiture=?", (voiture_id,)
        )
        disponibilite = cursor.fetchone()
        if disponibilite and disponibilite[0] == "Disponible":
            cursor.execute(
                "UPDATE voiture SET disponibilite='Non disponible' WHERE id_voiture=?",
                (voiture_id,),
            )
            cursor.execute(
                "INSERT INTO reservations (client_id, voiture_id) VALUES (?, ?)",
                (self.id, voiture_id),
            )
            conn.commit()
            print("La voiture a été réservée avec succès.")
        else:
            print("La voiture est déjà réservée ou n'est pas disponible.")
        conn.close()

    def annuler_reservation(self, reservation_id):
        conn = sql.connect("loc.db")
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM reservations WHERE id_reservation=? AND client_id=?",
            (reservation_id, self.id),
        )
        reservation = cursor.fetchone()
        if reservation:
            cursor.execute(
                "UPDATE voiture SET disponibilite='Disponible' WHERE id_voiture=?",
                (reservation[2],),
            )
            cursor.execute(
                "DELETE FROM reservations WHERE id_reservation=?", (reservation_id,)
            )
            conn.commit()
            print("La réservation de la voiture a été annulée.")
        else:
            print("Aucune réservation trouvée pour ce client avec l'identifiant donné.")
        conn.close()
# # Instantiate a Voiture object
# car = Voiture(1, "Toyota", "Corolla", "ABC123", "Sedan", 20000)

# # Test the get_details method
# print("Car Details : ")
# print(car.get_details())

# # Test the reserve method
# print("\nReserving the car : ")
# car.reserve()

# # Test the reserve method again (to simulate attempting to reserve an already reserved car)
# print("\nAttempting to reserve the car again:")
# car.reserve()

# # Test the annuler_reservation method
# print("\nCancelling the reservation:")
# car.annuler_reservation()

# # Test the annuler_reservation method again (to simulate attempting to cancel a reservation on an available car)
# print("\nAttempting to cancel the reservation again:")
# car.annuler_reservation()
