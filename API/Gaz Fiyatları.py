import requests
import json

# API URL'si ve Anahtar
api_url = "https://api.collectapi.com"
headers = {
    'X-Api-Key': '4tLlQnT2lVWAB8aUqCZKg6:7BBWYRqADwzfcS5O4zyaLO'  # Burada 'YOUR_API_KEY' kısmını kendi API anahtarınızla değiştirin.
}

# Kullanıcıdan eyalet ismi alalım
state = input("Gaz fiyatlarını öğrenmek istediğiniz eyaletin kısaltmasını girin (örneğin, CA, NY): ")

# API'den gaz fiyatlarını çekmek
response = requests.get(f"{api_url}?state={state}", headers=headers)

# Eğer istek başarılıysa, veriyi işle
if response.status_code == 200:
    data = response.json()
    if data:
        print(f"{state} eyaletindeki gaz fiyatları:")
        for item in data:
            print(f"  {item['station_name']}: {item['price']} USD")
    else:
        print("Bu eyalette gaz fiyatları bulunamadı.")
else:
    print("API isteği başarısız oldu:", response.status_code)
