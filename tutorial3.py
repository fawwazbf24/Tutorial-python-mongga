#Fawwaz Byru Fitrianto
#program tutorial lists, tuples dan sets
#2-11-2020

a=[[1,2,3],[4,5,6],[7,8,9]]
print(a)
print()

c=["test","echo",2,3,4,5,"reverb"]
d=["1,2,3,4",5,6]
e=list("rumah")

print(c)
c[3:5]=["new","home"]
print(c)
print(d)
print(e)
print()

f=[13,24,56,456,24.7,99]
f.sort()
print(f)
f.sort(reverse=True)
print(f)
print()

g=c+d
print(g)
c.append(d)
print(c)
c.pop()
print(c)
print(f)
f.pop(3)
print(f)
f.insert(3,"pohon")
print(f)
print()

list1=[1,2,3,4]
list2=list1
print(list2)
list2=list1.copy()
print(list2)
list1.pop()
print(list1)
print()

newlist=["home",1,2,3,4,"home",5,6]

for h in newlist:
    print(str(h) + "\n")
newlist.remove("home")
print(newlist)
g=newlist.count("home")
print(g)
print()

tuple=[1,2,3,4]
print(tuple)
print()

set={"apel", "pisang", "melon"}
print(set)
print()

x = int(input("berapa anak kambing saya :"))
print(x)

