x=float(input())
y=float(input())
z=float(input())
from math import sqrt
print(f'периметр такого трикутникак дорівнює:{x+y+z}')
print(f'площа такого трикутникак дорівнює:{sqrt((x+y+z)/2*(x+y-z)/2*(x-y+z)/2*(-x+y+z)/2)}')


x=float(input())
y=float(input())
a=[x,y]
print(a)

#6
x=float(input())
y=float(input())
z=float(input())
if x+y==z or x+z==y or z+y==x:
    print('yes')

    #7
x=float(input())
y=float(input())
z=float(input())
k=float(input())
l=[x,y,z,k]
l.sort()
def y():
    for i in[3,2,1,0]:
        if l[i]%2 == 0:
            return l[i]
    return "not found"
print(y())
