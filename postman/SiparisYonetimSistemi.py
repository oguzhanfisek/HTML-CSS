from flask import Flask, request, jsonify
import pyodbc

# Flask uygulamasını başlat
app = Flask(__name__)

# Veritabanı bağlantısı
connection = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=DESKTOP-OBLTQPD;"  
    "Database=SiparisYonetimSistemi;"  
    "Trusted_Connection=yes;"  
)

cursor = connection.cursor()

# GET Metodu - Tüm siparişleri listelemek
@app.route("/siparisyonetimsistemi", methods=["GET"])
def get_Orders():
    cursor.execute("SELECT * FROM Orders")  # 'Orders' tablosundaki tüm verileri al
    orders = [
        {
            "id": row[0],
            "product_id": row[1],
            "quantity": row[2],
            "total_price": row[3],
        }
        for row in cursor.fetchall()
    ]
    return jsonify(orders)

# POST Metodu - Yeni sipariş eklemek
@app.route("/siparisyonetimsistemi", methods=["POST"])
def add_Order():
    if not request.is_json:  # Gönderilen verinin JSON formatında olup olmadığını kontrol et
        return jsonify({"message": "Content-Type must be 'application/json'"}), 415

    data = request.get_json()  # JSON verisini al

    # Veritabanına yeni sipariş ekleme
    try:
        cursor.execute(
            """
            INSERT INTO Orders (id, product_id, quantity, total_price)
            VALUES (?, ?, ?, ?)
            """,
            data["id"], data["product_id"], data["quantity"], data["total_price"]
        )
        connection.commit()  # Değişiklikleri kaydet
        return jsonify({"message": "Yeni sipariş başarıyla eklendi!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# PUT Metodu - Sipariş bilgilerini güncellemek
@app.route("/siparisyonetimsistemi/<int:id>", methods=["PUT"])
def update_Orders(id):
    data = request.get_json()  # JSON verisini al

    # Siparişi güncelleme
    try:
        cursor.execute(
            """
            UPDATE Orders
            SET product_id = ?, quantity = ?, total_price = ?
            WHERE id = ?
            """,
            data["product_id"], data["quantity"], data["total_price"], id
        )
        connection.commit()
        return jsonify({"message": "Sipariş başarıyla güncellendi!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# DELETE Metodu - Sipariş silmek
@app.route("/siparisyonetimsistemi/<int:id>", methods=["DELETE"])
def delete_Orders(id):
    try:
        cursor.execute("DELETE FROM Orders WHERE id = ?", id)  # Siparişi silme
        connection.commit()
        return jsonify({"message": "Sipariş başarıyla silindi!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Uygulama başlatılıyor
if __name__ == "__main__":
    app.run(debug=True)
