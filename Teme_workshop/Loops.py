"""
1. Scrie un program care afiseaza primii 7 multiplii
a lui 7.

HINT: for loop + if + break
Expected Output: 0 7 14 21 28 35 42 49
"""
# multipli = ''
# for i in range(8):
#       x = 7 * i
#       multipli += str(x)
#       multipli += ' '
# print(multipli)
# result = []
# for i in range(100):
#       y = i * 7
#       if y % 7 == 0:
#             result.append(y)
#             result.count(7)
#       i += 1
#       break
# print(result)

# res1 = ""
# y = 0
# for i in range(1, 1000):
#     if y == 7:
#         break
#     if i % 7 ==0:
#         res1 += str(i) + " "
#         y += 1
# print(res1)

"""
2. Scrie o functie care adauga patratul fiecarui numar
intr-o noua lista si afiseaz-o.

Aceasta functie va primi ca parametru o lista.

Example input: [2, 3, 4]
Expected output: [4, 9, 16]
"""
# def multiply(a, b, c):
#     d = [a, b, c]
#     print(d)
#     for i in range(len(d)):
#         d[i] = d[i]*d[i]
#         i +=1
#     print(d)
# multiply(2, 3, 4)

"""
3. Scrie o functie care primeste ca paremtru o lista
de numere intregi.

Separa numerele pozitive de cele negative si returneaza-le.

Apeleaza functia cu diferite argumente si afiseaza rezultatul
conform exemplului de mai jos:

Example input: [1, 2, 5, -2, 3, -5]
Expected output:
Positive: [1, 2, 5, 3]
Negative: [-2, -5]
"""
# def numere_naturale(a, b, c, d, e, f):
#     numere = [a, b, c, d, e, f]
#     p = []
#     n = []
#     for x in range(len(numere)):
#         if numere[x] >= 0:
#             p.append(numere[x])
#         else:
#             n.append(numere[x])
#         x += 1
#     print(p)
#     print(n)
# numere_naturale(-3, -4, 0, 6, 7, 5)

"""
4. Scrie o functie care calculeaza factorialul unui numar natural
pozitiv luat ca si parametru si returneaza rezultatul.

Example input: 6
Expected output: 720
"""

# def factorial(a):
#     x = 1
#     for i in range(1, a+1):
#         x = x * i
#         i += 1
#     print(x)
# factorial(6)