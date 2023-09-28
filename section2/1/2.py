import datetime

myStr = input()
myList = myStr.split("/")
myList = list(map(lambda x:int(x),myList))

#the birthday date 
myYear = myList[0]
myMonth = myList[1]
myDay = myList[2]

#today
year = datetime.date.today().year
month = datetime.date.today().month
day = datetime.date.today().day

#calculate people's age
if  year > myYear and month > myMonth:
    myAge = year - myYear
elif year > myYear and month == myMonth and day > myDay  :
    myAge = year - myYear
elif year > myYear and month < myMonth:
    myAge = year - myYear - 1
elif year > myYear and month == myMonth and day < myDay :
    myAge = year - myYear - 1

if myList[0] > 2023 or myList[1] > 12 or myList[2] > 31:
    print("WRONG")
else:
    print(myAge)
    







