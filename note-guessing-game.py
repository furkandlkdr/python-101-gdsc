import colorama

colorama.init(autoreset=True)

NOTLAR = []

RENKLER = {
    "red": colorama.Fore.RED,
    "green": colorama.Fore.GREEN,
    "blue": colorama.Fore.BLUE
}

def renkleri_yazdir():
    for i,j in RENKLER.items():
        print( f"{j}{i}", end=", " )
    print()

def not_ekle():
    not_ = input("Notunuzu girin: ")
    renkleri_yazdir()
    renk = input("Rengi secin: (varsayilan = red)")

    if not renk in RENKLER:
        renk = [red]

    NOTLAR.append(
        {
        "renk": renk,
        "not": not_
        }
    )

def notlari_yazdir():
    for notlar_dict in NOTLAR:
        r = notlar_dict["renk"]
        rc = RENKLER.get(r)
        kull_not = notlar_dict.get('not')
        print(f"{rc} {kull_not}")

def menu_yazdir():
    print("""
    1- Secenekleri goster
    2- Notlari goster
    3- Not ekle
    
    0- Programdan Cik""")

menu_yazdir()
while True:
    x = int(input("> "))
    if x == 1:
        menu_yazdir()
    elif x == 2:
        notlari_yazdir()
    elif x == 3:
        not_ekle()
    elif x == 0:
        print("Program kapaniyor")
        break
    else:
        print("Boyle bir secenek yok!")
