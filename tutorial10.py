#error

try:
    x=int(input("penyebut : "))
    y=int(input("pembilang : "))
    result=y/x
except ValueError:
    print("salah tipe data mas")
except ZeroDivisionError:
    print("masukin penyebut, mikir mas!")
finally:
    print("restart program nya mas!! masih salah kui!!")

if y>3:
    raise Exception("pembilang nya kebanyakan mas!")


#print(result)