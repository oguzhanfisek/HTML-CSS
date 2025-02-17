from flask import Flask, request, jsonify
import pyodbc

# Flask uygulamasını başlat
app = Flask(__name__)

# Veritabanı bağlantısı
connection = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=DESKTOP-OBLTQPD;"  # Burayı kendi sunucu adınız ile değiştirin
    "Database=KategoriYonetimSistemi;"  # Burayı kendi veritabanınız ile değiştirin
    "Trusted_Connection=yes;"  
)

cursor = connection.cursor()

# GET Metodu - Tüm kategorileri listelemek
@app.route("/categories", methods=["GET"])
def get_categories():
    cursor.execute("SELECT * FROM categories")  # 'categories' tablosundaki tüm verileri al
    categories = [
        {
            "id": row[0],
            "name": row[1],
            "description": row[2]
        }
        for row in cursor.fetchall()
    ]
    return jsonify(categories)

# POST Metodu - Yeni kategori eklemek
@app.route("/categories", methods=["POST"])
def add_category():
    if not request.is_json:  # Gönderilen verinin JSON formatında olup olmadığını kontrol et
        return jsonify({"message": "Content-Type must be 'application/json'"}), 415

    data = request.get_json()  # JSON verisini al

    # Veritabanına yeni kategori ekleme
    try:
        cursor.execute(
            """
            INSERT INTO categories (name, description)
            VALUES (?, ?)
            """,
            data["name"], data["description"]
        )
        connection.commit()  # Değişiklikleri kaydet
        return jsonify({"message": "Yeni kategori başarıyla eklendi!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# PUT Metodu - Kategori bilgilerini güncellemek
@app.route("/categories/<int:id>", methods=["PUT"])
def update_category(id):
    data = request.get_json()  # JSON verisini al

    # Kategoriyi güncelleme
    try:
        cursor.execute(
            """
            UPDATE categories
            SET name = ?, description = ?
            WHERE id = ?
            """,
            data["name"], data["description"], id
        )
        connection.commit()
        return jsonify({"message": "Kategori başarıyla güncellendi!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# DELETE Metodu - Kategori silmek
@app.route("/categories/<int:id>", methods=["DELETE"])
def delete_category(id):
    try:
        cursor.execute("DELETE FROM categories WHERE id = ?", id)  # Kategoriyi silme
        connection.commit()
        return jsonify({"message": "Kategori başarıyla silindi!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Uygulama başlatılıyor
if __name__ == "__main__":
    app.run(debug=True)
