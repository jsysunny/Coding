ins=input()
ins=list(ins)
ins1=ins.copy()
# copy가 기존 꺼 안바꾸는거
#print(ins1)
for i in range(len(ins1)):
    if ins[i]==ins[1]:
        ins1[i]=ins[0]

print(''.join(ins1))