m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
num_of_days= [0, 31, 28, 31, 30,31, 30,31, 31,30, 31, 30,31]

suma1=0
suma2=0
for i in range(len(num_of_days)):
    if i == m1:
        suma1= sum(num_of_days[:i])+d1
    if i == m2:
        suma2= sum(num_of_days[:i])+d2

print(suma2-suma1+1)

