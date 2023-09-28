import random
randNum = []
class human:
    def __init__(self,name):
        self.name = name
        randNum.append(random.random()) 
        
        
class soccerPlayer(human):
    def get_teamName(self,teamname):
        self.teamname = teamname
    def Print_information(self):
        print(self.name + " " + self.teamname)

players = ['حسین','مازیار','اکبر','نیما','مهدی','فرهاد','محمد','خشایار','میلاد',
           'مصطفی','امین','سعید','پویا','پوریا','رضا','علی','بهزاد','سهیل','بهروز',
           'شهروز','سامان','محسن']

objectlist = []
for i in range(len(players)):
    objectlist.append(soccerPlayer(players[i]))

for i in range(len(randNum)):
    if randNum[i] > 0.5:
        objectlist[i].get_teamName("A")
    else:
        objectlist[i].get_teamName("B")
for i in range(len(objectlist)):
    objectlist[i].Print_information()


