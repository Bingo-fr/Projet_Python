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
        print("5. ")
        print("6. Retour")
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
            with open('jeux.json', 'r') as file:
                library=json.load(file)
            library.append(jeux)
            with open('jeux.json', 'w') as file:
                json.dump(library, file, indent=4)
        if (choice == "2"):
            with open('jeux.json', 'r') as file:
                library=json.load(file)
            for index, jeux in enumerate(library):
                print(str(index) + "," + jeux["nom"])
            choicejeux = int(input("Veuillez donnez le chiffre : "))
            jeux = library[choicejeux]
            del library[choicejeux]
            print(f'le jeu : {jeux} à été supprimé')
            with open('jeux.json', 'w') as file:
                json.dump(library, file, indent=4)
        if (choice == "3"):
            with open('jeux.json', 'r') as file:
                library=json.load(file)
                for index, jeux in enumerate(library):
                    print(str(index +1) + "," + jeux["nom"])
        if (choice == "4"):
            with open('jeux.json', 'r', encoding="utf-8") as file:
                library = json.load(file)
                for index, jeux in enumerate(library):
                    print(str(index +1) + "," + jeux["nom"])
                nom = int(input("Entrez un chiffre : "))
                print(library[nom -1]["detail"])
        if (choice == "5"):
            nom = input("Nom :")
            tag = input("Tag :")
            image = input("Image :")
            detail = input("detail : ")
            prix = input("prix : ")

            jeux={
                "nom": nom,
                "tag": tag,
                "image":image,
                "detail":detail,
                "prix":prix,
            }
            with open('jeux.json', 'r') as file:
                library=json.load(file)
            library.append(jeux)
            with open('jeux.json', 'w') as file:
                json.dump(library, file, indent=4)

        if (choice == "6"):
            pass

    if (choice == "2"):
        print("1. Afficher la liste des jeux en vente : ")
        print("2. Supprimer un jeu : ")
        print("3. Acheter un jeu : ")
        print("4. Quitter ")
        if (choice == "1"):