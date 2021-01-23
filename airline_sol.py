import re # importing regular expression for parsing the CSV file

# initialising dictionary to store the airports and count
dic = {}

# open the CSV file for reading
with open('airlines.csv', 'r') as f:
    # read the lines and store it in lines variable
    # this will eat memory it is good practice to read line by line 
    # when dealing with large files
    lines = f.readlines()

    # go through all the lines in the CSV file except 1st which is row header
    for line in lines[1:]:
        # extract the airport name from line using regular expression
        airport = re.findall(r'"(.*?)"', line)[0]
        # increase the count if the key is present in dic otherwise make it 1
        dic[airport] = dic.get(airport, 0) + 1 
    # output1
    print('output1: ')
    print(dic)

    # output2
    # find the maximum airport count
    maximum = max(dic.values())
    # initialize dictionary to store multiple maximum airport count
    max_dic = {}
    
    # go through the dictionary and append multiple maximum airport count 
    # into the previously created dictionary
    for key, value in dic.items():
        if value == maximum:
            max_dic.get(key) = max_dic.get(key, value)

    # output2
    print('output2: ')
    print(max_dic)

    # output3
    # same as previous to find multiple minimum airport count
    minimum = min(dic.values())
    min_dic = {}
    for key, value in dic.items():
        if value == minimum:
            min_dic.get(key) = min_dic.get(key, value)

    # output3
    print('output3: ')
    print(min_dic)
    
    # close the CSV file
    f.close()
