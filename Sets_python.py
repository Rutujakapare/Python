'''         Sets    --- mutable/changeable
  - store different type of data.
  - it is mutable collection of data.
  - it is unordered collection of data.
  - it store unique collection of data.
  - duplicates are not allowed.
  - created using curley brackets{}.'''

My_Set = {1,2,3,4,5,'tuple'}
print(My_Set)

## list convert into set
my_list = [1,2,3,4,5,5,5,'tuple','list','set','dict']   ## after converting into set duplicated are removed.
print(set(my_list))

## Sets_methods
#1) add()
my_Sets = {1,2,3,4,5,6,7,8,9,0}
print(my_Sets.add(10))


## Sets_Methods
# 1)difference()
my_collection ={1,2,3,4,5}
your_collection = {4,5,6,7,8,9}
print(my_collection.difference(your_collection))   ## different item in the first set i.e {1,2,3,}

#2) discard()
my_collection.discard(5)   ## removed value 5 from the set.
print(my_collection)

# 3) difference_update()
my = {1,2,3,4,5}
yours = {4,5,6,7,8,9}
my.difference_update(yours)   ## difference is removed
print(my)

#4) intersection()
a={2,4,6,8,10}
b= {10,2,5,7}
print(a.intersection(b))    ## return common data from both.

##5) isdisjoint()
first = {1,2,3,4,5}
second = {6,7,8,}
print(first.isdisjoint(second))    ## in both if one of the value is common it is return false.

##6)union()
print(first.union(second))   ## return all the values in the set by removing duplicates.


##7)issubset
one ={4,5}
two = {4,5,6,7,8,9}
print(one.issubset(two))   ## first set is subset of another

##8) issuperset()
yes = {1,2,3,4,5}
No={1,2}
print(yes.issuperset(No))   ## another is superset of first



