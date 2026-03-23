
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


#ex3
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

#ex4

l1=[1,2,3]

lambda x:x**2,l1


