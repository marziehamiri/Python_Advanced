
my_str1 = ""
my_list1 = []
my_list2 = []
number_of_people = int(input())
for i in range(number_of_people):
    my_str1 = input()
    my_list1 = my_str1.split()
    my_list2.append(my_list1) 
#print(my_list2)
count_Action = 0
count_Adventure = 0
count_History = 0
count_Comedy = 0
count_Romance = 0
count_Horror = 0
for i in range(len(my_list2)):
    if "Action" in my_list2[i]:
        count_Action = count_Action + 1 
    if "Adventure" in my_list2[i]:
        count_Adventure = count_Adventure + 1
    if "History" in my_list2[i]:
        count_History = count_History + 1
    if "Comedy" in my_list2[i]:
        count_Comedy = count_Comedy + 1
    if "Romance" in my_list2[i]:
        count_Romance = count_Romance + 1
    if "Horror" in my_list2[i]:
        count_Horror = count_Horror + 1
my_dict1 = {"Action":count_Action,"History":count_History,"Adventure":count_Adventure
,"Comedy":count_Comedy,"Romance":count_Romance,"Horror":count_Horror}
my_dict1 = sorted(my_dict1.items(),key = lambda x: x [ 1 ],reverse=True)

_before = 0
_before = my_dict1[0][1]
for i in range(1,6):
    if my_dict1[i][1] == _before : 
        for j in reversed(range(1,i+1)) :
            num2 = j
            num1 = j - 1 
            if my_dict1[num2][1] == my_dict1[num1][1]:
                marklist1 = sorted([my_dict1[num2],my_dict1[num1]],key =lambda x:x[0] )
                my_dict1[num1],my_dict1[num2] = marklist1
                _before = my_dict1[i][1]
        for j in range(1,i+1):
            num2 = j
            num1 = j - 1 
            if my_dict1[num2][1] == my_dict1[num1][1]:
                marklist1 = sorted([my_dict1[num2],my_dict1[num1]],key =lambda x:x[0] )
                my_dict1[num1],my_dict1[num2] = marklist1
                _before = my_dict1[i][1]
        
    else:
        _before = my_dict1[i][1]

    
for i in range(6):
    print("%s : %i"%(my_dict1[i][0],my_dict1[i][1]))




        
        




