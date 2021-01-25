#Fawwaz Byru Fitrianto
#program tutorial dictionaries, for loops, if.. else, dan while loops
#3-11-2020

dict= {
    "Nama" : "fawwaz",
    "usia" : 21,
    "teman":["raihan","alzi"]
}
dict["hewan kesukaan"]="kucing"

#print(dict)
#print(dict.keys())
#print(dict.values())
#print(dict.items())
#print()
#print(dict["Nama"])
#print(dict.get("Nama2","none"))
#print()
#list=[1,2,3,4,5]
#list.append(6)
#print(list)

print(dict.values())
for f in dict.values():
    print(f)
for a in "saya manusia":
   if a in "aiueo":
       print(a)
print()
print()

kata="saya manusia"
tes2=list(kata)
print(tes2)

for g in range(len(kata)):
    print(kata[g:])
print()

indeks=0
while indeks < len(kata):
    print(kata[indeks])
    indeks += 1
print()

for a in range(10):
    print("a")
    for b in range(5):
        print("b")
        if b == 2:
            break

