n = int(input())
sequence = list(map(int, input().split()))

seq = sorted(sequence)
new = []


cnt = dict()

for i in range(n):
    val = sequence[i]
    base_index = seq.index(val) + 1  
    if val in cnt:
        cnt[val] += 1
    else:
        cnt[val] = 0  

    new.append(base_index + cnt[val])

print(*new)
