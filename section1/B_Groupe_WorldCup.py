from collections import OrderedDict

dict_game = OrderedDict()
my_list1 = []
my_list2 = []

for i in range(6):
    my_list1 = input()
    my_list1 = my_list1.split("-")
    for i in range(len(my_list1)):
        my_list1[i] = int(my_list1[i])
    my_list2.append(my_list1)

dict_game = {0: {"Iran":my_list2[0][0],"Spain":my_list2[0][1]},
1:{"Iran":my_list2[1][0],"Portugal":my_list2[1][1]},
2:{"Iran":my_list2[2][0],"Morocco":my_list2[2][1]},
3:{"Spain":my_list2[3][0],"Portugal":my_list2[3][1]},   
4:{"Spain":my_list2[4][0],"Morocco":my_list2[4][1]},
5:{"Portugal":my_list2[5][0],"Morocco":my_list2[5][1]}}



wins_Iran = 0
loses_Iran = 0
drawes_Iran = 0
goal_Iran = 0
points_Iran = 0
wins_Spain = 0
loses_Spain = 0
drawes_Spain = 0
goal_Spain = 0
points_Spain = 0
wins_Portugal = 0
loses_Portugal = 0
drawes_Portugal = 0
goal_Portugal = 0
points_Portugal = 0
wins_Morocco = 0
loses_Morocco = 0
drawes_Morocco = 0
goal_Morocco = 0
points_Morocco = 0
goal_d_Iran = 0
goal_d_Spain = 0
goal_d_Morroco = 0
goal_d_Portugal = 0

#first_game
if dict_game[0]["Iran"] == dict_game[0]["Spain"]:
    drawes_Iran = drawes_Iran + 1
    drawes_Spain = drawes_Spain + 1
    points_Iran = points_Iran + 1
    points_Spain = points_Spain + 1
    #goal_Iran = dict_game[0]["Iran"] + goal_Iran
    #goal_Spain = dict_game[0]["Spain"] + goal_Spain
    goal_d_Iran = (dict_game[0]["Iran"] - dict_game[0]["Spain"]) + goal_d_Iran
    goal_d_Spain = (dict_game[0]["Spain"] - dict_game[0]["Iran"]) + goal_d_Spain

if dict_game[0]["Iran"] < dict_game[0]["Spain"]:
    loses_Iran = loses_Iran + 1
    wins_Iran = wins_Iran + 1
    #goal_Iran = dict_game[0]["Iran"] + goal_Iran
    #goal_Spain = dict_game[0]["Spain"] + goal_Spain
    points_Spain = points_Spain + 3
    goal_d_Iran = (dict_game[0]["Iran"] - dict_game[0]["Spain"]) + goal_d_Iran
    goal_d_Spain = (dict_game[0]["Spain"] - dict_game[0]["Iran"]) + goal_d_Spain
if dict_game[0]["Iran"] > dict_game[0]["Spain"]:
    wins_Iran = wins_Iran + 1
    loses_Spain = loses_Spain + 1
    points_Iran = points_Iran + 3
    #goal_Iran = dict_game[0]["Iran"] + goal_Iran
    #goal_Spain = dict_game[0]["Spain"] + goal_Spain
    goal_d_Iran = (dict_game[0]["Iran"] - dict_game[0]["Spain"]) + goal_d_Iran
    goal_d_Spain = (dict_game[0]["Spain"] - dict_game[0]["Iran"]) + goal_d_Spain
#second_game
if dict_game[1]["Iran"] == dict_game[1]["Portugal"]:
    drawes_Iran = drawes_Iran + 1
    drawes_Portugal = drawes_Portugal + 1
    points_Iran = points_Iran + 1
    points_Portugal = points_Portugal + 1
    #goal_Iran = dict_game[1]["Iran"] + goal_Iran
    #goal_Portugal = dict_game[1]["Portugal"] + goal_Portugal
    goal_d_Iran = (dict_game[1]["Iran"] - dict_game[1]["Portugal"]) + goal_d_Iran
    goal_d_Portugal = (dict_game[1]["Portugal"] - dict_game[1]["Iran"]) + goal_d_Portugal
if dict_game[1]["Iran"] < dict_game[1]["Portugal"]:
    loses_Iran = loses_Iran + 1
    wins_Portugal = wins_Portugal + 1
    #goal_Iran = dict_game[1]["Iran"] + goal_Iran
    #goal_Portugal = dict_game[1]["Portugal"] + goal_Portugal
    points_Portugal = points_Portugal + 3
    goal_d_Iran = (dict_game[1]["Iran"] - dict_game[1]["Portugal"]) + goal_d_Iran
    goal_d_Portugal = (dict_game[1]["Portugal"] - dict_game[1]["Iran"]) + goal_d_Portugal
if dict_game[1]["Iran"] > dict_game[1]["Portugal"]:
    wins_Iran = wins_Iran + 1
    loses_Portugal = loses_Portugal + 1
    points_Iran = points_Iran + 3
    #goal_Iran = dict_game[1]["Iran"] + goal_Iran
    #goal_Portugal = dict_game[1]["Portugal"] + goal_Portugal
    goal_d_Iran = (dict_game[1]["Iran"] - dict_game[1]["Portugal"]) + goal_d_Iran
    goal_d_Portugal = (dict_game[1]["Portugal"] - dict_game[1]["Iran"]) + goal_d_Portugal
#third_game
if dict_game[2]["Iran"] == dict_game[2]["Morocco"]:
    drawes_Iran = drawes_Iran + 1
    drawes_Morocco = drawes_Morocco + 1
    points_Iran = points_Iran + 1
    points_Morocco = points_Morocco + 1
    #goal_Iran = dict_game[2]["Iran"] + goal_Iran
    #goal_Morocco = dict_game[2]["Morocco"] + goal_Morocco
    goal_d_Iran = (dict_game[2]["Iran"] - dict_game[2]["Morocco"]) + goal_d_Iran
    goal_d_Morroco = ( dict_game[2]["Morocco"] - dict_game[2]["Iran"]) + goal_d_Morroco
if dict_game[2]["Iran"] < dict_game[2]["Morocco"]:
    loses_Iran = loses_Iran + 1
    wins_Morocco = wins_Morocco + 1
    #goal_Iran = dict_game[2]["Iran"] + goal_Iran
    #goal_Morocco = dict_game[2]["Morocco"] + goal_Morocco
    points_Morocco = points_Morocco + 3
    goal_d_Iran = (dict_game[2]["Iran"] - dict_game[2]["Morocco"]) + goal_d_Iran
    goal_d_Morroco = ( dict_game[2]["Morocco"] - dict_game[2]["Iran"]) + goal_d_Morroco
if dict_game[2]["Iran"] > dict_game[2]["Morocco"]:
    wins_Iran = wins_Iran + 1
    loses_Morocco = loses_Morocco + 1
    points_Iran = points_Iran + 3
    #goal_Iran = dict_game[2]["Iran"] + goal_Iran
    #goal_Morocco = dict_game[2]["Morocco"] + goal_Morocco
    goal_d_Iran = (dict_game[2]["Iran"] - dict_game[2]["Morocco"]) + goal_d_Iran
    goal_d_Morroco = ( dict_game[2]["Morocco"] - dict_game[2]["Iran"]) + goal_d_Morroco
#forth_game
if dict_game[3]["Spain"] == dict_game[3]["Portugal"]:
    drawes_Spain = drawes_Spain + 1
    drawes_Portugal = drawes_Portugal + 1
    points_Spain = points_Spain + 1
    points_Portugal = points_Portugal + 1
    #goal_Spain = dict_game[3]["Spain"] + goal_Spain
    #goal_Portugal = dict_game[3]["Portugal"] + goal_Portugal
    goal_d_Spain = (dict_game[3]["Spain"] - dict_game[3]["Portugal"]) + goal_d_Spain
    goal_d_Portugal = (dict_game[3]["Portugal"] - dict_game[3]["Spain"] ) + goal_d_Portugal
if dict_game[3]["Spain"] < dict_game[3]["Portugal"]:
    loses_Spain = loses_Spain + 1
    wins_Portugal = wins_Portugal + 1
    #goal_Spain = dict_game[3]["Spain"] + goal_Spain
    #goal_Portugal = dict_game[3]["Portugal"] + goal_Portugal
    points_Portugal = points_Portugal + 3
    goal_d_Spain = (dict_game[3]["Spain"] - dict_game[3]["Portugal"]) + goal_d_Spain
    goal_d_Portugal = (dict_game[3]["Portugal"] - dict_game[3]["Spain"] ) + goal_d_Portugal
if dict_game[3]["Spain"] > dict_game[3]["Portugal"]:
    wins_Spain = wins_Spain + 1
    loses_Portugal = loses_Portugal + 1
    points_Spain = points_Spain + 3
    #goal_Spain = dict_game[3]["Spain"] + goal_Spain
    #goal_Portugal = dict_game[3]["Portugal"] + goal_Portugal
    goal_d_Spain = (dict_game[3]["Spain"] - dict_game[3]["Portugal"]) + goal_d_Spain
    goal_d_Portugal = (dict_game[3]["Portugal"] - dict_game[3]["Spain"] ) + goal_d_Portugal
#fifth_game
if dict_game[4]["Spain"] == dict_game[4]["Morocco"]:
    drawes_Spain = drawes_Spain + 1
    drawes_Morocco = drawes_Morocco + 1
    points_Spain = points_Spain + 1
    points_Morocco = points_Morocco + 1
    #goal_Spain = dict_game[4]["Spain"] + goal_Spain
    #goal_Morocco = dict_game[4]["Morocco"] + goal_Morocco
    goal_d_Spain = (dict_game[4]["Spain"] - dict_game[4]["Morocco"]) + goal_d_Spain
    goal_d_Morroco = (dict_game[4]["Morocco"] -dict_game[4]["Spain"] ) + goal_d_Morroco
if dict_game[4]["Spain"] < dict_game[4]["Morocco"]:
    loses_Spain = loses_Spain + 1
    wins_Morocco = wins_Morocco + 1
    #goal_Spain = dict_game[4]["Spain"] + goal_Spain
    #goal_Morocco = dict_game[4]["Morocco"] + goal_Morocco
    points_Morocco = points_Morocco + 3
    goal_d_Spain = (dict_game[4]["Spain"] - dict_game[4]["Morocco"]) + goal_d_Spain
    goal_d_Morroco = (dict_game[4]["Morocco"] -dict_game[4]["Spain"] ) + goal_d_Morroco
if dict_game[4]["Spain"] > dict_game[4]["Morocco"]:
    wins_Spain = wins_Spain + 1
    loses_Morocco = loses_Morocco + 1
    points_Spain = points_Spain + 3
    #goal_Spain = dict_game[4]["Spain"] + goal_Spain
    #goal_Morocco = dict_game[4]["Morocco"] + goal_Morocco
    goal_d_Spain = (dict_game[4]["Spain"] - dict_game[4]["Morocco"]) + goal_d_Spain
    goal_d_Morroco = (dict_game[4]["Morocco"] -dict_game[4]["Spain"] ) + goal_d_Morroco
#sixth_game
if dict_game[5]["Portugal"] == dict_game[5]["Morocco"]:
    drawes_Portugal = drawes_Portugal + 1
    drawes_Morocco = drawes_Morocco + 1
    points_Portugal = points_Portugal + 1
    points_Morocco = points_Morocco + 1
    #goal_Portugal = dict_game[5]["Portugal"] + goal_Portugal
    #goal_Morocco = dict_game[5]["Morocco"] + goal_Morocco
    goal_d_Portugal = (dict_game[5]["Portugal"] - dict_game[5]["Morocco"] ) + goal_d_Portugal
    goal_d_Morroco = (dict_game[5]["Morocco"] - dict_game[5]["Portugal"]) + goal_d_Morroco
if dict_game[5]["Portugal"] < dict_game[5]["Morocco"]:
    loses_Portugal = loses_Portugal + 1
    wins_Morocco = wins_Morocco + 1
    #goal_Portugal = dict_game[5]["Portugal"] + goal_Portugal
    #goal_Morocco = dict_game[5]["Morocco"] + goal_Morocco
    points_Morocco = points_Morocco + 3
    goal_d_Portugal = (dict_game[5]["Portugal"] - dict_game[5]["Morocco"] ) + goal_d_Portugal
    goal_d_Morroco = (dict_game[5]["Morocco"] - dict_game[5]["Portugal"]) + goal_d_Morroco
if dict_game[5]["Portugal"] > dict_game[5]["Morocco"]:
    wins_Portugal = wins_Portugal + 1
    loses_Morocco = loses_Morocco + 1
    points_Portugal = points_Portugal + 3
    #goal_Portugal = dict_game[5]["Portugal"] +  goal_Portugal
    #goal_Morocco = dict_game[5]["Morocco"] + goal_Morocco
    goal_d_Portugal = (dict_game[5]["Portugal"] - dict_game[5]["Morocco"] ) + goal_d_Portugal
    goal_d_Morroco = (dict_game[5]["Morocco"] - dict_game[5]["Portugal"]) + goal_d_Morroco

my_dict3 = OrderedDict()
my_dict3 = {1:{"name":"Iran","wins":wins_Iran,"loses":loses_Iran,"draws":drawes_Iran,"goal difference":goal_d_Iran ,"points":points_Iran},
2:{"name":"Spain","wins":wins_Spain,"loses":loses_Spain,"draws":drawes_Spain ,"goal difference":goal_d_Spain,"points":points_Spain},
3:{"name":"Portugal","wins":wins_Portugal,"loses":loses_Portugal,"draws":drawes_Portugal,"goal difference":goal_d_Portugal,"points":points_Portugal },
4:{"name":"Morocco","wins":wins_Morocco ,"loses":loses_Morocco ,"draws":drawes_Morocco ,"goal difference":goal_d_Morroco,"points":points_Morocco}
}

my_dict3 = sorted(my_dict3.items(),key = lambda x: x [ 1 ] [ "points" ],reverse=True)

_before = 0
_before = my_dict3[0][1]["points"]
for i in range(1,4):
    if my_dict3[i][1]["points"] == _before : 
        for j in reversed(range(1,i+1)) :
            num2 = j
            num1 = j - 1 
            if my_dict3[num2][1]["points"] == my_dict3[num1][1]["points"]:
                marklist1 = sorted([my_dict3[num2],my_dict3[num1]],key =lambda x:x[1]["wins"])
                my_dict3[num1],my_dict3[num2] = marklist1
                _before = my_dict3[i][1]["points"]
        for j in range(1,i+1):
            num2 = j
            num1 = j - 1 
            if my_dict3[num2][1]["points"] == my_dict3[num1][1]["points"]:
                marklist1 = sorted([my_dict3[num2],my_dict3[num1]],key =lambda x:x[1]["wins"])
                my_dict3[num1],my_dict3[num2] = marklist1
                _before = my_dict3[i][1]["points"]
        
    else:
        _before = my_dict3[i][1]["points"]




_before2 = 0
_before2 = my_dict3[0][1]["points"]
_before3 = my_dict3[0][1]["wins"]
for i in range(1,4):
    if my_dict3[i][1]["points"] == _before2 and my_dict3[i][1]["wins"] == _before3: 
        for j in reversed(range(1,i+1)) :
            num2 = j
            num1 = j - 1 
            if my_dict3[num2][1]["points"] == my_dict3[num1][1]["points"] and my_dict3[num2][1]["wins"] == my_dict3[num1][1]["wins"]:
                marklist1 = sorted([my_dict3[num2],my_dict3[num1]],key =lambda x:x[1]["name"])
                my_dict3[num1],my_dict3[num2] = marklist1
                _before2 = my_dict3[i][1]["points"]
                _before3 = my_dict3[i][1]["wins"]  
        for j in range(1,i+1):
            num2 = j
            num1 = j - 1 
            if my_dict3[num2][1]["points"] == my_dict3[num1][1]["points"] and my_dict3[num2][1]["wins"] == my_dict3[num1][1]["wins"]:
                marklist1 = sorted([my_dict3[num2],my_dict3[num1]],key =lambda x:x[1]["name"])
                my_dict3[num1],my_dict3[num2] = marklist1
                _before2 = my_dict3[i][1]["points"]
                _before3 = my_dict3[i][1]["wins"]
        
    else:
        _before2 = my_dict3[i][1]["points"]
        _before3 = my_dict3[i][1]["wins"]




print("%s wins:%i , loses:%i , draws:%i , goal difference:%i , points:%i"%(my_dict3[0][1]["name"],my_dict3[0][1]["wins"],my_dict3[0][1]["loses"],my_dict3[0][1]["draws"],my_dict3[0][1]["goal difference"],my_dict3[0][1]["points"]))
print("%s wins:%i , loses:%i , draws:%i , goal difference:%i , points:%i"%(my_dict3[1][1]["name"],my_dict3[1][1]["wins"],my_dict3[1][1]["loses"],my_dict3[1][1]["draws"],my_dict3[1][1]["goal difference"],my_dict3[1][1]["points"]))
print("%s wins:%i , loses:%i , draws:%i , goal difference:%i , points:%i"%(my_dict3[2][1]["name"],my_dict3[2][1]["wins"],my_dict3[2][1]["loses"],my_dict3[2][1]["draws"],my_dict3[2][1]["goal difference"],my_dict3[2][1]["points"]))
print("%s wins:%i , loses:%i , draws:%i , goal difference:%i , points:%i"%(my_dict3[3][1]["name"],my_dict3[3][1]["wins"],my_dict3[3][1]["loses"],my_dict3[3][1]["draws"],my_dict3[3][1]["goal difference"],my_dict3[3][1]["points"]))








