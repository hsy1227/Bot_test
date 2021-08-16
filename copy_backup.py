with open("class.txt","r") as f1:
    with open("class2.txt","w") as f2:
        f2.write(f1.read())
