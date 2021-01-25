#Fawwaz Byru Fitrianto
#program tutorial dictionaries, for loops, if.. else, dan while loops
#3-11-2020

#kondisi awal pada python pasti True
#semua angka, huruf, true kecual null
#pass untuk skip
#break untuk keluar loop

if 3>2:
    print("benar")
elif 3>4:
    print("bad")
else:
    print(salah)

a = 2
b = 330
print("A") if a > b else print("B")

if 3>2:
    print("A")
else:
    print("B")
print()

is_tall=True
is_heavy=True

if is_tall and is_heavy:
    print("big")
elif is_tall and not(is_heavy):
    print("Tall")
elif not (is_tall and is_heavy):
    print("small")
elif not(is_tall) or is_heavy:
    print("human")
else:
    print("random")

a = "aiueo"
b = "a"
if b in a:
    print("yes")
