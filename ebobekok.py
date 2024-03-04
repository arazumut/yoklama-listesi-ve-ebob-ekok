def ebob_bul(sayi1, sayi2):
    while sayi2:
        sayi1, sayi2 = sayi2, sayi1 % sayi2
    return sayi1

def ekok_bul(sayi1, sayi2):
    return (sayi1 * sayi2) // ebob_bul(sayi1, sayi2)

try:
    sayi1 = int(input("Birinci sayıyı girin: "))
    sayi2 = int(input("İkinci sayıyı girin: "))

    ebob = ebob_bul(sayi1, sayi2)
    ekok = ekok_bul(sayi1, sayi2)

    print(f"{sayi1} ve {sayi2} sayılarının EBOB'u: {ebob}")
    print(f"{sayi1} ve {sayi2} sayılarının EKOK'u: {ekok}")

except ValueError:
    print("Lütfen geçerli bir sayı girin.")
