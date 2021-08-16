n=int(input())
score={}
maxscore={}
ans=''
for i in range(n):
    name,status=input().split()
    if(status =='AC'):
        if(score.get(name)==None):
            score[name]=status
            maxscore[name]=1
        else:
            for k,v in maxscore.items():
                if k==name:
                    maxscore[name]=v+1
winscore=0
ans=""
for name in maxscore:
    if(maxscore[name]>=winscore):
        winscore=maxscore[name]
        ans=name
print(ans)
