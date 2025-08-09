ins=input()
ins=list(ins)
ins1=ins.copy()
for i in range(len(ins1)):
    if ins[i]==ins[0]:
        ins1[i]=ins[1]
    elif ins[i]==ins[1]:
        ins1[i]=ins[0]

print(''.join(ins1))