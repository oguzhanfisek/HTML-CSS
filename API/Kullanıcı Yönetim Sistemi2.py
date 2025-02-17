import requests

base_url = "https://jsonplaceholder.typicode.com/users"

def list_users():
    response = requests.get(base_url)
    if response.status_code == 200:
        users = response.json()
        for user in users:
            print(f"ID: {user['id']}, Name: {user['name']}, Email: {user['email']}")
    else:
        print("Kullanıcıları listeleme başarısız oldu.")

def add_user(name, username, email):
    new_user = {
        "name": name,
        "username": username,
        "email": email
    }
    response = requests.post(base_url, json=new_user)
    if response.status_code == 201:
        print(f"Yeni kullanıcı eklendi: {response.json()}")
    else:
        print("Kullanıcı eklenemedi.")

def update_user(user_id, name=None, username=None, email=None):
    user_data = {}
    if name:
        user_data["name"] = name
    if username:
        user_data["username"] = username
    if email:
        user_data["email"] = email
    
    response = requests.put(f"{base_url}/{user_id}", json=user_data)
    if response.status_code == 200:
        print(f"Kullanıcı güncellendi: {response.json()}")
    else:
        print("Kullanıcı güncellenemedi.")

def delete_user(user_id):
    response = requests.delete(f"{base_url}/{user_id}")
    if response.status_code == 200:
        print(f"Kullanıcı {user_id} silindi.")
    else:
        print(f"Kullanıcı {user_id} silinemedi.")

def main():
    while True:
        print("\nKullanıcı Yönetim Sistemi")
        print("1. Kullanıcıları Listele")
        print("2. Yeni Kullanıcı Ekle")
        print("3. Kullanıcı Güncelle")
        print("4. Kullanıcı Sil")
        print("5. Çıkış")
        
        choice = input("Bir seçenek girin (1/2/3/4/5): ")
        
        if choice == "1":
            list_users()
        elif choice == "2":
            name = input("Kullanıcı adı: ")
            username = input("Kullanıcı adı (kullanıcı adı): ")
            email = input("Kullanıcı e-posta: ")
            add_user(name, username, email)
        elif choice == "3":
            user_id = int(input("Güncellemek istediğiniz kullanıcının ID'sini girin: "))
            name = input("Yeni ad (bırakmak için boş bırakın): ")
            username = input("Yeni kullanıcı adı (bırakmak için boş bırakın): ")
            email = input("Yeni e-posta (bırakmak için boş bırakın): ")
            update_user(user_id, name, username, email)
        elif choice == "4":
            user_id = int(input("Silmek istediğiniz kullanıcının ID'sini girin: "))
            delete_user(user_id)
        elif choice == "5":
            print("Çıkılıyor...")
            break
        else:
            print("Geçersiz seçenek. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()
