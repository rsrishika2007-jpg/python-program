a=[]
n=int(input("enter a number of elements"))
for i in range(0,n):
    m=int(input("enter  number"))
    a.append(m)
    
print(a)
print(a[0])
print(a[-1])
print(a[0:3])
print(a[-3:])
print(a[1:3])
a.extend([7,8,9])
print(a)
a.insert(4,8)
print(a)

