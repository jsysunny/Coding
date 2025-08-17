user2_id, user2_level = input().split()
user2_level = int(user2_level)

# Please write your code here.
class NextLevel:
    def __init__(self,user='codetree', lv=10):
        self.user=user
        self.lv=lv

nextlevel=NextLevel()
print(f"user {nextlevel.user} lv {nextlevel.lv}" )
nextlevel=NextLevel(user2_id, user2_level)

print(f"user {nextlevel.user} lv {nextlevel.lv}" )
        