import json

class Jeux:
    def __init__(self, nom, tag, image, detail):
        self.nom = nom
        self.tag = tag
        self.image = image
        self.detail = detail

class Notation:
    def __init__(self, commentaire, note):
        self.commentaire = commentaire
        self.note = note

class Biblibiothèque:
    def __init__(self, nom, nbr_sauvegarde, isfavorite):
        self.nom = nom
        self.nbr_sauvegarde = nbr_sauvegarde
        self.isfavorite = isfavorite


while (True):
    print("1.Créer un commentaire et laisser une note")
    print("2.Lister un commentaire sur un jeu")
    print("3.Afficher la note d'un commentaire")
    print("4.Répondre au commentaire")
    choice = input ("Votre choix :")
    if (choice == "1"):
        with open('jeux.json', 'r') as file:
            library=json.load(file)
        for index, jeux in enumerate(library):
                print(str(index) + "," + jeux["nom"])
        choicejeux = int(input("Selectionner un jeu : "))
        with open("notations.json", "r", encoding="utf-8") as f:
            notations = json.load(f)
            commentaire = input("Votre commentaire :")
            note = input("note :")
        Note = {
                "commentaire": commentaire,
                "note": note,
        }
        with open('notation.json', 'w') as file:
                json.dump(library, file, indent=4)