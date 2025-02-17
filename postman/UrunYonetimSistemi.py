from flask import Flask, request, jsonify
import pyodbc

# Flask uygulamasını başlat
app = Flask(__name__)

# Veritabanı bağlantısı
connection = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=DESKTOP-OBLTQPD;"  
    "Database=UrunYonetimSistemi;"  # Veritabanı adı güncellendi
    "Trusted_Connection=yes;"  
)

cursor = connection.cursor()

# GET Metodu - Tüm ürünleri listelemek
@app.route("/urunyonetimsistemi", methods=["GET"])
def get_Products():
    cursor.execute("SELECT * FROM Table1")  # 'Table1' tablosundaki tüm verileri al
    products = [
        {
            "id": row[0],
            "name": row[1],
            "description": row[2],
            "price": row[3],
            "stock_quantity": row[4],
        }
        for row in cursor.fetchall()
    ]
    return jsonify(products)

# POST Metodu - Yeni ürün eklemek
@app.route("/urunyonetimsistemi", methods=["POST"])
def add_Product():
    if not request.is_json:  # Gönderilen verinin JSON formatında olup olmadığını kontrol et
        return jsonify({"message": "Content-Type must be 'application/json'"}), 415

    data = request.get_json()  # JSON verisini al

    # Veritabanına yeni ürün ekleme
    try:
        cursor.execute(
            """
            INSERT INTO Table1 (name, description, price, stock_quantity)
            VALUES (?, ?, ?, ?)
            """,
            data["name"], data["description"], data["price"], data["stock_quantity"]
        )
        connection.commit()  # Değişiklikleri kaydet
        return jsonify({"message": "Yeni ürün başarıyla eklendi!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# PUT Metodu - Ürün bilgilerini güncellemek
@app.route("/urunyonetimsistemi/<int:id>", methods=["PUT"])
def update_Product(id):
    data = request.get_json()  # JSON verisini al

    # Ürünü güncelleme
    try:
        cursor.execute(
            """
            UPDATE Table1
            SET name = ?, description = ?, price = ?, stock_quantity = ?
            WHERE id = ?
            """,
            data["name"], data["description"], data["price"], data["stock_quantity"], id
        )
        connection.commit()
        return jsonify({"message": "Ürün başarıyla güncellendi!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# DELETE Metodu - Ürün silmek
@app.route("/urunyonetimsistemi/<int:id>", methods=["DELETE"])
def delete_Product(id):
    try:
        cursor.execute("DELETE FROM Table1 WHERE id = ?", id)  # Ürünü silme
        connection.commit()
        return jsonify({"message": "Ürün başarıyla silindi!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Uygulama başlatılıyor
if __name__ == "__main__":
    app.run(debug=True)
