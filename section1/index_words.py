import re
my_str = input()
lst_lines = []
lst_words = []
lst_lines = re.split(r"[.;]",my_str)
#print(lst_lines)
for i in range(len(lst_lines)):
    lst_words.append(lst_lines[i].split())

count = 0
a = 0
matches = []
n = 0
regex = r"\b[A-Z]\w*"
for i in range(len(lst_words)):
    for j in range(len(lst_words[i])):
        if j != 0 :
            matches = re.findall(regex, lst_words[i][j])
            
            if len(matches) != 0 :
                print("%i:%s"%(j+n+i+1,matches[0])) 
                count = 1 + count  
    n = j + n 
if count == 0:
    print("None")   
    






