import pyodbc

connection = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=DESKTOP-OBLTQPD;"
    "Database=AracKiralamaSistemi;"
    "Trusted_Connection=yes;"
)

cursor = connection.cursor()
print("sql bağlantısı oldu", cursor)

"""
create_table_query = 
CREATE TABLE Products (
    Id INT PRIMARY KEY IDENTITY(1,1),
    Name NVARCHAR(50) NOT NULL,
    Price DECİMAL(20,2) NOT NULL,
    Stock INT NOT NULL
);
cursor.execute(create_table_query)
connection.commit()
print("Products tablosu oluşturuldu.")

insert_query = "INSERT INTO Products(Name, Price, Stock)VALUES(?,?,?)"
cursor.execute(insert_query,("Laptop",15000.99,10))
connection.commit()
print("Veri eklendi.")

update_query = "UPDATE Products SET Stock = ? WHERE Name = ?"
cursor.execute(update_query,(20,"Laptop"))
connection.commit()
print("Veri güncellendi.")

delete_query = "DELETE FROM Products WHERE Name  = ?"
cursor.execute(delete_query,("Laptop",))
connection.commit()
print("Veri silindi.") 

alter_table_query = "ALTER TABLE Products ADD Description NVARCHAR(100)"
cursor.execute(alter_table_query)
connection.commit()
print("Tablo güncellendi.")

drop_table_query = "DROP TABLE Products"
cursor.execute(drop_table_query)
connection.commit()
print("Tablo silindi.")"""







create_table_query = """
CREATE TABLE Students (
    StudentId INT PRIMARY KEY IDENTITY(1,1),
    Name NVARCHAR(50) NOT NULL,
    Age INT NOT NULL,
    Grade NVARCHAR(50) NOT NULL
);"""
"""cursor.execute(create_table_query)
connection.commit()
print("Tablo oluşturuldu.")

insert_query = "INSERT INTO Students(Name, Age, Grade)VALUES(?,?,?)"
cursor.execute(insert_query,("Ali",15,"9th"))
cursor.execute(insert_query,("Ayşe",16,"10th"))
cursor.execute(insert_query,("Mehmet",14,"8th"))
connection.commit()
print("Veri eklendi.")

tumDegerler = "Select * from Students"

cursor.execute(tumDegerler)
rows = cursor.fetchall()

print("tablo verileri")

for row in rows:
    print(row)

update_query = "UPDATE Students SET Age = ? WHERE Name = ?"
cursor.execute(update_query,(16,"Ali"))
connection.commit()
print("Veri güncellendi.")

delete_query = "DELETE FROM Students WHERE Name  = ?"
cursor.execute(delete_query,("Ayşe",))
connection.commit()
print("Veri silindi.")

alter_table_query = "ALTER TABLE Students ADD Address NVARCHAR(100)"
cursor.execute(alter_table_query)
connection.commit()
print("Tablo güncellendi.")



drop_table_query = "DROP TABLE Students"
cursor.execute(drop_table_query)
connection.commit()
print("Tablo silindi.")"""





"""
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Merhaba Flask!"

if __name__ == '__main__':
    app.run(debug=True)"""


"""
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/resource',
methods=['GET'])
def get_resource():
    return jsonify({"message":
"Resource retrieved successfuly"})

if __name__ == '__main__':
    app.run(debug=True)




@app.route('/api/resource',methods=['POST'])
def create_resource():
    data = request.get_json()
    return jsonify({"data":data, "message": "POST request successful"}),201
    """

