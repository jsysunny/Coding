ins=input()
ins1=input()
count=0
for i in range(len(ins)-len(ins1)+1):
    if ins[i:i+len(ins1)]==ins1:
        count+=1

print(count)