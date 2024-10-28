import random
list=[]
for i in range (20):
    num=random.randint(-10,10)
    list.append(num)
print(list)
inifatiamaior=tamfatiamaior=inifatiaatual=tamfatiaatual=0
for i in range(len(list)):
    if list[i]<0:
        tamfatiaatual+=1
        if tamfatiamaior==1:
            inifatiaatual=i
    else:
        if tamfatiaatual>tamfatiamaior:
            tamfatiamaior=tamfatiaatual
            inifatiamaior=inifatiaatual
        tamfatiaatual=0
print(inifatiamaior,tamfatiamaior)
del list[inifatiamaior:inifatiamaior+tamfatiamaior]
print(list)