A = input()

# Please write your code here.
def palindrome(A):
    for i in range(len(A)):
        if A[i]!= A[len(A)-i-1]:
            return "No"
    return "Yes"

print(palindrome(A))