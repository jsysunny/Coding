product_name, product_code = input().split()
product_code = int(product_code)

# Please write your code here.

class Product:
    def __init__(self, name='', code=0):
        self. name= name
        self.code= code

p1=Product()

p1.name= 'codetree'
p1.code=50

print(f"product {p1.code} is {p1.name}")

p2=Product()

p2.name= product_name
p2.code=product_code

print(f"product {p2.code} is {p2.name}")