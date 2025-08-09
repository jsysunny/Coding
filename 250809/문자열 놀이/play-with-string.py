ins= input().split()
ins1=list(ins[0])
#print(ins1)
for _ in range(int(ins[1])):
    qns= input().split()
    #print(qns)

    if qns[0]=='1':
        temp=ins1[int(qns[2])-1]
        ins1[int(qns[2])-1]=ins1[int(qns[1])-1]
        ins1[int(qns[1])-1]=temp
        print(''.join(ins1))
    
    if qns[0]=='2':
        for i in range(len(ins1)):
            if ins1[i]==qns[1]:
                ins1[i]=qns[2]
        print(''.join(ins1))