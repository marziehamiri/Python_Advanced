import mysql.connector

print("connecting to db")
cnx = mysql.connector.connect(
    user = 'root',password = '123', host = '127.0.0.1', database = 'test'
)
print("connected to db")
cursor = cnx.cursor()
cursor.execute('INSERT INTO people VALUES(\'far\',38,\'f\')')
cnx.commit()
print('insert has done')
cnx.close()
