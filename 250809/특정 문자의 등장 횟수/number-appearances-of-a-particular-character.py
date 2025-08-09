ins=input()
count1=0
count2=0
for i in range(len(ins)-1):
    if ins[i:i+2]=="ee":
        count1+=1
    elif ins[i:i+2]=="eb":
        count2+=1

print(f"{count1} {count2}")