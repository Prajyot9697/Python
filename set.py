#Set - collection of unique element
# sets displayed only unique values
# set doesnt have indexing
# represented by curley bracket
# element cannot be updatedd in sets

# s={10,20,'abc',45.6}
# print(s)

# s1=set()
# print(type(s1))

# add elements in set
# s={10,20,'abc',45.6}
# s.add('itvedant') #'add' add the element at the start of set
# print(s)

# s.update(range(100,106)) #update add the element at the start of set
# print(s)


# t=('a','b','c')
# s.update(t)
# print(s)

#Delete the element
s={10,20,'abc',45.6}
# print(s.pop())
# print(s)

# s.remove(10)
# print(s)

# s.discard(45.6)
# print(s)

# s.clear()
# print(s)


s={1,2,3,4}
s1={2,4,6}

print(s.union(s1))
print(s.intersection(s1))
print(s.difference(s1))