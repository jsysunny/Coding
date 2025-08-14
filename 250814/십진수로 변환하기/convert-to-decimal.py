binary = input()
binary=list(binary)
# Please write your code here.
num=0
for i in range(len(binary)):
    num+=int(binary[i])*(2**(len(binary)-i-1))
print(num)