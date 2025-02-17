from flask import Flask, request, jsonify
import pyodbc

# Flask uygulamasını başlat
app = Flask(__name__)

# Veritabanı bağlantısı
connection = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=DESKTOP-OBLTQPD;"  # Server adını uygun şekilde değiştirin
    "Database=RandevuYonetimSistemi;"  # Veritabanı adı
    "Trusted_Connection=yes;"  
)

cursor = connection.cursor()

# GET Metodu - Tüm randevuları listelemek (table1 tablosundan)
@app.route("/randevuyonetimsistemi", methods=["GET"])
def get_table1():
    cursor.execute("SELECT * FROM table1")  # 'table1' tablosundaki tüm verileri al
    rows = cursor.fetchall()  # Verileri al
    print(rows)  # Veriyi konsola yazdırıyoruz
    table1_data = []
    
    for row in rows:
        # Verilerin her birini kontrol et
        table1_data.append({
            "id": row[0],
            "user_id": row[1],
            "date": row[2],
            # `time` objesini string formatına çeviriyoruz
            "time": row[3].strftime('%H:%M:%S') if row[3] else None,
            "description": row[4]
        })
    
    return jsonify(table1_data)  # Bu satırda table1_data döndürüyoruz.

# POST Metodu - Yeni randevu eklemek (table1 tablosuna)
@app.route("/randevuyonetimsistemi", methods=["POST"])
def add_to_table1():
    if not request.is_json:  # Gönderilen verinin JSON formatında olup olmadığını kontrol et
        return jsonify({"message": "Content-Type must be 'application/json'"}), 415

    data = request.get_json()  # JSON verisini al

    # Veritabanına yeni randevu ekleme (table1 tablosuna)
    try:
        cursor.execute(
            """
            INSERT INTO table1 (user_id, date, time, description)
            VALUES (?, ?, ?, ?)
            """,
            data["user_id"], data["date"], data["time"], data["description"]
        )
        connection.commit()  # Değişiklikleri kaydet
        return jsonify({"message": "Yeni randevu başarıyla eklendi!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# PUT Metodu - Randevu bilgilerini güncellemek (table1 tablosu)
@app.route("/randevuyonetimsistemi/<int:id>", methods=["PUT"])
def update_table1(id):
    data = request.get_json()  # JSON verisini al

    # Randevuyu güncelleme (table1 tablosunda)
    try:
        cursor.execute(
            """
            UPDATE table1
            SET user_id = ?, date = ?, time = ?, description = ?
            WHERE id = ?
            """,
            data["user_id"], data["date"], data["time"], data["description"], id
        )
        connection.commit()
        return jsonify({"message": "Randevu başarıyla güncellendi!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# DELETE Metodu - Randevu silmek (table1 tablosundan)
@app.route("/randevuyonetimsistemi/<int:id>", methods=["DELETE"])
def delete_from_table1(id):
    try:
        cursor.execute("DELETE FROM table1 WHERE id = ?", id)  # Randevuyu silme (table1 tablosu)
        connection.commit()
        return jsonify({"message": "Randevu başarıyla silindi!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Uygulama başlatılıyor
if __name__ == "__main__":
    app.run(debug=True)
