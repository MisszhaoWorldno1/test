import copy
import random
mappp=[]
mapp=[]
row=random.randint(3,30)
line=random.randint(3,30)
for i in range(row):
    mappp.append([])
for i in range(row):
    for j in range(line):
        if random.random()<0.8:
            mappp[i].append(0)
        else:
            mappp[i].append(2)                           #生成随机地图
mappp[random.randint(0,row-1)][random.randint(0,line-1)]=1
mappp[random.randint(0,row-1)][random.randint(0,line-1)]=3 #随机生成地图出入口

mapp=copy.deepcopy(mappp)
print("地图是:")
for i in mapp:
    print(i)
entrance=[0,0]
out=[0,0]
tempt=[]
determin=[]
determin1=[]
for i in mapp:
	try:
		entrance[1]=i.index(1)
		entrance[0]=mapp.index(i)
	except:continue                    #识别入口

for i in mapp:
	try:
		out[1]=i.index(3)
		out[0]=mapp.index(i)
	except:continue                    #识别出口

now=copy.deepcopy(entrance)                             #初始化当前位置
move=['u','d','l','r']
def rule(movement):
    mapp[now[0]][now[1]]=2
    if movement=='u':
        if now[0]>0:
            now[0]-=1
    if movement=='d':
        if now[0]<len(mapp):
            now[0]+=1
    if movement=='l':
        if now[1]>0:
            now[1]-=1
    if movement=='r':
        if now[1]<len(mapp[0]):
            now[1]+=1
    return 0

def distance(now,out):
    return (pow(now[0]-out[0],2)+pow(now[1]-out[1],2))        #评估函数1

def distance1(now,out):
    return abs(now[0]-out[0])+abs(now[1]-out[1])   #评估函数2

def choice():                                                 
    if now[0]>0:
        if mapp[now[0]-1][now[1]]!=2:
            now[0]-=1
            tempt.append(distance(now,out))
            now[0]+=1
        else:
            tempt.append(10000)
    else:
        tempt.append(10000)

        
    if now[0]<len(mapp)-1:
        if mapp[now[0]+1][now[1]]!=2:
            now[0]+=1
            tempt.append(distance(now,out))
            now[0]-=1
        else:
            tempt.append(10000)
    else:
        tempt.append(10000)

        
    if now[1]>0:
        if mapp[now[0]][now[1]-1]!=2:
            now[1]-=1
            tempt.append(distance(now,out))
            now[1]+=1
        else:
            tempt.append(10000)
    else:
        tempt.append(10000)

        
    if now[1]<len(mapp[0])-1:
        if mapp[now[0]][now[1]+1]!=2:
            now[1]+=1
            tempt.append(distance(now,out))
            now[1]-=1
        else:
            tempt.append(10000)
    else:
        tempt.append(10000)

        
    x=tempt.index(min(tempt))
    tempt.clear()
    
    return(move[x])

def choice1():
    if now[0]>0:
        if mapp[now[0]-1][now[1]]!=2:
            now[0]-=1
            tempt.append(distance1(now,out))
            now[0]+=1
        else:
            tempt.append(10000)
    else:
        tempt.append(10000)

        
    if now[0]<len(mapp)-1:
        if mapp[now[0]+1][now[1]]!=2:
            now[0]+=1
            tempt.append(distance1(now,out))
            now[0]-=1
        else:
            tempt.append(10000)
    else:
        tempt.append(10000)

        
    if now[1]>0:
        if mapp[now[0]][now[1]-1]!=2:
            now[1]-=1
            tempt.append(distance1(now,out))
            now[1]+=1
        else:
            tempt.append(10000)
    else:
        tempt.append(10000)

        
    if now[1]<len(mapp[0])-1:
        if mapp[now[0]][now[1]+1]!=2:
            now[1]+=1
            tempt.append(distance1(now,out))
            now[1]-=1
        else:
            tempt.append(10000)
    else:
        tempt.append(10000)

        
    x=tempt.index(min(tempt))
    tempt.clear()
    
    return(move[x])

while(True):
    i=0
    j=0
    w=0
    determin.append(copy.deepcopy(now))
    determin1.append(copy.deepcopy(now))
    while now!=out:
        rule(choice())
        determin.append(copy.deepcopy(now))
        i+=1
        if i>100:
            break

    now=copy.deepcopy(entrance)
    mapp=copy.deepcopy(mappp)
    while now!=out:
        rule(choice1())
        determin1.append(copy.deepcopy(now))
        j+=1
        if j>100:
            break

    mapp=copy.deepcopy(mappp)

    if min(len(determin),len(determin1))==102:
        print("容量到达极限")
        break
    
    if len(determin)==min(len(determin),len(determin1)):
        print(determin)
        w=1
        for i in range(len(determin)):
            mapp[determin[i][0]][determin[i][1]]=2
        print("欧式距离")
    
    if len(determin1)==min(len(determin),len(determin1)) and w==0:
        print(determin1)
        for i in range(len(determin1)):
            mapp[determin1[i][0]][determin1[i][1]]=2
        print("曼哈顿距离")
    
    mappp=copy.deepcopy(mapp)
    
    entrance=[random.randint(0,row-1),random.randint(0,line-1)]
    out=[random.randint(0,row-1),random.randint(0,line-1)]
    now=copy.deepcopy(entrance)
    mapp[entrance[0]][entrance[1]]=1
    mapp[out[0]][out[1]]=3
    determin.clear()
    determin1.clear()


