import modul as md
import Bubblesort as bs


a=17
a=float(21)
fawwaz=md.orang("fawwaz",21)
print(fawwaz.nama)
print(fawwaz.umur)
fawwaz.jalan()
fawwaz.makan()
fawwaz.umurs("alzi")

print()

asep = md.orangtua("asep",99,105)
print(asep.nama)
asep.jalan()
asep.sakit()
asep.makan()

print()

komunitas=md.orangorang("fawwaz","byru","fitrianto")
print(komunitas.arg)
for f in komunitas.arg:
    print(f)

#a=1
#b=2
#print(modul.penjumlahan(a,b))

#x = [1,23,45,643,12,23,15,44,10]
#print(bs.bubblesort(x))

#print(md.penjumlahan(a,b))
#md.penjumlahan(a,b)
#bs.penjumlahan(a,b)