ins=input().split()
found=False
for i in range(len(ins[0])):
    if ins[0][i]==ins[1]:
        print(i)
        found=True
        break

if not found:
    print("No")
