
thisdict={}
while(True):
    name=input()
    if name=='DATA_INPUT_END' :
        break
    number=input()
    thisdict[name]=number
print(thisdict)
while(True):
    findname=input()
    if findname=='END':
        break

    a=findname in thisdict.keys()
    if(a ==True):
        print(thisdict[findname])
    else:
        print('gg')

