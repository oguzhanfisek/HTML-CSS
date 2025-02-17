from flask import Flask, request, jsonify
import pyodbc

app = Flask(__name__)

connection = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=DESKTOP-OBLTQPD;"  
    "Database=KullanıcıYonetimSistemi;"  
    "Trusted_Connection=yes;"  
)

cursor = connection.cursor()
print("SQL bağlantısı başarılı", cursor)

# GET Metodu - Tüm kullanıcıları listelemek
@app.route("/kullaniciyonetimsistemi", methods=["GET"])
def get_Users():
    cursor.execute("SELECT * FROM Users")  
    Users = [
        {
            "id": row[0],
            "username": row[1],
            "email": row[2],
            "password": row[3],
        }
        for row in cursor.fetchall()
    ]
    return jsonify(Users)

# POST Metodu - Yeni kullanıcı eklemek
@app.route("/kullaniciyonetimsistemi", methods=["POST"])
def add_User():
    # Gelen başlıkları ve veriyi kontrol et
    print(f"Request Headers: {request.headers}")  # Başlıkları yazdır
    print(f"Request Data: {request.data}")  # Gelen veriyi yazdır
    
    # Eğer içerik JSON değilse hata döndür
    if not request.is_json:
        return jsonify({"message": "Content-Type must be 'application/json'"}), 415

    # JSON verisini al
    data = request.get_json()
    
    # Veritabanına ekle
    cursor.execute(
        """
        INSERT INTO Users (id, username, email, password)
        VALUES (?, ?, ?, ?)
        """,
        data["id"], data["username"], data["email"], data["password"]
    )
    connection.commit()
    
    return jsonify({"message": "Yeni kullanıcı başarıyla eklendi!"}), 201

if __name__ == "__main__":
    app.run(debug=True)

# PUT Metodu - Kullanıcı bilgilerini güncellemek
@app.route("/kullaniciyonetimsistemi/<int:id>", methods=["PUT"])
def update_Users(id):
    data = request.get_json()

    cursor.execute(
        """
        UPDATE Users
        SET username = ?, email = ?, password = ?
        WHERE id = ?
        """,
        data["username"], data["email"], data["password"], id
    )
    connection.commit()

    return jsonify({"message": "Kullanıcı başarıyla güncellendi!"})

# DELETE Metodu - Kullanıcı silmek
@app.route("/kullaniciyonetimsistemi/<int:id>", methods=["DELETE"])
def delete_Users(id):
    cursor.execute("DELETE FROM Users WHERE id = ?", id)  
    connection.commit()

    return jsonify({"message": "Kullanıcı başarıyla silindi!"})

# Uygulama başlatılıyor
if __name__ == "__main__":
    app.run(debug=True)
