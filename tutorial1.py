#Fawwaz Byru Fitrianto
#program tutorial tipe data
#2-11-2020

a="hello world"
b=24
c=2.4
d= [2,4,6,"E","r",24]
e=(1,3,5,7,"P")
f={ "F" : 42, "m" : 9}
g= True
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print()

h="hello guys"
i=list(h)
print(i), print(h[6]), print(h[1:7]), print(h[:5]), print(h[5:])
print(h), print(h)
print()

j="""hello
     guys
my name is fawwaz
"""
k="hello \nworld"
kk=list(k)
print(j), print(k), print(kk)
print()

aa="hello"
bb=" world"
print(aa+bb)
print(len(aa+bb))
print(dir(str))
print(aa.capitalize())
print(len(aa.capitalize()))
print(aa.upper())
print(aa.upper().isupper())
print()

cc="Nama saya asep saya suka bambang"
print(cc)
cc=cc.replace("asep","dono",1)
print(cc)
cc=cc[0:10]+"dono"+cc[14:]
print(cc)
print()

v="   hello world  "
v=v.strip()
w=v.split(" ")
print(v)
print(w)
print()

r="nama saya {} umur saya {} tahun berat saya {} Kg"
r=r.format("fawwaz",21,57)
q="nama saya {nama} umur saya {umur} tahun berat saya {berat:.3f} Kg"
q=q.format(nama="fwz",umur="21",berat=57.123456)
print(r), print(q)