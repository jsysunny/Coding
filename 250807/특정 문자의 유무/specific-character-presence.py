str1=str(input())
first='ee' in str1
second='ab' in str1
if first:
    first="Yes"
else:
    first="No"
if second:
    second="Yes"
else:
    second="No"
print(f"{first} {second}")