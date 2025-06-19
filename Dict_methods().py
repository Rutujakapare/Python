## 1) get()
users = {
    'id' :10,
    'Name' :'Riya',
    'age' : 22,
    'dept' :'IT'
}
#print(users('Name'))    ## getting an error
print(users.get('Name'))   ## to avoid above error we are using get method it return actually values

## 2) keys(),values(), items()
info ={
     'name':'krish',
     'age':10,
     'dept':'core',
     'subject':'Math'
 }
print(info.keys())   ## return keys in the dictionary
print(info.values())  ## return values in the dictionary
print('name' in info.keys())    ## return true because name in present in keys in the dict
print('math' in info.values())   ## return true because math is present in the values in the dict
print(info.items())  ## return the dict


## 3) copy()
user = info.copy()   ## copy one dict to another
print(user)
print(info)

## 4) pop()
print(user.pop('dept'))  ## remove the given value
print(user)         ## removed given value
print(info)         ## but do not delete in original dict

print(user.popitem())   ## last keys-values pair removed
print(user)    ## remaining dict values  item

user.update ({'dept' : 'IT'})   ## add the item in the dict
<<<<<<< HEAD
print(user)-
=======
print(user)
>>>>>>> fa4565ec049dcc871aea40a9517e62c16732700e
