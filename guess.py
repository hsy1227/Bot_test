import random
ans=random.randint(1,100)
time=5

low=1
high=100
while(time!=0):
    number=int(input(f"剩餘機會: {time},數字範圍為:{low} 到 {high} 輸入數字吧:D "))
    if(number==ans):
        print("答對ㄌ:D")
        break
    else:
        if(number > ans):
            high=number
        if(number<ans and number>=low):
            low=number
    time-=1
if(time==0):
    print(f"公布答案: {ans}")
