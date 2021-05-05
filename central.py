import csv
with open('./SOCR-HeightWeight2.csv')as f:
    read = csv.reader(f)
    file = list(read)

file.pop(0)

heigth = []
for i in range(len (file)):
     h = file[i][1]
     heigth.append(float(h))

def mean():
    sum = 0
    for i in heigth:
        sum = sum + i
    print(sum/len(heigth))

def median():
    heigth.sort()
    length = len(heigth)
    if(length % 2 == 0):
        upperindex = int(length/2+1)
        loweindex = int(length/2)
        uppervalue = heigth[upperindex]
        lowervalue = heigth[loweindex]
        medi = (uppervalue+lowervalue)/2
        print(medi)
    else:
        print("heigth is odd")
        index = int(length/2)
        value = heigth[index]
        print(value)

def mode():
    print(max(heigth))
    print(min(heigth))
    one = 0
    two = 0
    three = 0
    for i in heigth:
        if(60 < i < 65):
            one= one+1
        elif(65 < i <70):
            two=two+1
        elif(70 < i < 75):
            three = three+1
    value = (65+70)/2
    print(value)

mode()