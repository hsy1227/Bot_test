with open("class.txt","r") as f:
    girl=0
    boy=0
    for line in f.readlines():
        record=line.split(' ',5)
        print(record)
        if(record[0]!="\n"):

            if(record[2]=="0"):
                print("hi")
                girl+=1
            else:
                boy+=1
        else:
            exit()
    print(f"女生數量:{girl}\n男生數量:{boy}")
    f.close()
