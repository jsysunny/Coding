n= int(input())

new=[1,n]
while True:
    new.append(new[-1]+new[-2])
    if new[-1]+new[-2]>100:
        new.append(new[-1]+new[-2])
        break
    

for n in new:
    print(n, end=" ")