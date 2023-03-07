from module1 import*
laused=["Tere tulemast"]

while True:
    v=int(input("1-Funktsioon failist andmete lugemiseks ja loendina tagastamiseks\n2-Funktsioon andmete faili kirjutamiseks\n3-Tõlkefunktsioon vene keelest eesti keelde ja vastupidi\n"))
    if v==1:
        laused=luge_fail("rus.txt")
        for line in laused:
            print(line)
            laused=luge_fail("est.txt")
        for line in laused:
            print(line)
    elif v==2:
        line=input("Lisa lause: ")
        laused.append(line)
        kirjuta_fail("rus.txt",laused)
        line=input("Lisa lause: ")
        laused.append(line)
        kirjuta_fail("est.txt",laused)
    elif v==3:
        text=""
        for line in laused:
            text=text+" "+line
        tõlgi_sona(text,"et")
        ind=int(input("Number:"))
        tõlgi_sona(laused[ind],"et")

    elif v==4:
        est=["koer,kass,maja,auto,puu,raamat,inimene,laud,aken,päev"]
        rus=["собака,кошка,дом,машина,дерево,книга,человек,стол,окно,день"]
        hinne=Teadmiste_kontroll(rus,est)
        print(hinne)