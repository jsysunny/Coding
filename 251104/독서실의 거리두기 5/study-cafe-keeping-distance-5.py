N = int(input())
seat = input()

new=[]
# Please write your code here.
for i,ch in enumerate(seat):
    if ch=="1":
        new.append(i)
#print(new)

tmaxa=0
for i in range(N):
    if i not in new:
        temp=new+[i]
        temp.sort()
        mina=float("inf")
        for j in range(1,len(temp)):
            #print(temp[i]-temp[i-1])
            mina= min(mina, abs(temp[j]-temp[j-1]))
            #print(maxa)
        tmaxa=max(tmaxa,mina)
print(tmaxa)        