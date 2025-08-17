n = int(input())
sequence = list(map(int, input().split()))

# Please write your code here.
seq=sequence.copy()
seq.sort()
new=[]
for i in range(n):
    if seq.index(sequence[i])+1 in new:
        new.append(seq.index(sequence[i])+2)
    else:
        new.append(seq.index(sequence[i])+1)
for n in new:
    print(n, end=" ")