abilities = list(map(int, input().split()))

# Please write your code here.
mina = float("inf")
def diff(i,j,k):
    sum1= abilities[i]+abilities[j]+abilities[k]
    sum2= sum(abilities)-sum1
    return abs(sum1-sum2)

for i in range(6):
    for j in range(i+1,6):
        for k in range(j+1,6):
            mina=min(mina, diff(i,j,k))
print(mina)
