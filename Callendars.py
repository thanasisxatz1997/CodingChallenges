
C1=[['9:00','10:30'],['12:00','13:00'],['16:00','18:00']]
B1=['9:00','20:00']
C2=[['10:00','11:30'],['12:30','14:30'],['14:30','15:00'],['16:00','17:00']]
B2=['10:00','18:30']
limit=30

a1=[]
a2=[]
res=[]
availTimes=[]
B1
boundL=max(int(B1[0].split(':')[0])*60+int(B1[0].split(':')[1]),int(B2[0].split(':')[0])*60+int(B2[0].split(':')[1]))
boundU=min(int(B1[1].split(':')[0])*60+int(B1[0].split(':')[1]),int(B2[1].split(':')[0])*60+int(B2[0].split(':')[1]))
for i in range(0,1440):
    res.append(0)
    a1.append(0)
    a2.append(0)

for i in range(boundL,boundU):
    res[i]=0
    a1[i]=1
    a2[i]=1

zCount=0
for meeting in C1:
    startB = int(meeting[0].split(':')[0]) * 60 + int(meeting[0].split(':')[1])
    stopB = int(meeting[1].split(':')[0]) * 60 + int(meeting[1].split(':')[1])
    print('StartBound for 1', startB)
    print('StopBound for 1', stopB)
    for i in range(startB,stopB):
        print('ZERO ADDED')
        zCount+=1
        a1[i]=0
print('zCount for 1',zCount)
print('A1 has ',a1.count(0))
zCount=0
for meeting in C2:
    startB=int(meeting[0].split(':')[0])*60+int(meeting[0].split(':')[1])
    stopB=int(meeting[1].split(':')[0])*60+int(meeting[1].split(':')[1])
    print('StartBound for 2', startB)
    print('StopBound for 2', stopB)
    for i in range(startB,stopB):
        zCount+=1
        a2[i]=0
print('zCount for 2',zCount)
print(a1[boundL:boundU])
print(a2[boundL:boundU])
print('A2 has ',a2.count(0))
print('RES:::')
print(res)
for i in range(0,1440):
    if (a1[i]==1 and a2[i]==1):
        res[i]=1

print(res[boundL:boundU])
count=0
startTime=0
for i in range(boundL,boundU):
    if res[i]==1:
        count+=1
        if count==limit:
            availTimes.append([startTime,i])
            count=0
            startTime=i+1
    else:
        count=0
        startTime=i+1

print(availTimes)
availTimesS=[]
for time in availTimes:
    startT=time[0]
    startH=startT//60
    startM=startT-startH * 60
    startTS=str(startH)+':'+str(startM)
    stopT = time[1]
    stopTH = stopT // 60
    stopTM = stopT - stopTH * 60+1
    stopTS = str(stopTH) + ':' + str(stopTM)
    availTimesS.append([startTS,stopTS])
print(availTimesS)
