import requests
import json

url = "http://node120108-env-5963925.jcloud-ver-jpc.ik-server.com:12081/play"
token = "99017e04a19ff7846fbe440406b1e564"  # Remplacez cela par votre token

low = 0
high = 4000000000

with open("result.txt", "w") as result_file:
    for _ in range(42):  # Limitez le nombre de requêtes à 10
        mid = (low + high) // 2
        payload = {'token': token, 'answer': mid}
        response = requests.get(url, params=payload)

        try:
            json_data = response.json()
            status = json_data.get("status")

            result_file.write(f"Réponse JSON : {json_data}\n")

            if status == '>':
                low = mid + 1
            elif status == '<':
                high = mid - 1
            elif status == '=':
                result_file.write(f"Nombre trouvé : {mid}\n")
                break
            else:
                result_file.write("Réponse inattendue du serveur.\n")
                break

            token = json_data.get('token', token)

            if low > high:
                result_file.write("Nombre non trouvé dans la limite de requêtes.\n")
                break

        except json.JSONDecodeError as e:
            result_file.write(f"Impossible de décoder la réponse JSON. Erreur : {e}\n")
            result_file.write(f"Contenu brut de la réponse : {response.text}\n")
            break
