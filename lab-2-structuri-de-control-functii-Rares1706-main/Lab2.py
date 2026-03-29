# ex 1
# a = input()
# a = float(a)
#
# while a:
#     if a >= 0 and a < 5:
#         print('Reexaminare')
#         break
#     elif a >= 5 and a <= 6:
#         print('Suficient')
#         break
#     elif a > 6 and a <= 8:
#         print('Bine')
#         break
#     elif a > 8 and a <= 10:
#         print('Excelent')
#         break
#     elif a > 10 or a < 0:
#         a = input()
#         a = float(a)

# ex2
# b = input().lower()
#
# l1 = ['bine', 'frumos', 'super', 'excelent', 'minunat']
# l2 = ['urat', 'prost', 'groaznic', 'dezamagitor']
#
# x = 0
#
# for cuvant in l1:
#     if cuvant in b:
#         x += 1
#
# for cuvant in l2:
#     if cuvant in b:
#         x -= 1
#
# if x > 0:
#     print('Pozitiv')
# elif x < 0:
#     print('Negativ')
# else:
#     print('Neutru')


# ex3
# def factura(nume,**produse):
#     print(nume)
#     print(produse)
#
#     total = 0
#
#     for produs,pret in produse.items():
#         total += pret
#
#     print(total)
#
# factura("Ion",paine=5,lapte=10,cascaval=100)

# #ex4
#
# l1=[1,2,3]
#
# patrate=list(map(lambda x:x**2,l1))
# print(patrate)

# #ex 5
#
# l1=[(0, 2), (4, 3), (9, 9), (10, -1)]
#
# l1.sort(key=lambda x: x[1])
# print(l1)

# #ex6
#
# l1=[1,2,3,4,5,6,7,8,9]
#
# pare=list(filter(lambda x:x%2==0,l1))
#
# impare=list(filter(lambda x:x%2==1,l1))
#
# print(pare)
# print(impare)

# #ex7
#
# preturi=[10,None,20,None,40,None]
#
# pr=[p for p in preturi if p is not None]
#
# print(pr)

# #ex8
#
# data="2023-04-24 09:03:32.744178"
#
# anul=data[0:4]
# print(anul)
# luna=data[5:7]
# print(luna)
# ziua=data[8:10]
# print(ziua)
# ora=data[11:13]
# print(ora)

# #ex9
# def suma_liste(l1, l2):
#     rezultat = []
#
#     for a,b in zip(l1,l2):
#         suma=a+b
#         rezultat.append((a,b,suma))
#
#     return rezultat
#
# l1=[1,2,3,4,5,6]
# l2=[1,2,3,4,5,6]
#
# print(suma_liste(l1,l2))

# #ex10
#
# pare=[x for x in range(101) if x%2==0]
# print(pare)
#
# cuburi=[n**3 for n in range(1,11)]
# print(cuburi)
#
# l1=[1,2,3,4,5,6,7,8,9,10]
# l2=[2,4,6,8]
#
# comune=[x for x in l1 if x in l2]
# print(comune)

# #ex11
#
# pare={x for x in range(0,20,2)}
# print(pare)
#
# text="hipopotam"
#
# litere={lit for lit in text if lit.isalpha()}
# print(litere)
#
# cuvinte="Invat python acum"
#
# set_cuvinte={cuv for cuv in cuvinte.split() if len(cuv)>=5}
# print(set_cuvinte)

# #ex12
#

# patrate={x:x**2 for x in range(1,11)}
# print(patrate)
#
# text="hipopotam"
#
# frecventa={litera:text.count(litera) for litera in text if litera.isalpha()}
# print(frecventa)
#
# divizori={n:[d for d in range(1,n+1)if n%d ==0]for n in range(1,11)}
#
# print(divizori)
