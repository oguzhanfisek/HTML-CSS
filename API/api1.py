import pyodbc

connection = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=DESKTOP-OBLTQPD;"
    "Database=AracKiralamaSistemi;"
    "Trusted_Connection=yes;"
)


cursor = connection.cursor()
print("sql bağlantısı oldu", cursor)

create_table_query = """
CREATE TABLE Products (
    Id INT PRIMARY KEY IDENTITY(1,1),
    Name NVARCHAR(50) NOT NULL,
    Price DECİMAL(20,2) NOT NULL,
    Stock INT NOT NULL
);
"""

cursor.execute(create_table_query)
connection.commit()
print("Products tablosu oluşturuldu.")