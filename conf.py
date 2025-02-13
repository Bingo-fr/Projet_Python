import json

class Jeux:
    def __init__(self, nom, tag, image, detail):
        self.nom = nom
        self.tag = tag
        self.image = image
        self.detail = detail
class magasin_local:
        def __init__(self, liste_de_jeu, ):
             pass
    


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

