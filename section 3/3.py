import mysql.connector

uemail = input()
upassword = input()
cnx = mysql.connector.connect( user = 'root',password = '123',host = '127.0.0.1',database = 'company')
query = 'INSERT INTO uuser(username,password) VALUES(\"%s\",\"%s\");'%(uemail,upassword)
cursor = cnx.cursor()
cursor.execute(query)
cnx.commit()
print('insert has done')
cnx.close()