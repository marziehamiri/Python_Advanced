import mysql.connector

cnx = mysql.connector.connect ( user = 'root',password = '123',host = '127.0.0.1',database = 'company')
query = 'select * from emoloyeee;'
cursor = cnx.cursor()
cursor.execute(query)
mylist = []
mylist1 = []
mylist2 = []
mylist3 = []

for (Name,Weight,Height) in cursor:
    mylist.append(Name)
    mylist.append(Weight)
    mylist.append(Height)
    mylist1.append(mylist)
    mylist = []
mylist1.sort(key=lambda x:x[2],reverse=True)
for i in range(len(mylist1)):
    if i == 0:
        continue
    elif i > 0:
        if mylist1[i][2] == mylist1[i-1][2]:
            mylist2.append(mylist1[i])
            mylist2.append(mylist1[i-1])
            mylist2.sort(key=lambda x:x[1])
            mylist1[i-1] = mylist2[0]
            mylist1[i] = mylist2[1]

for item in mylist1:
    mystring = ' '.join(str(x) for x in item)
    mylist3.append(mystring) 
    
for item in mylist3:
    print(item)

cnx.commit()
cnx.close()
