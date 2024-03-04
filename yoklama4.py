import datetime
import os

def yoklama_al():
    ogrenci_miktarı = 25
    yoklama_listesi = {}

    for i in range(ogrenci_miktarı):
        yoklama_listesi[f"Öğrenci-{i+1}"] = datetime.datetime.now()

    print("Yoklama başladı...")

    while yoklama_listesi:
        girilen_kişi_ismi = input("Adınızı giriniz (Çıkmak için 'q' tuşuna basabilirsiniz): ")

        if girilen_kişi_ismi.lower() == 'q':
            break

        if girilen_kişi_ismi in yoklama_listesi:
            yoklama_listesi[girilen_kişi_ismi] = datetime.datetime.now()
            print(f"{girilen_kişi_ismi} yoklama alındı.")
        else:
            print(f"{girilen_kişi_ismi} listede bulunamadı. Lütfen doğru ismi giriniz.")

    with open("katildilar.txt", "w") as dosya_katildilar, open("katilmayanlar.txt", "w") as dosya_katilmayanlar:
        for ogrenci, zaman in yoklama_listesi.items():
            fark = datetime.datetime.now() - zaman
            dakika_farki = fark.seconds / 60
            if dakika_farki < 15:
                dosya_katildilar.write(f"{ogrenci}: {dakika_farki:.2f} dakika önce girdi.\n")
            else:
                dosya_katilmayanlar.write(f"{ogrenci}: {dakika_farki:.2f} dakika sonra girdi.\n")

    print("\nYoklama tamamlandı.")

yoklama_al()

if os.path.exists("katildilar.txt") and os.path.exists("katilmayanlar.txt"):
    print("Yoklama sonuçları dosyalara kaydedildi.")
else:
    print("Dosya oluşturulmadı!")
