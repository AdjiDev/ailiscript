import sys as aji
from time import sleep as turu
import random

def mengetik(teks, delaynya=0.03):
    for i in teks:
        aji.stdout.write(i)
        aji.stdout.flush()
        turu(delaynya)

def cektobrut():
    agus = input("Masukan nama untuk mengecek seberapa tobrut~# ").lower()
    brpa_tobrut = random.randint(0, 100)
    if brpa_tobrut <= 30:
        mengetik(f"{agus} {brpa_tobrut}% kecil wuuuuuuu")

    match agus:
        case "keluar":
            aji.exit()
        case "crot":
            mengetik("Ngapain ngafs", delaynya=0.05)

if __name__ == "__main__":
    cektobrut()