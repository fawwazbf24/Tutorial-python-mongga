#Fawwaz Byru Fitrianto
#program tutorial angka dan boolean
#2-11-2020

import math

a=24
b=24.5

print(type(a))
a=float(a)
print(a)
print(type(a))
print()

b=int(b)
print(b)
print()

c=a/b
print(int(c))
print(a is b)
print(a == b)
print()

counter=0
string = "saya suka kue coklat"
print("saya" in string)
for f in string:
    if(f=="s"):
        counter+=1
print(counter)
print()

aa=3
bb=2.0
cc=aa**bb
dd=math.pow(aa,bb)
print(cc)
print(dd)