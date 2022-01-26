import xlsxwriter

def delc(a):
    del a[:]
    del a

def listap(cislo, lista, listp):
    if cislo not in lista:
        lista.append(cislo)
        listp.append(1)
    else:
        index = lista.index(cislo)
        listp[index] += 1
    return lista, listp

def myprint(a,b):
    for i in range(len(a)):
        print(a[i], " : ", b[i])

def ltos(lista):
    st = ""
    for e in lista:
        st += str(e)
        if lista.index(e) != len(lista)-1:
            st += ", "
    return st

def sinput(xlist, seznam, pocet, sloupek):
    radek = 3
    if sloupek == 0:
        sloupek = 2
    for i in range(len(seznam)):
        s = ltos(seznam[i])
        xlist.write(radek+i, sloupek, s)
        xlist.write(radek+i, sloupek+1, pocet[i])

cisla = [[[],[]] for _ in range(49)]
ind = 0
while True:
    a = input("input :")
    if a == "0":
        break
    else:
        cisla[ind][0] = a.split("\t")[:5]
        cisla[ind][1] = a.split("\t")[5:]
        ind += 1
for i in range(len(cisla)):
    for v in range(len(cisla[i])):
        for c in range(len(cisla[i][v])):
            cisla[i][v][c] = int(cisla[i][v][c])

for i in cisla:
    for v in i:
        v.sort()

            


""" Soubor init """
radek = 2
sloupek = 2
soubor = xlsxwriter.Workbook("cisla.xlsx")
worksheet_jednotliva = soubor.add_worksheet(name = "jednotlivá čísla")
worksheet_dvojice = soubor.add_worksheet(name = "dvojice čisel")
worksheet_trojice = soubor.add_worksheet(name = "trojice čisel")
worksheet_ctverice = soubor.add_worksheet(name = "ctverice čisel")
worksheet_petice = soubor.add_worksheet(name = "petice čisel")
a = [worksheet_jednotliva, worksheet_dvojice, worksheet_trojice, worksheet_ctverice, worksheet_petice]
for l in a:
    l.write(radek, sloupek, "kombinace :")
    l.write(radek, sloupek+1, "pocet :")
    l.write(radek, sloupek+3, "kombinace +1 :")
    l.write(radek, sloupek+4, "pocet :")
    l.write(radek, sloupek+5, "kombinace +2 :")
    l.write(radek, sloupek+6, "pocet :")

"""Soubor init END"""

"""zapsat jednotliva cisla"""
for i in range(1,56):
    a[0].write(radek+i, sloupek, i)
a[0].write(radek, sloupek+7, "druha cisla :")
a[0].write(radek, sloupek+8, "pocet :")
a[0].write(radek, sloupek+9, "druha cisla kombinace :")
a[0].write(radek, sloupek+10, "pocet :")
for i in range(1,11):
    a[0].write(radek+i, sloupek+7, i)

jednotliva = [0 for _ in range(56)]
jednotliva2 = [0 for _ in range(11)]
kombinace2 = []
kombinace2p = []

cisla1 = [] #kombinace
cisla12 = [] #počet kombinací
cisla2 = [] #kombinace
cisla22 = [] #počet kombinací
for i in cisla:
    #jednotliva cisla
    for c in range(len(i)):
        if c == 0:
            for j in i[c]:
                jednotliva[j] += 1
                for v in i[1]:
                    #kombinace 1 čísla z 5tice + 1 z dvojice [5, 2]
                    cisla1, cisla12 = listap([j,v], cisla1, cisla12)
                cisla2, cisla22 = listap([j, i[1][0], i[1][1]], cisla2, cisla22)
        #jednotliva druha
        else:
            for j in i[c]:
                jednotliva2[j] +=1
        #kombinace druha
            kombinace2, kombinace2p = listap([i[c][0], i[c][1]], kombinace2, kombinace2p)

for i in range(1,len(jednotliva)):
    worksheet_jednotliva.write(radek+i, sloupek+1, jednotliva[i])

for i in range(1,len(jednotliva2)):
    worksheet_jednotliva.write(radek+i, sloupek+8, jednotliva2[i])

sinput(a[0], cisla1, cisla12, 5)
sinput(a[0], cisla2, cisla22, 7)
sinput(a[0], kombinace2, kombinace2p, 11)

    

"""DVOJICE"""
dva = []
dvap = []
dva1 = []
dva1p = []
dva2 = []
dva2p = []

for i in cisla:
    for c in range(len(i[0])-1):
        for v in range(c+1, len(i[0])):
            dva, dvap = listap([i[0][c], i[0][v]], dva, dvap)
            dva2, dva2p = listap([i[0][c], i[0][v], i[1][0], i[1][1]], dva2, dva2p)
            for k in i[1]:
                dva1, dva1p = listap([i[0][c], i[0][v], k], dva1, dva1p)
sinput(a[1], dva, dvap, 0)
sinput(a[1], dva1, dva1p, 5)
sinput(a[1], dva2, dva2p, 7)
"""TROJICE"""
tri = []
trip = []
tri1 = []
tri1p = []
tri2 = []
tri2p = []

for i in cisla:
    for c in range(len(i[0])-2):
        for v in range(c+1, len(i[0])-1):
            for b in range(v+1, len(i[0])):
                tri, trip = listap([i[0][c], i[0][v], i[0][b]], tri, trip)
                tri2, tri2p = listap([i[0][c], i[0][v], i[0][b], i[1][0], i[1][1]], tri2, tri2p)
                for k in i[1]:
                    tri1, tr1p = listap([i[0][c], i[0][v], i[0][b], k], tri1, tri1p)
sinput(a[2], tri, trip, 0)
sinput(a[2], tri1, tri1p, 5)
sinput(a[2], tri2, tri2p, 7)
"""CTVERICE"""
ctyr = []
ctyrp = []
ctyr1 = []
ctyr1p = []
ctyr2 = []
ctyr2p = []

for i in cisla:
    for c in range(len(i[0])-3):
        for v in range(c+1, len(i[0])-2):
            for b in range(v+1, len(i[0])-1):
                for j in range(b+1, len(i[0])):
                    ctyr, ctyrp = listap([i[0][c], i[0][v], i[0][b], i[0][j]], ctyr, ctyrp)
                    ctyr2, ctyr2p = listap([i[0][c], i[0][v], i[0][b], i[0][j], i[1][0], i[1][1]], ctyr2, ctyr2p)
                    for k in i[1]:
                        ctyr1, ctyr1p = listap([i[0][c], i[0][v], i[0][b], i[0][j], k], ctyr1, ctyr1p)
sinput(a[3], ctyr, ctyrp, 0)
sinput(a[3], ctyr1, ctyr1p, 5)
sinput(a[3], ctyr2, ctyr2p, 7)
"""PETICE"""
pet = []
petp = []
pet1 = []
pet1p = []
pet2 = []
pet2p = []

for i in cisla:
    pet, petp = listap(i[0], pet, petp)
    pet2, pet2p = listap([i[0][0], i[0][1], i[0][2], i[0][3], i[0][4], i[1][0], i[1][1]], pet2, pet2p)
    for k in i[1]:
        pet1, pet1p = listap([i[0][0], i[0][1], i[0][2], i[0][3], i[0][4], k], pet1, pet1p)

sinput(a[4], pet, petp, 0)
sinput(a[4], pet1, pet1p, 5)
sinput(a[4], pet2, pet2p, 7)

soubor.close()
