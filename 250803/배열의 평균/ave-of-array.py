
lista = [list(map(int, input().split())) for _ in range(2)]

for row in lista:
    print(f"{sum(row) / len(row):.1f}", end=" ")
print()


for col in range(len(lista[0])):
    col_sum = lista[0][col] + lista[1][col]
    print(f"{col_sum / 2:.1f}", end=" ")
print()


total_sum = sum(lista[0]) + sum(lista[1])
total_avg = total_sum / 8
print(f"{total_avg:.1f}")
