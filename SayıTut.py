import time
import os


def geriyesay(rakam):
    while rakam > 0:
        print("     {}".format(rakam))
        time.sleep(1)
        rakam -= 1
    print("     {}".format(0))


def gec():
    print()
    print("     Hatalı Girdiniz!")
    print("     Menüye yönlendiriliyorsunuz...")
    time.sleep(3)


def bolme():
    os.system("cls")
    while True:
        print()
        print("Sonucu 9'a böl!")
        try:
            bolum = int(input("Tam bölünebilir ya da bölünmeyebilir... Bölüm kaç çıktı: "))
            print("Tuttuğun sayı hesaplanıyor lütfen bekle...")
            time.sleep(3)
            return bolum
        except:
            print("Hatalı girdiniz!")


def problem():
    sayi1 = 0
    bolum = 0
    os.system("cls")
    print()
    print("     Şimdi sayıyı 3 ile çarp!")
    print("     Sonra 2'ye böl!")
    input("     Devam etmek için 'Enter'e bas!")

    while True:
        print()
        secil1 = input("    Sonuç buçuklu mu? Buçuklu ise '1'e bas değilse '0'a bas! ")
        print()
        if secil1 == "1":
            sayi1 += 1
            print("     Sonuç buçukluysa sonucu üst sayıya yuvarla... 'örneğin sonuç 5.5 ise 6 ya yuvarlarsın'")
            input("     Devam etmek için 'Enter'e bas!")
            break
        elif secil1 == "0":
            sayi1 += 0
            break
        else:
            print("     Hatalı Girdiniz!")

    os.system("cls")
    print()
    print("     Şimdi sayıyı yine 3 ile çarp!")
    print("     Sonra 2'ye böl!")
    input("     Devam etmek için 'Enter'e bas!")

    while True:
        print()
        secil2 = input("    Sonuç buçuklu mu? Buçuklu ise '2'e bas değilse '0'a bas! ")
        print()
        if secil2 == "1":
            sayi1 += 2
            print("     Sonuç buçukluysa sonucu üst sayıya yuvarla... 'örneğin sonuç 5.5 ise 6 ya yuvarlarsın'")
            input("     Devam etmek için 'Enter'e bas!")
            break
        elif secil2 == "0":
            break
        else:
            print("     Hatalı Girdiniz!")

    os.system("cls")
    while True:

        print()
        print("     Sonucu 9'a böl!")
        try:
            bolum = int(input("     Tam bölünebilir ya da bölünmeyebilir... Bölüm kaç çıktı: "))
            print("     Tuttuğun sayı hesaplanıyor lütfen bekle...")
            time.sleep(3)
            break
        except:
            print("     Hatalı girdiniz!")

    os.system("cls")
    print()
    geriyesay(3)
    print()
    print("     Tuttuğun sayı = ", (bolum * 4) + sayi1)


while True:
    os.system("cls")
    print()
    AD = input("    Adınız: ")
    while True:
        print("""
            |Aklından Bir Sayı Tut Oyununa Hoş Geldin {}!|
        [1] Oyuna başlamak için
        [2] Çıkış""".format(AD))
        sec = input("   Seçiminiz: ")
        if sec == "1":
            print(" Oyun açılıyor...")
            geriyesay(3)
            os.system("cls")
            print()
            print("     0'dan büyük bir sayı tut!")
            input("     Tuttuysan 'Enter'e bas...")
            problem()
            print("     Nasılda bildim ama :)")
            input("     Ana menüye dönmek için 'Enter'e bas! ")
            break
        elif sec == "2":
            print()
            print("     Çıkış Yapılıyor...")
            time.sleep(3)
            exit()
        else:
            gec()