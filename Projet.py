import json

class Jeux:
    def __init__(self, nom, tag, image, detail):
        self.nom = nom
        self.tag = tag
        self.image = image
        self.detail = detail


class Biblibiothèque:
    def __init__(self, nom, nbr_sauvegarde, isfavorite):
        self.nom = nom
        self.nbr_sauvegarde = nbr_sauvegarde
        self.isfavorite = isfavorite
while(True):
    print("1.Bibliothèque locale")
    print("2.Magasin")
    print("3.Quitter")
    choice = input()
    if (choice == "1"):
        print("1. Créer un jeu avec un nom, un tag, une image, détail : ")
        print("2. Supprimer un jeu : ")
        print("3. Afficher la liste de tous les jeux : ")
        print("4. Afficher le détail d'un jeu : ")
        choice = input()
        if (choice == "1"):
            nom = input("Nom :")
            tag = input("Tag :")
            image = input("Image :")
            detail = input("detail : ")

            jeux={
                "nom": nom,
                "tag": tag,
                "image":image,
                "detail":detail,
            }
            with open('magasin.json', 'r') as file:
                library=json.load(file)
            library.append(jeux)
            with open('magasin.json', 'w') as file:
                json.dump(library, file, indent=4)
        if (choice == "2"):
            with open('magasin.json', 'r') as file:
                library=json.load(file)
            for index, jeux in enumerate(library):
                print(str(index) + "," + jeux["nom"])
            choicejeux = int(input("Veuillez donnez un chiffre : "))
            jeux = library[choicejeux]
            del library[choicejeux]
            print(f'le jeu : {nom} à été supprimé')


