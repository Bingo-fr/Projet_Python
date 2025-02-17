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
        print("5. Ajouter un jeu au magasin : ")
        print("6. Ajouter un commentaire et une note : ")
        print("7. Retour")
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
                print(str(index +1) + "," + jeux["nom"])
            choicejeux = int(input("Veuillez donnez le chiffre : "))-1
            jeux = library[choicejeux]
            del library[choicejeux]
            print(f'le jeu : {jeux} a été supprimé')
            with open('jeux.json', 'w') as file:
                json.dump(library, file, indent=4)
        if (choice == "3"):
            with open('jeux.json', 'r') as file:
                library=json.load(file)
                for index, jeux in enumerate(library):
                    print(str(index +1) + "." + jeux["nom"])
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

            print("Votre jeu a bien été ajouté ! ")
            with open('ventes.json', 'r') as file:
                library=json.load(file)
            library.append(jeux)
            with open('ventes.json', 'w') as file:
                json.dump(library, file, indent=4)
        if (choice == "6"):
            with open('bibliotheque_l.json', 'r', encoding='utf-8') as file:
                library = json.load(file)

            for jeux in library:
                print(jeux["nom"])

            jeu = input("Entrez le nom du jeu : ")

            while True:
                try:
                    note = int(input(f"Attribuez une note à {jeu} (entre 1 et 5) : "))
                    if 1 <= note <= 5:
                        break
                    else:
                        print("Erreur : Veuillez entrer un nombre entre 1 et 5.")
                except ValueError:
                    print("Erreur : Veuillez entrer un nombre valide.")

            commentaire = input("Laissez un commentaire sur ce jeu : ")

            avis = {
                "jeu": jeu,
                "note": note,
                "commentaire": commentaire
            }

            try:
                with open("avis_note.json", "a", encoding="utf-8") as file:
                    json.dump(avis, file, ensure_ascii=False)
                    file.write("\n") 
            except FileNotFoundError:

                with open("avis_note.json", "w", encoding="utf-8") as file:
                    json.dump([avis], file, ensure_ascii=False, indent=4)

            print("\nMerci ! Votre avis a été enregistré avec succès. 🎮")
        
        
        if (choice == "7"):
            pass

    if (choice == "2"):
        print("1. Afficher la liste des jeux en vente : ")
        print("2. Acheter un jeu : ")
        print("3. Retour ")
        choice = input()
        if (choice == "1"):
            with open('ventes.json', 'r', encoding="utf-8") as file:
                library=json.load(file)
                for index, jeux in enumerate(library):
                    print(f"{index+1} Nom : {jeux['nom']}, Tag : {jeux['tag']}, Image : {jeux['image']}, detail : {jeux['detail']}, Prix {jeux['prix']}")
        if (choice == "2"):
            with open('ventes.json', 'r', encoding="utf-8") as file:
                library = json.load(file)

            for index, jeux in enumerate(library):
                print(str(index + 1) + "," + jeux["nom"])

            choicejeux = int(input("Entrez le chiffre correspondant au jeu que vous voulez acquérir : ")) - 1
            jeu = library[choicejeux]

            biblio = [] 
            biblio.append(jeu)

            try:
                with open('bibliotheque_l.json', 'r', encoding='utf-8') as file:
                    bibliotheque = json.load(file)
            except FileNotFoundError:
                bibliotheque = [] 

            bibliotheque.append(jeu)

            with open('bibliotheque_l.json', 'w', encoding='utf-8') as file:
                json.dump(bibliotheque, file, indent=4)

            print(f'Le jeu : {jeu["nom"]} a été ajouté à votre bibliothèque.')

        if (choice == "3"):
            pass

        choice=0

    if (choice == "3"):
        break


