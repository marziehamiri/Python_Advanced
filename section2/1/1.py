import math
import numpy as np

class Salamat:
    
    def __init__(self,count):
        self.count = count

    myStr = ""
    a = []

    aHeight = []
    def getHeight(self):
        myStr = input()
        aHeight = myStr.split()
        aHeight = list(map(lambda x:float(x),aHeight))
        if len(aHeight) == self.count:
            #Salamat.a.append(aHeight)
            Salamat.a.append(np.mean(aHeight))
        return np.mean(aHeight)
            

    aWeight = []
    def getWeight(self):
        myStr = input()
        aWeight = myStr.split() 
        aWeight = list(map(lambda x:float(x),aWeight))
        if len(aWeight) == self.count:
            #Salamat.a.append(aWeight)
            Salamat.a.append(np.mean(aWeight))
        return np.mean(aWeight)
           

    aAge = []
    def getAge(self):
        myStr = input()
        aAge = myStr.split()
        aAge = list(map(lambda x:float(x),aAge))
        if len(aAge) == self.count:
            #Salamat.a.append(aAge)
            Salamat.a.append(np.mean(aAge))
        return np.mean(aAge)

        
    def getLargerAverage(self):
        if Salamat.a[1] > Salamat.a[4]:
            print("A")
        elif Salamat.a[1] == Salamat.a[4]:
            if Salamat.a[2] < Salamat.a[5]:
                 print("A")
            elif Salamat.a[2] == Salamat.a[5]:
                print("Same")
            else:
                print("B")

        else:
            print("B")
    

numA = int(input())   
firstClass = Salamat(numA)
firstAvgA = firstClass.getAge()
firstAvgH = firstClass.getHeight()    
firstAvgW = firstClass.getWeight()



numB = int(input())   
SecendClass = Salamat(numB)
secondAvgA = SecendClass.getAge()
secondAvgH = SecendClass.getHeight()    
secondAvgW = SecendClass.getWeight()


print(firstAvgA) 
print(firstAvgH) 
print(firstAvgW)

print(secondAvgA)
print(secondAvgH)
print(secondAvgW)


firstClass.getLargerAverage()       



