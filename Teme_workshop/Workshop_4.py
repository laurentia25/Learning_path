# 1.Funcție care să calculeze și să returneze suma a două numere

# def suma(a, b):
#     return a + b
# print(suma(3, 5))
# print(suma(17, 2))

# 2. Funcție care să returneze TRUE dacă un număr este par, FALSE pentru impar

# def numar_par(a):
#     if  a % 2 != 0:
#         return FALSE
#     else:
#         return TRUE
#
# print(numar_par(5))

# 3. Funcție care returnează numărul total de caractere din numele tău complet.(nume, prenume, nume_mijlociu)


# def nume(nume, prenume, nume_milociu = ''):
#     if type(nume) == str and type(prenume) == str and type(nume_milociu) == str:
#         return len(nume+prenume+nume_milociu)
#     return -1
#
#
# # print(f'Lungimea numelui complet este {nume("Laurentia", "Vasilasco")} caractere')
# if nume(10, 20, 30) > 0:
#     print(f'Lungimea numelui complet este {nume(10, 20, 30)} caractere')
# else:
#     print('Introduceti parametri de tip string!')


# 4. Funcție care returnează aria dreptunghiului

# def aria_dreptunghiului(a, b):
#     return a * b
#
# print(f' Aria dreptunghiului este {aria_dreptunghiului(4, 5)}')

# 5. Funcție care returnează aria cercului

# def round(r):
#     import math
#     return r * math.pi
# print(round(5))

"""
6. Funcție care returnează True dacă un caracter x se găsește
într-un string dat și False dacă nu găsește.
"""
from pip._internal.utils.misc import tabulate

# def check(x, c = ''):
#     if c.find(x,0, len(c)) > 0: # parametri de lungimea stingului sunt oprionali
#         return True
#     return False
#
# print(f'Caracterul exista in string: {check("a", "abct")}')

'''7. Funcție fără return, primește un string și printează pe ecran:
Numărul de caractere lower case este x
Numărul de caractere upper case exte y '''


# def verificare(prop):
#     litere_mici = []
#     litere_mari = []
#
#     for a in range(len(prop)):
#         if prop[a].islower():
#             litere_mici.append(prop[a])
#         else:
#             litere_mari.append(prop[a])
#     print(f'Avem {len(litere_mari)} litere mari in string')
#     print(f'Avem {len(litere_mici)} litere mici in string')
#
# verificare('AvDnTomY')

'''8. Funcție care primește o LISTĂ de numere și returnează o LISTĂ doar cu numerele pozitive.'''


# def num_pozitive(list):
#     plus = []
#     for a in range(len(list)):
#         if list[a] >= 0:
#             plus.append(list[a])
#     print(f'Numerele pozitive sunt {plus}')
#
#
# num_pozitive([1, 2, 5, -3, -6])

'''9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZĂ
Primul număr x este mai mare decat al doilea număr y
Al doilea număr y este mai mare decat primul număr x
Numerele sunt egale. '''


# def compare_numbers(x, y):
#     if x > y:
#         print(f'{x} este mai mare decat {y}')
#     elif x < y:
#         print(f'{y} este mai mare decat {x}')
#     else:
#         print(f'Numerele sunt egale')
#
#
# compare_numbers(4, 6)
# compare_numbers(3, 4)
# compare_numbers(2, 2)

'''10. Funcție care primește un număr și un set de numere.
Printează ‘am adaugat numărul nou în set’ + returnează True
Printează ‘nu am adaugat numărul în set. Acesta există deja’ + returnează False'''


# def update_set(a, abc):
#     if a in abc:
#         print('nu am adaugat numărul nou în set')
#         return False
#     else:
#         print('am adaugat numărul nou în set')
#         abc.add(a)
#         return True
#
#
# update_set(2, {5, 3, 4})


'''11. Funcție care primește o lună din an și returnează câte zile are acea lună.'''

# import calendar
#
# def zile_luna(luna):
#     numar_luna = {'Ianuarie': 1, 'Februarie': 2, 'Martie': 3, 'Aprilie': 4, 'Mai': 5, 'Iunie': 6,
#                   'Iulie': 7, 'August': 8, 'Septembrie': 9, 'Octombrie': 10, 'Noiembrie': 11, 'Decembrie': 12}
#
#     if luna not in numar_luna:
#         return 'Luna introdusa este invalida'
#     else:
#         numar_zile = calendar.monthrange(2023, numar_luna[luna])[1]
#         return numar_zile
#
# print(zile_luna('Februarie'))

'''12. Funcție calculator care să returneze 4 valori. Suma, diferența, înmulțirea, împărțirea a două numere.

În final vei putea face:
a, b, c, d = calculator(10, 2)
print("Suma: ", a)
print("Diferenta: ", b)
print("Inmultirea: ", c)
print("Impartirea: ", d)'''


# def calculator(x, y):
#     a = x + y
#     print(f'Suma: {a}')
#     b = x -y
#     print(f'Diferenta: {b}')
#     c = x * y
#     print(f'Inmultirea: {c}')
#     d = x / y
#     print(f'Impartirea: {d}')
#
#
# calculator(4, 2)


'''13. Funcție care primește o listă de cifre (adică doar 0-9) 
Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
Returnează un DICT care ne spune de câte ori apare fiecare cifră
=> dict {
0: 0
1 :2
2: 0
3: 1
4: 0
5: 3
6: 0
7: 2
8: 0
9: 1
}'''

#
# def count_number(x):
#     dictionary = {}
#     for i in range(0, 9):
#         dictionary[i] = x.count(x[i])
#         i += 1
#     return dictionary
#
#
# print(count_number([1, 2, 3, 4, 5, 6, 4, 3, 2, 1]))
#
# def item_count(my_list):
#     dicti = {
#         '0': 0,
#         '1': 0,
#         '2': 0,
#         '3': 0,
#         '4': 0,
#         '5': 0,
#         '6': 0,
#         '7': 0,
#         '8': 0,
#         '9': 0
#     }
#     for item in dicti.keys():
#         dicti[item] = my_list.count(int(item))
#     return dicti
#
# print(f'Dictionar: {item_count([0, 3, 2, 5, 4, 6, 7])}')

'''14. Funcție care primește 3 numere. Returnează valoarea maximă dintre ele.'''


# def comparison(a, b, c):
#     return max(a, b, c)
#
#
# print(comparison(3, 16, 34))


'''15. Funcție care să primească un număr și să returneze suma tuturor numerelor de la 0 la acel număr.
Exemplu: dacă dăm numărul 3, suma va fi 6 (0+1+2+3)'''


# def suma(a):
#     i = 0
#     b = 0
#     while i <= a:
#         b = i + b
#         i += 1
#     return b
#
#
# print(suma(4))


'''
16.Funcție care primește 2 liste de numere (numerele pot fi dublate). Returnați numerele comune.

Exemplu:
list1 = [1, 1, 2, 3]
list2 = [2, 2, 3, 4]
Răspuns: {2, 3}   '''


# def common(list1, list2):
#     list3 = set(list2).intersection((set(list1)))
#     return list3
#
#
# print(common([2, 6, 3, 4], [1, 2, 6, 3, 5]))


'''17. Funcție care să aplice o reducere de preț.
Dacă produsul costă 100 lei și aplicăm reducere de 10%. Pretul va fi 90 de lei.
Tratează cazurile în care reducerea e invalidă. De exemplu o reducere de 110% e invalidă.'''


# def discount(price, off):
#     if off > 100:
#         return f'Introduceti un discount valid!'
#     else:
#         new_price = price - price * off / 100
#         return new_price
#
#
# print(discount(100, 110))


''' 18.Funcție care să afișeze data și ora curentă din România.
(bonus: afișazăi și data și ora curentă din China)'''
# from datetime import datetime
#
#
# def timp(country):
#
#     current_time = get_current_time(country)


'''19. Funcție care să afișeze câte zile mai sunt până la ziua ta / 
sau până la Crăciun dacă nu vrei să ne zici cand e ziua ta :)
'''

# EX OOP

'''1.Clasa Cerc
    Atribute: rază, culoare
    Constructor pentru ambele atribute
    Metode:
descrie_cerc() - va PRINTA culoarea și raza
aria() - va RETURNA aria 
diametru() 
circumferinta()
'''


# class Cerc:
#
#     def __init__(self, raza, culoare):
#         self.raza = raza
#         self.culoare = culoare
#
#     def describe(self):
#         print(f'Cercul are raza de {self.raza} cm si culoarea este {self.culoare}.')
#
#     def aria(self):
#         import math
#         return math.pi * self.raza * self.raza
#
#     def diametru(self):
#         return 2 * self.raza
#
#     def circumferinta(self):
#         return 2 * math.pi * self.raza
#
#
# cerc1 = Cerc(3, 'rosu')
# cerc1.describe()
# print(cerc1.aria())
# print(cerc1.diametru())
# print(cerc1.circumferinta())


'''2. Clasa Dreptunghi
     Atribute: lungime, lățime, culoare
     Constructor pentru toate atributele
     Metode:
descrie()
aria()
perimetrul()
schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic.
Ea va lua ca și parametru o nouă culoare și va suprascrie atributul self.culoare.
Poți verifica schimbarea culorii prin apelarea metodei descrie().'''


# class Rectangle:
#     long = 10
#     lat = 5
#     color = 'red'
#
#     def __init__(self, color, long, lat):
#         self.color = color
#         self.long = long
#         self.lat = lat
#
#
#    def describe(self):
#        # print(f'Dreptunghiul este de culoare {c}')
#     def area(self):
#         return self.long * self.lat
#
#     def perimeter(self):
#         return (self.long + self.lat) * 2
#
#     def change_color(self, new_color):
#         self.color = new_color
#
#
# rectangle1 = Rectangle('blue')
# rectangle2 = Rectangle('red')
# print(f'Dreptunghiul are aria de {rectangle1.area()} cm2')
# print(rectangle1.perimeter())
# print(rectangle1.color)
#
# print(rectangle2.area())
# print(rectangle2.perimeter())
# print(rectangle2.color)

# class Dreptunghi:
#     lungime = None
#     latime = None
#     culoare = 'blue'
#
#     def __init__(self, lungime, latime, culoare):
#         self.lungime = lungime
#         self.latime = latime
#         self.culoare = culoare
#
#     def descriere(self):
#         print(f'Acest dreptunghi are o lungime de {self.lungime} si o latime de {self.latime}.
#         Culoarea lui este{self.culoare}')
#
#     def area(self):
#         return self.lungime * self.latime
#
#     def perimetru(self):
#         return 2 * (self.lungime + self.latime)
#
#     def change_color(self, new_color):
#         self.culoare = new_color
#
#
# dreptunghi = Dreptunghi(12, 13, 'green')
# dreptunghi.change_color('greem')
# print(f'Aria dreptunghiului este {dreptunghi.area()}')
# dreptunghi.descriere()
# print(f'perimetrul este {dreptunghi.perimetru()}')
#
# print(dreptunghi.area())

'''3. Clasa Angajat
     Atribute: nume, prenume, salariu
     Constructor pentru toate atributele
     Metode:
descrie()
nume_complet()
salariu_lunar()
salariu_anual()
marire_salariu(procent)'''


# class Angajat:
#     def __init__(self, nume, prenume, salariu):
#         self.nume = nume
#         self.prenume = prenume
#         self.salariu = salariu
#
#     def describe(self):
#         print(f'Angajatul {self.nume} {self.prenume} are salariul de {self.salariu} de lei')
#
#     def nume_complet(self):
#         return f'{self.nume} {self.prenume}'
#
#     def salariu_lunar(self):
#         return f'Salariul lunar este de {self.salariu} de lei'
#
#     def salariu_anual(self):
#         return f'Salariul anual este de {self.salariu * 12} de lei'
#
#     def marire_salariu(self, salariul_nou):
#         self.salariul_nou = salariul_nou
#         procent_marire = (self.salariul_nou * 100 / self.salariu)-100
#         return f'Salariul a fost marit cu {procent_marire} %'
#
#
# angajat1 = Angajat('Ion', 'Vasile', 1000)
# angajat1.describe()
# print(angajat1.nume_complet())
# print(angajat1.salariu_lunar())
# print(angajat1.salariu_anual())
# print(angajat1.marire_salariu(1500))

'''4. Clasa Cont
   Atribute: iban, titular_cont, sold
   Constructor pentru toate atributele
   Metode:
afisare_sold() - Titularul x are în contul y suma de n lei
debitare_cont(suma)
creditare_cont(suma)'''


# class Cont:
#     def __init__(self, iban, titular_cont, sold, suma=0):
#         self.iban = iban
#         self.titular_cont = titular_cont
#         self.sold = sold
#         self.suma = suma
#
#     def afisare_sold(self):
#         return f'Titularul {self.titular_cont} are în contul {self.iban} suma de {self.sold} lei'
#
#     def debitare_cont(self):
#         return f'Titularul {self.titular_cont} are în contul {self.iban} suma de {self.sold - self.suma} lei'
#
#     def creditare_cont(self):
#         return f'Titularul {self.titular_cont} are în contul {self.iban} suma de {self.sold + self.suma} lei'
#
#
# cont1 = Cont(12345, 'Popescu Vasile', 300, 30)
# print(cont1.afisare_sold())
# print(cont1.debitare_cont())
# print(cont1.creditare_cont())


''' 5. Clasa Factură
     Atribute: seria (va fi constantă, nu trebuie constructor, toate facturile vor avea aceeași serie), 
     număr, nume_produs, cantitate, pret_buc
     Constructor: toate atributele, fără serie
     Metode:
schimbă_cantitatea(cantitate)
schimbă_prețul(pret)
schimbă_nume_produs(nume)
generează_factura() - va printa tabelar dacă reușiți

Factura seria x număr y
Data: generează automat data de azi
Produs | cantitate | preț bucată | Total 
Telefon |      7       |       700       | 49000     
 '''

class Factura:
    SERIE = 'ABC'

    def __init__(self, numar, nume_produs, cantitate, pret_buc):
        self.numar = numar
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_buc = pret_buc

    def schimba_cantitatea(self, new_cantitate):
        self.new_cantitate = new_cantitate
        self.cantitate = self.new_cantitate
        return self.cantitate

    def schimba_pretul(self, new_price):
        self.new_price = new_price
        self.pret_buc = self.new_price
        return self.pret_buc

    def schimbă_nume_produs(self, new_name):
        self.new_name = new_name
        self.nume_produs = self.new_name
        return self.nume_produs


factura1 = Factura(12, 'rosii', 3, 2)
print(factura1.schimba_cantitatea(4))


