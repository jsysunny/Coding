input_str = input()
target_str = input()
found=False
# Please write your code here.
for i in range(len(input_str)-len(target_str)+1):
    if input_str[i:i+len(target_str)]== target_str:
        print(i)
        found=True
        break

if not found:
    print(-1)