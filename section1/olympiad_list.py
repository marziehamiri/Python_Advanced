my_str1 = ""
my_list1 = []
my_list2 = []
n = int(input())
for i in range(n):
    my_str1 = input()
    my_list1 = my_str1.split(".")
    my_list2.append(my_list1)
#print(my_list2)
for i in range (len(my_list2)):
    my_str2 = ""
    my_str2 = my_list2[i][1]
    my_str2 = str(my_str2) 
    my_str2 = my_str2.lower()
    my_str2 = my_str2.capitalize()
    my_list2[i][1] = my_str2
#print(my_list2)
my_list_f = []
my_list_m = []
for i in range(len(my_list2)):
    if my_list2[i][0] == "f":
        my_list_f.append(my_list2[i])
       
    elif my_list2[i][0] == "m":
        my_list_m.append(my_list2[i])
        

#print(my_list_f)
#print(my_list_m)
my_list_f.sort(key=lambda x:x[1])
my_list_m.sort(key=lambda x:x[1])

for i in range(len(my_list_f)):
    print("%s %s %s"%(my_list_f[i][0],my_list_f[i][1],my_list_f[i][2]))
for i in range(len(my_list_m)):
    print("%s %s %s"%(my_list_m[i][0],my_list_m[i][1],my_list_m[i][2]))