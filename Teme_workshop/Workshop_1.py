'''Partea 1 - Setup, Variabile, Tipuri de date

Exerciții - studiu în workshopul de weekend
1. În cadrul unui comentariu, explică cu cuvintele tale ce este o variabilă.
'''
from random import randint

# O variabila este un parametru care poate pastra valori, o cutiuta.

'''
2. Declară și initializează câte o variabilă din fiecare din următoarele tipuri de variabilă:
string
int 
float
bool
Observație: Valorile vor fi alese de tine după preferințe.
'''
# var_string = 'Variabila de tip string'
# var_int = 25
# var_float = 25.55
# var_bool = True

'''3. Utilizează funcția type pentru a verifica dacă au tipul de date așteptat.'''
# print(type(var_string))
# print(type(var_int))
# print(type(var_float))
# print((type(var_bool)))

'''4. Rotunjește ‘float’-ul folosind funcția round() și salvează această modificare în aceeași variabilă (suprascriere):
Verifică tipul acesteia.'''

# var_float = round(var_float)
# print(var_float)

'''5. Folosește print() și printează în consolă 4 propoziții folosind cele 4 variabile. 
Rezolvă nepotrivirile de tip prin ce modalitate dorești.'''

# print(f'{var_string} poate fi afisata fara modificari')
# print(f'Ciresele costa {var_float} lei')
# print(f'Maria are {var_int} de ani')
# print(f'Conditionalul if ruleaza doar daca conditia este validata ca fiind {var_bool}')

'''6. Citește de la tastatură:
numele;
prenumele.
    Afișează: 'Numele complet are x caractere'.
'''
# nume = str(input('Te rog sa introduci numele'))
# prenume = str(input('Te rog sa introduci prenumele'))
# nume_complet = len(nume) + len(prenume)
# print(f'Numele complet are {nume_complet} caractere')

'''7. Citește de la tastatură:
lungimea;
lățimea.
   Afișează: 'Aria dreptunghiului este x'.
'''
# lungime = float(input("Introduceti lungimea dreptunghiuli:"))
# latime = float(input('Introduceti latimea dreptunghiului'))
# aria = lungime * latime
# print(f'Aria dreptunghiului este {aria} cm2')

'''8. Având stringul: 'Coral is either the stupidest animal or the smartest rock':
afișează de câte ori apare cuvântul 'the' '''

coral = 'Coral is either the stupidest animal or the smartest rock'

'''9. Același string:
Afișează de câte ori apare cuvântul 'the';
Printează rezultatul.
'''

# print(coral.count(' the '))

'''10. Același string:
Folosește un assert ca să verifici dacă acest string conține doar numere.'''
# print(coral.isdigit())

'''11. Exercițiu:
citește de la tastatură un string de dimensiune impară;
afișează caracterul din mijloc.'''

# x = str(input("Te rog sa introduci un sir de caractere:"))
# while len(x)%2 == 0:
#   print('Lungimea sirului de caractere introdus trebuie sa fie numar impar!')
#   x = str(input('Te rog sa introduci din nou un sir de caractere:'))
# print(x[int((len(x)-1)/2)]) # se printeaza caracterul din mijloc

'''12. Folosind o singură linie de cod :
citește un string de la tastatură (ex: 'alabala portocala');
salvează fiecare cuvânt într-o variabilă;
printează ambele variabile pentru verificare.'''

# x, y = str(input("Te rog sa introduci un sir")).split()
# print(x)
# print(y)

'''13. Exercițiu:
citește un string de la tastatură (ex: alabala portocala);
salvează primul caracter într-o variabilă - indiferent care este el, încearcă cu 2 stringuri diferite;
capitalizează acest caracter peste tot, mai puțin pentru primul și ultimul caracter => alAbAlA portocAla.'''
#
# a = str(input("Te rog sa introduci un string"))
# b = a[0]
#
# c = a.replace(b,b.upper())
# d = a[0]+c[1:-1:]+a[-1]
# print(d)

'''14.Exercițiu:
citește un user de la tastatură;
citește o parolă;
afișează: 'Parola pt user x este ***** și are x caractere';
***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie să afișeze corect.

eg: parola abc => ***
      parola abcd => ****
'''
# user = input('Introduceti un user:')
# parola = input('Introduceti o parola')
# x = len(parola)
# y = '*'*x
# print(f'Parola pt user {user} este {y} si are {x} caractere')

########## Partea 2 - Operatori, condiționale###########
'''1. Explică cu cuvintele tale în cadrul unui comentariu cum funcționează un if else.'''
# Conditionaul if verificara daca este adevarata o conditie data si executa comenzile din cod,
# sau executa comenzile specificate daca conditia data este falsa.

#2. Verifică și afișează dacă x este număr natural sau nu.

# x = int(input('Introduceti un numar:'))
# if x >=0:
#     print(f'{x} este un numar natural')
# else:
#     print(f'{x} nu este un numar natural')

#3. Verifică și afișează dacă x este număr pozitiv, negativ sau neutru.
# if x > 0:
#     print(f'{x} este un numar pozitiv')
# elif x = 0:
#     print(f'{x} este un numar neutru')
# else:
#     print(f'{x} este un numar negativ')

#4. Verifică și afișează dacă x este între -2 și 13.
# if  x > -2 and x < 13:
#     print(f'{x} este cuprins in intervalul [-2; 13]')
# else:
#     print(f'{x} este in afara intervalului dat')

#  5. Verifică și afișează dacă diferența dintre x și y este mai mică de 5.
# y = 7
# if  x-y < 5:
#     print(f'Diferenta dintre x si y este {x-y} < 5')
# else:
#     print("Diferenta dintre x si y nu este mai mica decat 5")

# 6. Verifică dacă x NU este între 5 și 27  - a se folosi ‘not’.
# if  not x < 5 or x > 27 :
#     print(f"Numarul {x} este in intervalul [5; 27]")
# else:
#     print(f"Numarul {x} nu este in intervalul [5; 27]")

# 7.x și y (int)
# Verifică și afișează dacă sunt egale, dacă nu afișează care din ele este mai mare.
# if x==y:
#     print('Numerele sunt egale')
# else:
#     print('Numerele nu sunt egale')

# 8.
# X, y, z - laturile unui triunghi.
# Afișează dacă triunghiul este isoscel, echilateral sau oarecare.

# x = int(input('Latura triunghiului este:'))
# y = int(input('Latura triunghiului este:'))
# z = int(input('Latura triunghiului este:'))
#
# if x == y or y == z or x == z:
#     print('Triungiul este isoscel')
# elif x == y == z :
#     print("Triunghiul este echilateral")
# else:
#     print('Triunghiul este oarecare')

'''9. Citește o literă de la tastatură.
    Verifică și afișează dacă este vocală sau nu.'''
# vocale = ['a', 'e', 'i', 'o', 'u', 'ă', 'î']
# litera = str(input('Introdu o litera'))
#
# for vocala in vocale:
#     if litera == vocala :
#         print("Litera este o vocala")
#         break
# else:
#     print('Litera este o consoana')
'''10.Transformă și printează notele din sistem românesc în  >
Peste 9 => A
Peste 8 => B
Peste 7 => C
Peste 6 => D
Peste 4 => E
4 sau sub => F'''
# nota = int(input("Ce nota ai luat?"))
#
# if nota >= 9:
#     print(f'{nota} este echivalent cu A')
# elif nota >= 8:
#     print(f'{nota} este echivalent cu B')
# elif nota >= 7:
#     print(f'{nota} este echivalent cu C')
# elif nota >= 6:
#     print(f'{nota} este echivalent cu D')
# elif nota >= 4:
#     print(f'{nota} este echivalent cu E')
# else:
#     print(f'{nota} este echivalent cu F')

'''11.Verifică dacă x are minim 4 cifre (x e int).
(ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)'''

# numar = str(input('Introduceti un numar:'))
#
# if len(numar) >= 4:
#     print(f'{numar} are {len(numar)} cifre')
# else:
#     print(f'{numar} are mai putin de 4 cifre')
'''12.Verifică dacă x are exact 6 cifre.'''
# numar = str(input('Introduceti un numar:'))
#
# if len(numar) == 6:
#     print(f'{numar} are {len(numar)} cifre')
# else:
#     print(f'{numar} are {len(numar)} cifre')
'''13.Verifică dacă x este număr par sau impar (x e int).'''

# numar = str(input('Introduceti un numar:'))
# if int(numar[-1]) % 2 > 0:
#     print(f'{numar} este impar')
# else:
#     print(f'{numar} este par')

'''14.  x, y, z (int)
Afișează care este cel mai mare dintre ele?'''

# x = int(input('Introduceti un numar:'))
# y = int(input('Introduceti un numar:'))
# z = int(input('Introduceti un numar:'))
# if x > y and x > z:
#     print(f'{x} este cel mai mare numar!')
# elif y > x and y > z:
#     print(f'{y} este cel mai mare numar!')
# else:
#     print(f'{z} este cel mai mare numar!')
'''15. X, y, z - reprezintă unghiurile unui triunghi
Verifică și afișează dacă triunghiul este valid sau nu.'''
# x = int(input('Introduceti primul unghi al triunghiului:'))
# y = int(input('Introduceti al doilea unghi al triunghiului:'))
# z = int(input('Introduceti al treilea unghi al triunghiului:'))
#
# if x + y + z == 180:
#     print(f'Triunghiul este valid')
# else:
#     print(f'Triungliul nu este valid.')

'''16. Având stringul: 'Coral is either the stupidest animal or the smartest rock'
Citește de la tastatură un int x
Afișează stringul fără ultimele x caractere
Exemplu: dacă ai ales 7 => 'Coral is either the stupidest animal or the smarte'''''

# prop = 'Coral is either the stupidest animal or the smartest rock'
#
# x = int(input("Introduceti un numar"))
# print(prop[:-x:])
'''17. Același string. Declară un string nou care să fie format din primele 5 caractere + ultimele 5.'''

# prop = 'Coral is either the stupidest animal or the smartest rock'
# prop2 = prop[:5:]+prop[-5::]
# print(prop2)

'''18. Același string. 
Salvează într-o variabilă și afișează indexul de start al cuvântului rock (hint: este o funcție care te ajuta sa faci asta)
Folosind această variabilă + slicing, afișează tot stringul până la acest cuvânt
output: 'Coral is either the stupidest animal or the smartest' '''
# prop = 'Coral is either the stupidest animal or the smartest rock'
# print(prop.index('rock'))
# print(prop[:prop.index('rock'):])

'''it zarul
Caută pe net și vezi cum se generează un număr random
Ne imaginăm ca dai cu zarul și salvăm acest număr în dice_roll
Ia numărul ghicit de la utilizator
Verifică și afișează dacă utilizatorul a ghicit
Vei avea 3 opțiuni
Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y.
Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y.
Ai ghicit. Felicitări! Ai ales x si zarul a fost y.'''

# import random
# x = random.randint(1, 6)
# y = int(input("Introduceti un nr de la 1 la 6:  "))
# if y == x:
#   print(f'Felicitari! Ai ales {y} si zarul a fost {x}')
# elif y < x:
#   print(f'Ai pierdut. Ai ales un numar mai mic. Ai ales {y} dar a fost {x}.')
# else:
#   print(f'Ai pierdut. Ai ales un numar mai mare. Ai ales {y} dar a fost {x}.')

'''20.  Citește de la tastatură un string
Verifică dacă primul și ultimul caracter sunt la fel. Se va folosi un assert
Atenție: se dorește ca programul să fie case insensitive - 'apA' e acceptat'''

# f = str(input("Introduceti un sir de caractere"))
# x = f[0]
# y = f[-1]
# assert x == y, 'Literele sunt la fel'

'''21. Având stringul '0123456789'
Afișează doar numerele pare 
Afișează doar numerele impare
(hint: folosește slicing, controlează din pas)'''

# cifre = '0123456789'
# print(cifre[::2])
# print(cifre[1::2])
