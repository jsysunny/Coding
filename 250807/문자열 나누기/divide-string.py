n=int(input())
lista=input().split()

str_all="".join(lista)

for i in range(0,len(str_all),5):
    print(str_all[i:i+5])