str= input()
lista=['apple', 'banana', 'grape', 'blueberry', 'orange']

cnt=0
for l in lista:
    if l[2]== str or l[3]== str:
        print(l)
        cnt+=1
print(cnt)