import mysql.connector

cnx = mysql.connector.connect(user = 'root', password = '123' , host = '127.0.0.1' , database = 'test')
query = 'select * from people;'
cursor = cnx.cursor()
cursor.execute(query)

for (name,age,gender) in cursor:
    print('%s is %i years old and is a %s'%(name,age,gender))
cnx.commit()
cnx.close()


