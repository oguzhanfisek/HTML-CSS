import requests

api_url = "https://v2.jokeapi.dev/joke/Any"

response = requests.get(api_url)

if response.status_code == 200:
    joke_data = response.json()
    
    if joke_data["type"] == "single":
        print("Şaka:", joke_data["joke"])
    elif joke_data["type"] == "twopart":
        print("Şaka: ")
        print("Soru:", joke_data["setup"])
        print("Cevap:", joke_data["delivery"])
else:
    print("API isteği başarısız oldu:", response.status_code)
