class Voiture:
    def __init__(
        self,
        id_voiture,
        marque,
        modele,
        immatriculation,
        categorie,
        prix,
        disponibilite=True,
        image_url=None,
    ):
        self.id = id_voiture 
        self.marque = marque
        self.modele = modele
        self.immatriculation = immatriculation
        self.categorie = categorie
        self.prix = prix
        self.disponibilite = disponibilite
        self.image_url = image_url

    def get_details(self):
        return {
            "id_voiture": self.id, 
            "marque": self.marque,
            "modele": self.modele,
            "immatriculation": self.immatriculation,
            "categorie": self.categorie,
            "prix": self.prix,
            "disponibilite": "Disponible" if self.disponibilite else "Non disponible",
            "image_url": self.image_url,
        }
