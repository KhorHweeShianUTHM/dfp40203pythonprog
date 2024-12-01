#Logical operators
x = False; y = True
r = x and y
print(r) # False

s =x or y
print(s) # True

x = False; y = False
t = x and y
print(t) # False

u = x or y
print(u) # False

x = True; y = True
v = x and y
print(v) # True

w =x or y
print(w)  # True

x = False
z1 = not x
print(z1) # True

x = True
z2= not x
print(z2) # False
