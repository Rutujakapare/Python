# 1)append()
names = ['rutuja','rohit','saurabh','avinash','akash']
names.append('akanksha')
print(names)

#2)extend()
basket1 = ['a','b','c','d']
basket2 =['a','f','a','h']
basket1.extend(basket2)
print(basket1)

#3)count()
print(basket1.count('a'))

#4)copy()
new_basket = basket1.copy()
print(new_basket)

#5)index()
print(new_basket.index('b'))

#6)insert()
new_basket.insert(2,'rutu')
print(new_basket)

#7)remove()
new_basket.remove('b')
print(new_basket)

#8)reverse()
new_basket.reverse()
print(new_basket)

#9)sort()
new_basket.sort()
print(new_basket)

#10)pop()
new_basket.pop(7)
print(new_basket)

#11)clear()
new_basket.clear()
print(new_basket)