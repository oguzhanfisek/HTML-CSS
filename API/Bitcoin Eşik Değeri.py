import requests

api_url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"

lower_threshold = 90000 
upper_threshold = 110000  

response = requests.get(api_url)

if response.status_code == 200:
    data = response.json()
    bitcoin_price = data['bitcoin']['usd']  
    print(f"Anlık Bitcoin Fiyatı: ${bitcoin_price}")
    
    if bitcoin_price < lower_threshold:
        print("Bitcoin fiyatı düşük!")
    elif bitcoin_price > upper_threshold:   
        print("Bitcoin fiyatı yüksek!")
    else:
        print("Bitcoin fiyatı normal seviyelerde.")
else:
    print("API isteği başarısız oldu:", response.status_code)
