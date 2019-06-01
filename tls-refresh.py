import requests
import ssl

pagarme_request = requests.get("https://tls12.pagar.me");

if pagarme_request.status_code == 200:
	print(pagarme_request.text)
else:
	print("Sua versão SSL é: " + ssl.OPENSSL_VERSION)
	print("Sua versão deve ser superior à 1.0.1c")