import requests

api_url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"

response = requests.get(api_url)

if response.status_code == 200:
    data = response.json()
    bitcoin_price = data['bitcoin']['usd'] 
    print(f"Anlık Bitcoin Fiyatı: ${bitcoin_price}")
else:
    print("API isteği başarısız oldu:", response.status_code)
