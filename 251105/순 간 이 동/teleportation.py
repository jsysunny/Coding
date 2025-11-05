a, b, x, y = map(int, input().split())

direct = abs(a - b)
shortcut1 = abs(a - x) + abs(y - b)
shortcut2 = abs(a - y) + abs(x - b)

print(min(direct, shortcut1, shortcut2))