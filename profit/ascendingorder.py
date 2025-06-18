NumList = []

Number = int(input("Please enter the number yuh want to arrange"))
for i in range(1, Number+1):
    value =int(input("Enter the values in the Element"));
    NumList.append(value)
    
for i in range(Number):
    for j in range(i+1 , Number):
        if(NumList[i]>NumList[j]):
            temp = NumList[i]
            NumList[i]=NumList[j]
            NumList[j]=temp;
print("the arrange list are : temp",NumList)