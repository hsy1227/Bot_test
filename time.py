import time

result=time.strftime("今天是%Y年%m月%d日,現在時間已經是%H點%M分%S秒",time.localtime())
print(result)
start=time.time()
print("執行程式囉")
time.sleep(1.2345)
end=time.time()
ans=end-start
endresult=time.strftime("今天是%Y年%m月%d日,現在時間已經是%H點%M分%S秒",time.localtime())
print(endresult)
print(ans)
