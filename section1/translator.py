
from collections import OrderedDict

lst_sentences = []
n = int(input())
lst_words = []
for i in range(n):
    lst_sentences = input()
    lst_words.append(lst_sentences.split()) 
my_str = input()    
#print(lst_words)
dict_words = OrderedDict()
for i in range(n):
    dict_words.update( {i:{"Persian":lst_words[i][0],
    "English":lst_words[i][1],
    "French":lst_words[i][2],
    "German":lst_words[i][3]}}) 
#print(dict_words)"
lst_str = []
lst_str = my_str.split()
for i  in range(len(lst_str)) :
    for j in range(len(dict_words)):
        if lst_str[i] == dict_words[j]["English"] or lst_str[i] == dict_words[j]["French"] or lst_str[i] == dict_words[j]["German"] :
            lst_str[i] = dict_words[j]["Persian"]

for i in range(len(lst_str)):
    print("%s"%(lst_str[i]),end=" ")

