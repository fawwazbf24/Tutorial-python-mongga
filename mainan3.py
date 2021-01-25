from soal import *

promt_soal=[
    "1. siapa yang laki-laki? \n a. fawwaz \n b. bunga \n c. nisa",
    "2. apa warna kesukaan asep? \n a. merah \n b. biru \n c. ungu",
    "3. 1+1 = \n a. 2 \n b. 3 \n c. 4"
]

pertanyaan=[
    soal(promt_soal[0],"a"),
    soal(promt_soal[1],"b"),
    soal(promt_soal[2],"a")
]

score=0
for f in pertanyaan:
    jawaban=input(f.soal + "\n")
    if jawaban==f.jawaban:
        score+=1

print(score)
