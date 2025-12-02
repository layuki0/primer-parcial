myarray = [3,5,8,29,22,2,678,2]
minVal = myarray[0]

for i in myarray:
    if i < minVal:
        minVal = i

print('Lowest value', minVal)
