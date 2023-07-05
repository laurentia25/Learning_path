"""
1. Explica intr-un comentariu ce este o variabila de tip string.
"""

# O variabila careia ii este asignata o valoare de tip string
# -> text sau orice altceva scris cu ghilimele

"""
2. Defineste 3 variabile: oras, strada si nr.
a. Afiseaza aceste variabile intr-o propozitie, folosind concatenarea string-urilor.
b. Afiseaza aceste variabile intr-o propozitie, folosind f-strings.
"""

# oras = "Cluj"
# strada = "Ion Creanga"
# nr = "54"
# print("Locuiesc in"+oras+"pe strada"+strada+nr, sep = " ")
# print(f'Locuiesc in {oras} pe strada {strada} {nr}')

"""
3. Se da variabila string, nume_complet = 'Pop Maria Ioana'.
a. Afiseaza numele de familie din string.
b. Afiseaza al doilea prenume.
c. Afiseaza de cate ori apare litera 'a' in nume_complet.
d. Inverseaza string-ul si afiseaza rezultatul.
e. Inlocuieste al doilea prenume cu 'Elena'.
f. Afiseaza caracterele de la indexul 5 la indexul 9 (inclusiv).
g. Afiseaza caracterele de la inceputul string-ului pana la index-ul 8 (inclusiv).
"""
# nume_complet = 'Pop Maria Ioana'
# # a
# nume = nume_complet[:3]
# print(nume)
# # b
# prenume2 = nume_complet[-5:]
# print(prenume2)
# # c
# print(nume_complet.count("a"))
# # d
# print(nume_complet[::-1])
# # e
# nume_nou = nume_complet.replace("Ioana","Elena")
# print(nume_nou)
# # f
# slice = nume_complet[4:10]
# print(slice)
# # g
# slice2 = nume_complet[:9]
# print(slice2)

"""
4. Citeste de la tastatura culoarea preferata a utilizatorului si salveaza rezultatul intr-o variabila.
a. Determina lungimea inputului citit de la tastatura.
b. Determina tipul inputului citit de la tastatura.
c. Transforma inputul de la utilizator in text cu litere mari si afiseaza-l.
d. Transforma inputul de la utilizator in text care incepe cu litera mare si restul sunt litere mici.
Afiseaza rezultatul.
"""

# culoare_preferata = str(input("Care este culoarea ta preferata?"))
# # a
# print(len(culoare_preferata))
# # b
# print(type(culoare_preferata))
# # c
# print(culoare_preferata.upper())
# # d
# print(culoare_preferata.capitalize())

"""
5. Se da variabila anotimp = 'primavara'. Verifica daca anotimp se termina in 'vara'.
"""

# anotimp = 'primavara'
# last4 = anotimp[-4:] == "vara"
# print(last4)

"""
6. Citeste de la tastatura pretul cosului de cumparaturi. Afiseaza pretul cu un discount de 25%.
"""

# pret = int(input("Care este pretul produsului?"))
# pret2 = pret - pret*25/100
# print(pret2)

"""
7. Se da string-ul: zile_sapt = 'luni,marti,miercuri,joi,vineri,sambata,duminica'.
Transforma string-ul in lista, folosindu-te de o metoda ajutatoare de pe string.
"""

# zile_sapt = 'luni,marti,miercuri,joi,vineri,sambata,duminica'
# lista = zile_sapt.rsplit()
# print(lista)

"""
8. Scrie un program care solicita utilizatorului sa introduca varsta sa
și returneaza un mesaj personalizat, in funcție de varsta introdusa.
Daca varsta este mai mare sau egala cu 18, programul trebuie sa afiseze
mesajul "Esti major si poti vota".
In caz contrar, programul trebuie sa afiseze mesajul "Esti minor si nu poti vota inca".
"""

# varsta = int(input("Ce varsta ai?"))
# if varsta >= 18:
#     print("Esti major si poti vota")
# else:
#     print('Esti minor si nu poti vota inca')
#
"""
9. Scrie un program care primeste un pret de la tastatura si afiseaza
un mesaj daca prețul este mai mare sau mai mic decât 100 de lei.
"""

# pret = int(input("Te rog sa introduci un pret!"))
# if pret > 100:
#     print("Pretul este mai mare de 100 de lei!")
# elif pret == 100:
#     print("Pretul este de 100 de lei!")
# else:
#     print("Pretul este mai mic de 100 de lei!")

"""
10. Citeste doua numere intregi de la tastatura. Printeaza produsul dintre cele doua numere
daca acesta este mai mic sau egal decat 1000, altfel printeaza suma lor.
"""
# num1 = int(input("Te rog sa dai valoare primului numar:"))
# num2 = int(input("Te rog sa dai valoare celui de al doilea numar:"))
#
# if num1 * num2 > 1000:
#     num3 = num1 + num2
#     print(num3)
# else:
#     num3 = num2 * num1
#     print(num3)

"""
11. Se dau doua liste:
lista_1 = [10, 20, 30, 40, 50, 10]
lista_2 = [1, 2, 3, 4, 5]
Pentru fiecare lista verifica daca primul si ultimul element sunt egale.
In functie de rezultat, afiseaza un mesaj.
"""

# lista_1 = [10, 20, 30, 40, 50, 10]
# lista_2 = [1, 2, 3, 4, 5]
#
# if lista_1[0] == lista_1[len(lista_1)-1] or lista_2[0] == lista_2[len(lista_2)-1] :
#     print("in lista 1 primul si ultimul element sunt egale")
# else:
#     print("primul si ultimul element nu sunt egale")


"""
12. Scrie un program care afiseaza de cate ori apare litera 'e' in
stringul str_1 = 'Emma is a sofware developer.'
"""

# str_1 = 'Emma is a sofware developer.'
# print(str_1.count("e"))

"""
13. Scrie un program in care citesti de la tastatura doua nr intregi,
numite base si exponent.
Afiseaza intr-un mesaj sugestiv, valoarea lui base la puterea exponent.
Atentie: indiferent daca utilizatorul a introdus un numar pozitiv sau negativ
ca si exponent, trebuie sa ridici base la puterea exponent pozitiv.
hint: exploreaza functia abs() si vezi cum o poti folosi
"""
# base = int(input("Te rog sa introduci un numar!"))
# exponent = int(input("Te rog sa introduci al doilea numar"))
# print(f'Valoarea bazei este {base}')
# print(f'Valoarea exponentului este {exponent}')
# putere = base ** abs(exponent)
# print(putere)


"""
14. Scrie un program in care se citeste de la tastatura un string.
Daca string-ul are numar impar de caractere, afiseaza un string care
contine primul caracter, caracterul din mijloc si ultimul caracter
al string-ului citit de la tastatura.
Daca string-ul are numar par de caractere, afiseaza un string care contine doar primul
si ultimul caracter  al string-ului citit de la tastatura.
"""

# string = str(input("Te rog sa introduci un sir de caractere"))
#
# if len(string)%2 != 0 :
#     primul_caracter = string[0]
#     index_mijloc = int((len(string)-1)/2)
#     mijloc = string[index_mijloc]
#     ultimul_caracter = string[-1]
#     print(f'{primul_caracter} {mijloc} {ultimul_caracter}')
# else:
#     primul_caracter = string[0]
#     ultimul_caracter = string[-1]
#     print(f'{primul_caracter} {ultimul_caracter}')
"""
15. Se dau doua variabile:
str1 = 'Abc'
str2 = 'Xyz'
Creeaza o variabila string, str3 formata din:
- primul caracter din str1 cu litera mica
- primul caracter din str2 cu litera mare
- al doilea caracter din str1 cu litera mare
- al doilea caracter din str2 cu litera mare
- al treilea caracter din str1 cu litera mare
- al treilea caracter din str2 cu litera mica
"""

# str1 = 'Abc'
# str2 = 'Xyz'
# str3 = str1.lower()[0]+str2.upper()[0]+str1.upper()[1]+str2.upper()[1]+str1.upper()[2]+str2.lower()[2] # => aXBYCz
# print(str3)

"""
16. Se da lista:
fruits = ["apple", "banana", "cherry"]
a. Schimba elementul 'apple' cu 'kiwi'.
b. Foloseste metoda append() pentru a adauga elementul 'oranges'.
c. Foloseste metoda insert() pentru a adauga elementul 'lemon' ca al doilea
element din lista.
d. Foloseste metoda remove() pentru a sterge elementul 'banana' din lista.
e. Foloseste un index negativ pentru a accesa ultimul element din lista.
f. Foloseste un index negativ pentru a accesa penultimul element din lista.
g. Afiseaza lungimea listei.
h. Foloseste slicing pe lista, astfel incat sa obtii o lista cu al doilea, al treilea
si al patrulea element.
"""

# fruits = ["apple", "banana", "cherry"]
# # a
# fruits.remove('apple')
# fruits.append('kiwi')
# print(fruits)
# # b
# fruits.append('oranges')
# print(fruits)
# # c
# fruits.insert(1,'lemon') #=> unde adaugam, ce adaugam
# print(fruits)
# # d
# fruits.remove('banana')
# print(fruits)
# # e
# ultimul_element = fruits[-1]
# print(ultimul_element)
# print(fruits[-1])
# # f
# print(fruits[-2])
# # g
# print(len(fruits))
# # h
# print(fruits[1 :4 :1])

"""
17. Inverseaza lista my_list = [100, 200, 300, 400].
"""

# my_list = [100, 200, 300, 400]
# print(my_list[::-1])

"""
18. Lista de cumparaturi:
Se citeste de la tastatura o lista de cumparaturi. Utilizatorul introduce
lista de cumparaturi ca un string, cu alimentele separate prin virgula,
ATENTIE: fara spatii
Exemplu:rosii,castraveti,branza,oua
a. Sa se transforme string-ul citit de la tastatura intr-o lista. (vezi metode ajutatoare string).
b. Sorteaza lista de cumparaturi si printeaza lista sortata.
c. Adauga un aliment nou in lista de cumparaturi.
d. Sterge un aliment din lista de cumparaturi.
e. Modifica elementul de la pozitia 0 din lista.
f. Daca lista contine 'rosii' in ea, afiseaza mesajul "Aliment sanatos".
Daca nu, afiseaza mesajul "Iti recomandam rosiile de asemenea".
"""
# lista = str(input('Introduceti lista de cumparaturi'))
#
# lista_de_cumparaturi = lista.replace(' ', '')
# print(lista_de_cumparaturi)
# # a
# lista_sortata = lista_de_cumparaturi.rsplit(sep = ",")
# # b
# lista_sortata.sort()
# print(lista_sortata)
# # c
# aliment_nou = str(input("Adauga un aliment nou in lista"))
# lista_sortata.append(aliment_nou)
# print(lista_sortata)
# # d
# print(lista_sortata.pop())
# print(lista_sortata)
# # e -> ce inseamna modifica? sa il inlocuiesc cu o valoare noua
# lista_sortata.insert(0, "ceapa")
# print(lista_sortata)
# # f  Daca lista contine 'rosii' in ea, afiseaza mesajul "Aliment sanatos".
# if lista_sortata.count('rosii') > 0:
#     print("Aliment sanatos")
# else:
#     print("Iti recomandam rosiile de asemenea")

"""
19. Se da lista fructe = ['capsuni', 'mere', 'lamai'].
Converteste lista la string si afiseaza string-ul. A se vedea metoda join(). (search on google)
"""

# fructe = ['capsuni', 'mere', 'lamai']
# separator = "-"
# result = separator.join(fructe)
# print(result)

"""
20. Se da lista numere = [1, 2, 3, 4, 56, 22, 5].
Afiseaza elementul cu valoarea maxima din string. (google- functia max())
"""

# numere = [1, 2, 3, 4, 56, 22, 5]
# print(max(numere))

"""
21. Se da lista preturi = [12.3, 34.5, 22].
Calculeaza suma elementelor din lista preturi. (google - functia sum())
"""
# preturi = [12.3, 34.5, 22]
# print(sum(preturi))

"""
22. Se da dictionarul:
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
a. Afiseaza valoarea cheii city.
b. Kelly a fost promovata. Salariul ei este acum de 10000 lei. Fa modificarea si in dictionar.
c. Sterge varsta din dictionar.
d. Adauga o noua pereche cheie-valoare in dictionar, cu cheia employment_date. Valoarea o alegi tu.
e. Verifica daca exista cheia 'country' in dictionar. Daca nu exista, adauga-o.
"""
# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"}
# # a
# print(sample_dict['city'])
# # b
# sample_dict['salary'] = 10000
# print((sample_dict['salary']))
# # c
# del sample_dict['age']
# print(sample_dict)

# d ->d. Adauga o noua pereche cheie-valoare in dictionar, cu cheia employment_date. Valoarea o alegi tu.
# sample_dict.update({"employment_date": "2 mai 2023"})
# print(sample_dict)
#
# # e. Verifica daca exista cheia 'country' in dictionar. Daca nu exista, adauga-o.
#
# if sample_dict.get('country','0') == '0':
#     sample_dict['country'] = 'Moldova'
#     print(sample_dict['country'])
# else:
#     print(sample_dict['country'])

"""
23. Se da dictionarul:
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
a. Afiseaza toate cheile din dictionar. (HINT: metoda keys())
b. Afiseaza toate valorile din dictionar. (HINT: metoda values())
c. Verifica lungimea dictionarului.
"""
# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"
# }
# # a
# print(sample_dict.keys())
# # b
# print(sample_dict.values())
# # c
# print(len(sample_dict))

"""
24. Gasirea unui element intr-un dictionar
Se da dictionarul:
persoana = {
    'nume': 'Alex',
    'varsta': 25,
    'oras': 'Bucuresti'
}
Utilizatorul introduce cheia cautata.
Verifica daca aceasta se gaseste sau nu in dictionar.
"""
# persoana = {
#     'nume': 'Alex',
#     'varsta': 25,
#     'oras': 'Bucuresti'
# }
# cheie = str(input('Te rog sa introduci o cheie!'))
# cheie_cautare = cheie.replace(" ",'')
# print(persoana.get(cheie_cautare, 'Cheia cautata nu exista.'))

"""
25. Adaugarea unui element intr-un dictionar
Se da dictionarul:
 persoana = {
    'nume': 'Alex',
    'varsta': 25,
    'oras': 'Bucuresti'
}
Utilizatorul trebuie sa introduca cheia si valoarea pe care doreste sa
le adauge in dictionar.
Foloseste metoda update() (metoda ajutatoare pe dictionar)
"""
# persoana = {
#     'nume': 'Alex',
#     'varsta': 25,
#     'oras': 'Bucuresti'
# }
# cheie = str(input('Te rog sa introduci o cheie:'))
# valoare = input('Te rog sa introduci o valoare pentru cheie:')
# persoana.update({cheie : valoare})
# print(persoana)
"""
26. Stergerea unui element din dictionar
 Se da dictionarul:
 persoana = {
    'nume': 'Alex',
    'varsta': 25,
    'oras': 'Bucuresti'
}
Utilizatorul introduce cheia elementului de eliminat.
a. Elimina elementul, verificand prima data daca cheia se afla in dictionar,
si daca se afla, foloseste metoda del.
b. Elimina elementul, folosind metoda ajutatoare pop().
"""
# persoana = {
#     'nume': 'Alex',
#     'varsta': 25,
#     'oras': 'Bucuresti'
# }
# cheie_eliminata = str(input('Ce cheie vrei sa stergi?'))
# if persoana.get(cheie_eliminata,'Nu exista') == 'Nu exista':
#     print('Cheia nu exista')
# else:
#     del persoana[cheie_eliminata]
#     print('Cheia a fost strearsa')
# print(persoana)

"""
27. Concatenarea a doua dictionare.
Se dau doua dictioanare:
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
Sa se concateneze cele doua dictionare folosind metoda update().
Observatie: Metoda update() o putem folosi pentru a adauga unul sau mai multe
perechi cheie:valoare in dictionar.
"""
# dict1 = {'a': 1, 'b': 2}
# dict2 = {'c': 3, 'd': 4}
# dict2.update(dict1)
# print(dict2)

"""
28. Se da urmatoarea lista cu dictionare:
lista = [{'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6}]
a. Adauga perechea {'c':'3'} in primul dictionar din lista.
b. Adauga un nou dictionar ca element in lista. Adauga-l la final.
c. Aduaga un nou dictionar ca element in lista, la indexul 1.
d. Verifica daca in al doilea dictionar din lista se gaseste cheia 'c'.
"""
# lista = [{'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6}]
# # a
# primul_dict = lista[0]
# primul_dict.update({'c':'3'})
# lista[0] = primul_dict
# print(lista)
# # b
# lista.append({'l':'9'})
# print(lista)
# # c
# lista.insert(1,{'p':'10'})
# print(lista)
# # d
# dictionar2 = lista[1]
# if dictionar2.get('c', 'nu exista') == 'nu exista':
#     print('Cheia c nu exista in dictionar')
# else:
#     c = dictionar2.get('c', 0)
#     print(f'Valoarea cheii c este {c}')
"""
29.
Se citeste de la tastatura un numar.
a. Printeaza un mesaj sugestiv daca numarul este par sau nu.
b. Daca numarul este multiplu de 4, afiseaza un mesaj sugestiv.
"""
# numar = int(input("Te rog sa introduci un numar:"))
#
# if numar%2 > 0:
#     print("Numarul introdus este impar")
# elif numar%4 > 0:
#     print("Numarul nu este multiplu de 4")
# else:
#     print("Numarul este multiplu de 4")

"""
30.
Se citesc de la tastatura doua numere, num si check. Verifica daca
num este divizibil cu check si afiseaza un mesaj corespunzator catre utilizator.
"""
# num = int(input("Te rog sa introduci un numar:"))
# check = int(input("Te rog sa introduci un numar:"))
# if num%check == 0:
#     print(f"{num} este divizibil cu {check}")
# else:
#     print(f"{num} nu este divizibil cu {check}")

"""
31. Se da dictionarul:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
a. Foloseste metoda get() pentru a printa valoarea cheii 'model'.
b. Schimba valoarea cheii 'year' in 1970.
c. Adauga perechea cheie:valoare 'color':'red' in dictionar.
Adaug-o folosind accesarea dictionarului prin cheie (car['color']) si dand o valoare.
Adaug-o folosind metoda update()
d. Foloseste metoda pop() pentru a sterge 'model' din dictionar.
e. Foloseste metoda empty() pentru a 'goli' dictionarul.
"""

# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# a. Foloseste metoda get() pentru a printa valoarea cheii 'model'.
# print(car.get('model',"Nu exista cheia model"))
# b. Schimba valoarea cheii 'year' in 1970.
# car['year'] = 1970
# print(car)
# c. Adauga perechea cheie:valoare 'color':'red' in dictionar.
# Adaug-o folosind accesarea dictionarului prin cheie (car['color']) si dand o valoare.
# Adaug-o folosind metoda update()
# car['color'] ='red'
# print(car)
# car.update({'color':'red'})
# print(car)
# d. Foloseste metoda pop() pentru a sterge 'model' din dictionar.
# car.pop('model')
# print(car)
# e. Foloseste metoda clear() pentru a 'goli' dictionarul.
# car.clear()
# print(car)
