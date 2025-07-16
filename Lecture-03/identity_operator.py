a = [1,2,3]
b = a

c = [1,2,3]
d = [1,2,3]

print(a is b)  # True, because b is a reference to the same list as a
print(a is c)  # False, because c is a different list with the same content
print(c is d)  # False, because d is a different list with the same content
print(a == c)  # True, because the content of a and c is the same
print(c == d)  # True, because the content of c and d is the same 