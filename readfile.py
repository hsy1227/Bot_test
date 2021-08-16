with open("class.txt","r") as f:
    girl=0
    boy=0
    record=[]
    firstline=f.readline().rstrip()
    number1=firstline.split(" ")[2]
    record.append(number1)
    second=f.readline().rstrip()
    number2=second.split(" ")[2]
    record.append(number2)
    third=f.readline().rstrip()
    number3=third.split(" ")[2]
    record.append(number3)
    four=f.readline().rstrip()
    number4=four.split(" ")[2]
    record.append(number4)
    for i in range(len(record)):
        if(record[i]=="0"):
            girl+=1
        else:
            boy+=1

    print(f"女生數量:{girl}\n男生數量:{boy}")
    f.close()
