import math
def null_150():
    n = 0
    while n!=150:
        n += 1
        if n % 2 == 0:
            print(n, end=", ")

def harommal_oszthato(a:int):
    n = 0
    oszt:int = 0
    while n>=10:
        a:int = int(input("Adjon meg egy számot:"))
        if a % 3 == 0:
            oszt += 1
        print (oszt)

def tizzel_oszthato():
    print("\nTízzel osztható számok bekérése")
    n = 1
    while not (n % 10 == 0):
        n:int = int(input("Adjon meg egy számot:"))
        n %= 10
    print("A szám tízzel osztható")

def ketjegyu_paros():
    print ("\n Kétjegyűnek és párosnak kell lennie a számnak")
    szam = 0
    while not (szam == 2 and n % 2 == 0):
        n:int = int(input("\nÍrjon be egy számot:"))
        szam = len(str(n))

def pozitiv_paratlan():
    print("\nAddig kéri be a számot amig nem pozitív egész")
    err = True
    while err == True:
        n:int = int(input("\nAdjon meg egy számot: "))
        if n % 2 != 0:
            if n > 0:
                err = False

def negyzetszam():
    ok = False
    while ok == False:
        n:int = int(input("\nAdjon meg egy számot: "))
        sqrt=math.sqrt(n)
        if sqrt.is_integer() == True:
            print ("negyzetszam")
            ok = True
        if n % 3 == 0:
            print ("Harommal oszthato")
            ok = True

def csak_pozitiv(): #11. feladat
    n = -1
    while n < 0:
        n:int = int(input("\nAdjon meg egy számot: "))

def atlagolas():
    szam:float = float(input("\nAdjon meg egy számot:"))
    n = 0
    atlag:float = 0
    while szam != 0: 
        atlag += szam
        n+=1
        szam:float = float(input("\nAdjon meg egy számot:"))
    print ("N érteke:",n)
    print("Átlag értéke:",atlag/n)


def harom_karakter():
    hossz = 0
    while hossz < 3:
        szoveg:str = input("\nÍrjon be egy legalább 3 karakteres szöveget: ")
        hossz = len(szoveg)
    print(szoveg.upper())
    print("Gratulálok, nyertél egy szál Lucky Strike-ot")

def kisbetu():
    kisbetu = False
    szoveg = "a"
    kis = 0
    n = -1
    while not (kisbetu == True and len(szoveg) >= 4):
        szoveg:str = input("\nÍrjon be egy legalább 4 karakteres szöveget: ")
        kisbetu = szoveg.islower()
    print("ok")
            
def atlagolas2():
    szam:float = float(input("\nAdjon meg egy számot:"))
    n = 0
    atlag:float = 0
    while szam < 0 or szam > 0 : 
        atlag += szam
        n+=1
        szam:float = float(input("\nAdjon meg egy számot:"))
        if szam < 0:
            n-=1

    print ("N érteke:",n)
    print("Átlag értéke:",atlag/n)



atlagolas2()