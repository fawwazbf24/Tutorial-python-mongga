#Fawwaz Byru Fitrianto
#program tutorial function
#10-11-2020

#sesuatu yg diawali def itu adalah function

#def namafungsi(parameter):
#    blablabla
#    fawwazbyru
#    nananana

#untuk keluar function tinggal tab kebelakang aja

def luaslingkaran(r):
    luas=3.14*r*r
    return luas

print(luaslingkaran(12))

def luaslingkaran2(R):
    luass=3.14*R*R
    print(luass)

luaslingkaran2(10)

jari2=14

def luaslingkaran3(jari2):
    jari2=jari2+1
    luas3= 3.14*jari2*jari2
    return jari2

print(jari2)
print(luaslingkaran3(jari2))

def inputdata():
    x = int(input("masukkan angka : "))
    return x

def kalkulasi(x):
    y = [0,0,0]
    y[0]=x+2
    y[1]=3*x+1
    y[2]=x**2+2*x+1
    print(y)
    return y

def printdata(asal):
    for f in asal:
        print(f)

printdata(kalkulasi(inputdata()))
printdata(kalkulasi(inputdata()))

print()
print()

for f in range(10):
    print(f)
    print(-f)

print()
print()

def rumah(x):
    x=x+1
    if x<3:
        rumah(x)
    x=x+2
    print(x)

rumah(1)
