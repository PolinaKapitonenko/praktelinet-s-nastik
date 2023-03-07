# Функция для чтения данных из файла и возврата в виде списка
from random import choice


def luge_fail(faili_nime):
    with open(faili_nime, "r", encoding="utf-8-sig") as f:
        data = [line.strip() for line in f]
    return data

# Функция для записи данных в файл
def kirjuta_fail(faili_nime, data):
    with open(faili_nime, "w", encoding="utf-8") as f:
        f.write("\n".join(data))

# Функция перевода с русского на эстонский и наоборот
def tõlgi_sona(sõna, mis_keelest, mis_keele, dictionary):
    if mis_keelest == "rus" and mis_keele == "est":
        key = sõna.lower()

def Teadmiste_kontroll(rus:list,est:list):
    """
    """
    kokku=int(input("Mitu küsimust?"))
    for i in range(kokku):
         järjend=choice(rus,est)
         sõna=choice(järjend)
         print(f"{sõna} - ", end="")
         tõlke=input()
         if sõna in rus:
             i=rus.index(sõna)
             tõlke_kontroll=est[i]
         elif sõna in est:
             i=est.index(sõna)
             tõlke_kontroll=rus[i]
         if tõlke==tõlke_kontroll:
             p+=1
             print("õige")
         else:
             print("Vale")
    p=5
    if (p/kokku)*100>90:
        hinne=5
    elif (p/kokku)*100>75:
        hinne=4
    elif (p/kokku)*100>60:
        hinne=3
    else:
        hinne="Väga halb!"
    return hinne
        