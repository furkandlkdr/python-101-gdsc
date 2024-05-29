import random

print("----------------OYUNA HOŞ GELDİNİZ----------------")
print("1 ile 100 arasında bir sayı tuttum.")

tutulan_sayi = random.randint(1,100)
tahmin_sayisi = 0

while True:
    tahmin_edilen = int(input("tahminim: "))
    tahmin_sayisi += 1
    if tahmin_edilen < tutulan_sayi:
        print("YÜKSEL")
    elif tahmin_edilen > tutulan_sayi:
        print("ALÇAL")
    else:
        print("{} denemede sayiyi buldunuz!" .format(tahmin_sayisi))
        break
