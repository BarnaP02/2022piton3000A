lista = []

with open("input.txt", "r", encoding="utf8") as f:
    for szam in f:
        lista.append(szam)


"""
C#-ban ugyanaz

using (f = StreamReader("input.txt" , Encoding.UTF8))
{

}
"""

print("A fájl bezárva, a lista beolvasni")

print(f'1. Hány eleme van a sorozatnak? {len(lista)}')


def van_negativ_szam(l):
    for elem in lista:
        if elem < 0:
            return True
        return False

print(f'2. Van-e a sorazatban negatív szám? {"van" if van_negativ_szam(lista) else "nincs"}')

# nem túl pitonikus
i = 0
while (i < len(lista) and not lista[i]<0):
    i+=1
print('van' if i<len(lista) else 'nincs')

    # C#, C++, C
    #print( i<len(lista) ? 'van' : 'nincs')



db = 0
for elem in lista:
    if elem%2==0:
        db+=1


print(f'3. Hány páros szám található a sorozatban?{db}')

print(len(list(len(filter(lambda x : x%2==0, lista)))))