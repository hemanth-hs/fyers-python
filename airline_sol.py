import re

dic = {}
with open('airlines.csv', 'r') as f:
    lines = f.readlines()
    for line in lines[1:]:
        airport_code = line[:4]
        airport = re.findall(r'"(.*?)"', line)[0]
        dic[airport] = dic.get(airport, 0) + 1 
    print('output1: ')
    print(dic)
    maximum = max(dic.values())
    max_dic = {}
    for key, value in dic.items():
        if value == maximum:
            max_dic.get(key) = max_dic.get(key, value)
    print(max_dic)
