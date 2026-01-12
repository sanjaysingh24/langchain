#mutability
a = [1,2,3,4]
b = a
b.append(5)
#print(a)  #1 2 3 4 5 because b is a refrece to a same memory share

#immutability
a = "hello"
b  = a
b +='world'
print(a) # because string is immutable these are not share the same memory it create a new object