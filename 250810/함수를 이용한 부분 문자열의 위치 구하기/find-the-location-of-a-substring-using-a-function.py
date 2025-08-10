text = input()
pattern = input()

# Please write your code here.
def ifind(text,pattern):
    for i in range(len(text)-len(pattern)+1):
        if text[i:i+len(pattern)]==pattern:
            return i
    else:
        return -1

print(ifind(text,pattern))