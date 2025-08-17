n = int(input())
name = []
street_address = []
region = []

class Intro:
    def __init__(self, name, street_address, region):
        self.name=name
        self.street_address= street_address
        self.region= region

intro=[]
for _ in range(n):
    n_i, s_i, r_i = input().split()
    name.append(n_i)
    street_address.append(s_i)
    region.append(r_i)
    intro.append(Intro(n_i,s_i,r_i))

# Please write your code here.
name1=name.copy()
name1.sort(reverse=True)
idx= name.index(name1[0])

print(f"name {intro[idx].name}")
print(f"addr {intro[idx].street_address}")
print(f"city {intro[idx].region}")