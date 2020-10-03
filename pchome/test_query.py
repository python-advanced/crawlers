import mysql.connector

cnx = mysql.connector.connect(user='root', password='3596', host='127.0.0.1', database='pchome')
cursor = cnx.cursor(dictionary=True)

query = ("SELECT * FROM products "
         "WHERE name LIKE 'ASUS%'")

cursor.execute(query)

for row in cursor:
    # print(row)
    print(row['name'])

cursor.close()
cnx.close()