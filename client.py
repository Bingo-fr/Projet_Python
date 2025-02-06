import requests

base_url = "http://172.25.1.24:5007"

message = input("Entrez un msg : ")
data = {"message": message }

response = requests.post(base_url + "/message", json=data)
print(response.status_code)

if response.status_code == 200:
    print("Réponse du serveur : ", response.json()["response"])
else:
    print("Erreur : ", response.json())
