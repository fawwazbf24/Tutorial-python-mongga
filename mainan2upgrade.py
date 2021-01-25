from kelas import *

#dir=str(input("masukkan direktori file: \n"))
testfile=open("C:\\Users\\fawwa\\OneDrive\\Desktop\\file\\tesmainan.txt","r",encoding="utf 8")
print(testfile.read())

testfile.seek(0)
counts={}
for baris in testfile:
    katakata = baris.split(" ")
    for kata in katakata:
        for katabersih in ilanginsimbol(kata):
            counts[katabersih.lower()]=counts.get(katabersih.lower(),0)+1

print(counts)

kataterbanyak=str()
jumlahkata=0

for f in counts.keys():
    if counts[f]>jumlahkata:
        kataterbanyak=f
        jumlahkata=counts[f]

print(kataterbanyak,":",jumlahkata)