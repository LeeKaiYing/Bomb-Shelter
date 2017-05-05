fruitshop = {
    "banana":{
        "price":4,
        "stock": 6},
    "apple":{
        "price": 2,
        "stock": 0},
    "orange":{
        "price": 1.5,
        "stock": 32},
    "pear":{
        "price": 3,
        "stock": 15}
    }
print(fruitshop)
total = 0
for value in fruitshop.values():
    total = total + value['price']*value['stock']

print (total)
