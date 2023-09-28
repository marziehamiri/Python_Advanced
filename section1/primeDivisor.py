my_list1 = []
my_list2 = []
my_list3 = []
counter = 0

for i in range(10):
    input_ = int(input())
    my_list1.append(input_)


co = 0
for i in range(len(my_list1)):
    Divisor = 2
    counter = 0
    while Divisor <= my_list1[i] :
        if my_list1[i] % Divisor == 0:
            for j in range(1,Divisor+1):
                
                if Divisor % j == 0:
                    co = co + 1
            
            if co == 2:
                counter = counter + 1
            co = 0  
        Divisor = Divisor + 1
    my_list2 = [my_list1[i],counter]
    my_list3.append(my_list2)

mux = 0
number = 0
for i in range(len(my_list3)):
    if i==0:
        mux = my_list3[i][1]
        number = my_list3[i][0]
    elif my_list3[i][1] > mux:
        mux = my_list3[i][1]
        number = my_list3[i][0]
    elif my_list3[i][1] == mux and number > my_list3[i][0]:
        number = number
        mux = my_list3[i][1]
    elif my_list3[i][1] == mux and number < my_list3[i][0]:
        number = my_list3[i][0]
        mux = my_list3[i][1]


print(number,mux)













    