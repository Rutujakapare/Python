## git patterns

print(list(range(5,101,5)))


##                     list joins
### add in space or any symbol in between the list item

sentence = ' '
new_sentence =sentence.join(['welcome','to','python','coding','practice'])
print(new_sentence)

##                       OR
print(' '.join (['welcome','to','python','coding','practice']))

##                    list unpacking
a,b,c,*other,d = [1,2,3,4,5,6,7,8,9]
print(a)
print(b)
print(c)
print ([*other])
print(d)
