unlock_code, wire_color, seconds = input().split()
seconds = int(seconds)

# Please write your code here.
class Bomb:
    def __init__(self, code, color, second):
        self.code= code
        self.color=color
        self.second=second

bomb= Bomb(unlock_code, wire_color, seconds)
print(f"code : {bomb.code}")
print(f"color : {bomb.color}")
print(f"second : {bomb.second}")