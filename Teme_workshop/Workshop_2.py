"""1. Declară o listă note_muzicale în care să pui do re mi etc până la do
Afișeaz-o.
Inversează ordinea folosind slicing și suprascrie această listă.
Printează varianta actuală (inversată).
Pe această listă aplică o metodă care bănuiești că face același lucru, adică să îi inverseze ordinea.
Nu trebuie să o suprascrii în acest caz, deoarece metoda face asta automat.
Printează varianta actuală a listei. Practic ai ajuns înapoi la varianta inițială."""

# note = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
# print(note)
# print(note[::-1]) # slicing este temporar
# note.reverse() # metoda inverseaza lista si o suprascrie peste lista initiala
# print(note)

'''2. De câte ori apare ‘do’?'''
# print(note.count('do'))

'''3. Având 2 liste, [3, 1, 0, 2] și [6, 5, 4]
   Găsește 2 variante să le unești într-o singură listă.'''
# lista1 = [3, 1, 0, 2]
# lista2 = [6, 5, 4]
# output = lista2+lista1
# print(output)
# lista2.extend(lista1) # metoda noua cu extent!
# print(lista2)
'''4 Sortează și afișează lista generată la exercițiul anterior.
Șterge numărul 0 folosind o metoda.
Afișaza iar lista.'''
# output.sort()
# print(output)
# output.pop(0)
# print(output)

'''5 Folosind un if verifică lista generată la exercițiul 3 și afișează:
Lista este goală.
Lista nu este goală.'''
# if len(output) != 0:
#     print('lista nu este goala')
# else:
#     print('lista este goala')

'''6. Folosește o funcție care să șteargă lista de la exercițiul 3.'''

# lista2.clear()
'''7. Copy paste la exercițiul 5. Verifică încă o dată.
Acum ar trebui să se afișeze că lista e goală.'''

# print(lista2)


'''8. Având dicționarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
Folosește o funcție că să afișezi Elevii (cheile)'''

# dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}
# chei = dict1.keys()

'''9. Printează cei 3 elevi și notele lor
Ex: ‘Ana a luat nota {x}’
Doar nota o vei lua folosindu-te de cheie'''


# print(chei[0], 'a luat nota ', {dict1['Ana']})

# print(dict1.items())
# for item in dict1.items():
#     print(item)
# for key, value in dict1.items():
#     print(key, 'a luat nota', value)

'''10. Dorel a făcut contestație și a primit 6
Modifică nota lui Dorel în 6
Printează nota după modificare'''

# dict1['Dorel'] = 6
# print(dict1.items())
# for item in dict1.items():
#     print(item)
# for key, value in dict1.items():
#     print(key, 'a luat nota', value)

'''11. Gigel se transferă din clasă
Căuta o funcție care să îl șteargă
Vine un coleg nou. Adaugă Ionică, cu nota 9
Printează noii elevi'''

# del dict1['Gigel']
# dict1.update({'Ionică': 9})
# print(dict1.items())
# for item in dict1.items():
#     print(item)
# for key, value in dict1.items():
#     print(key, 'a luat nota', value)

'''12. Ne imaginăm o echipă de fotbal pt teren sintetic.
3 Schimbări maxime admise:

Declară o Listă cu 5 jucători
Schimbari_efectuate = te joci tu cu valori diferite
Schimbari_max = 3'''

# jucatori = ['Gigel', 'Dorel', 'Ion', 'Andrei', 'Cristi']

'''Dacă Jucătorul x e în teren și mai avem schimbări la dispoziție
Efectuează schimbarea 
Șterge jucătorul scos din listă
Adaugă jucătorul intrat
Afișază a intrat x, a ieșit y, mai ai z schimbări

Dacă jucătorul nu e în teren:
Afișază ‘nu se poate efectua schimbarea deoarece jucătorul x nu e în teren’
Afișază ‘mai ai z schimbări’

Testează codul cu diferite valori

Google search hint
“how to check if item is în list python”'''


'''13.Set zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
Adaugă în zilele_sapt ‘luni’
Afișează zile_sapt'''
# zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
# weekend = {'sâmbăta', 'duminică'}

# zile_sapt.add('luni')
# print(zile_sapt)

'''14.Folosește un if și verifică dacă:
Weekend este un subset al zilelor din săptămânii.
Weekend nu este un subset al zilelor din săptămânii.'''
# if weekend.issubset(zile_sapt):
#     print('Weekend este subset pentru zile_sapt')
# else:
#     print('Weekend nu este subset pentru zile_sapt')

'''15. Afișează diferențele dintre aceste 2 seturi.'''
# print(zile_sapt.difference(weekend))

'''16. Afișează intersecția elementelor din aceste 2 seturi.'''
# print(zile_sapt.intersection(weekend))

# Partea 2 - Cicluri repetitive

'''1.Având lista:
mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel'] 

Folosește un for că să iterezi prin toată lista și să afișezi;
‘Mașina mea preferată este x’.
Fă același lucru cu un for each.
Fă același lucru cu un while.'''

# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']

# for item in range(len(masini)):
#     print(f'Masina mea preferata este {masini[item]}')


# for masina in masini:
#     print(f'Masina mea preferata este {masina}')


# index = 0
# while index < len(masini):
#     if index < len(masini):
#         print(f'Masina mea preferata este {masini[index]}')
#         index += 1


'''2. Aceeași listă:
Folosește un for else
În for
Modifică elementele din listă astfel încât să fie scrise cu majuscule, exceptând primul și ultimul.
În else:
  Printează lista.'''

# for a in range(len(masini)):
#     if a > 0 and a < len(masini)-1:
#         masini[a] = masini[a].upper()
# print(masini)

'''3. Aceeași listă:
Vine un cumpărător care dorește să cumpere un Mercedes.
Iterează prin ea prin modalitatea aleasă de tine.
Dacă mașina e mercedes:
   Printează ‘am găsit mașina dorită de dvs’
   Ieși din ciclu folosind un cuvânt cheie care face acest lucru
Altfel:
   Printează ‘Am găsit mașina X. Mai căutam‘'''

# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# for masina in masini:
#     if masina == "Mercedes":
#         print("Am gasit masina dorita de dvs")
#         break
#     else:
#         print(f'Am gasit masina {masina}. Mai cautam')
#
# x=0
# while x<=len(masini):
#         if masini[x] == 'Mercedes':
#             print('Am gasit masina')
#             break
#         else:
#             print(f'Am gasit masina {masini[x]}')
#             x+=1

'''4. Aceeași listă;
Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu excepția Trabant și Lăstun. 
Dacă mașina e Trabant sau Lăstun:
   Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie else).
Printează S-ar putea să vă placă mașina x.'''

# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']

# x = 0
# print(f'S-ar putea sa va placa {masini[x]}')
# while x <= len(masini):
#     if masini[x] == "Trabant" and masini[x] == 'Lăstun':
#        print(f'S-ar putea sa va placa {masini[x]}')
#        x += 1

# for masina in masini:
#     if masina == 'Lăstun' or masina == 'Trabant':
#         continue
#     print(f'S-ar putea sa va placa {masina}')

'''5. Modernizează parcul de mașini:

Crează o listă goală, masini_vechi.
Iterează prin mașini.
Când găsesti Lăstun sau Trabant:
Salvează aceste mașini în masini_vechi.
Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).
Printează Modele vechi: x.
Modele noi: x.'''
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']

# masini_vechi =[]
# for masina in masini:
#     if masina == 'Trabant' or masina == 'Lăstun':
#        masini_vechi.append(masina)
#        masini.remove(masina)
#        masini.append('Tesla')
# print(f'Modele vechi {masini_vechi}')
# print(f'Modele noi:{masini}')

'''6. Având dict:
pret_masini = {
    'Dacia': 6800,
    'Lăstun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}

Vine un client cu un buget de 15000 euro.

Prezintă doar mașinile care se încadrează în acest buget.
Iterează prin dict.items() și accesează mașina și prețul.
Printează Pentru un buget de sub 15000 euro puteți alege mașină xLastun
Iterează prin listă.
'''

# pret_masini = {
#     'Dacia': 6800,
#     'Lăstun': 500,
#     'Opel': 1100,
#     'Audi': 19000,
#     'BMW': 23000}
#
# masini = list(pret_masini.keys())
# # print(masini)
# # print(masini[0])
# i = 0
# masini_buget = {}
# for i in range(len(masini)):
#     if pret_masini[masini[i]] <= 15000:
#         # print(masini[i])
#         # print(pret_masini[masini[i]])
#         masini_buget.update({masini[i]: pret_masini[masini[i]]})
#         i += 1
# print(masini_buget)
# print(f'Pentru o masina de pana in 15000 euro puteti alege din: {masini_buget}')

'''7. Având lista:
numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
Iterează prin ea.
Afișează de câte ori apare 3 (nu ai voie să folosești count).'''

# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# x = 0
# n = []
# for x in range(len(numere)):
#     if numere[x] == 3:
#         n.append(numere[x])
#         x += 1
# print(len(n))

'''8. Aceeași listă:
Iterează prin ea
Calculează și afișează suma numerelor (nu ai voie să folosești sum).'''

# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# x = 0
# s = 0
# for x in range(len(numere)):
#     s += numere[x]
# print(s)

'''9. Aceeași listă:
Iterează prin ea.
Afișază cel mai mare număr (nu ai voie să folosești max).'''

# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# max = numere[0]
# for x in range(len(numere)):
#     if max <= numere[x]:
#         max = numere[x]
#         x += 1
# print(max)

'''10. Aceeași listă:
Iterează prin ea.
Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
Ex: dacă e 3, să devină -3
Afișază noua listă.'''

# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
#
#
# for x in range(len(numere)):
#     if numere[x] >= 0:
#         numere.insert(x, -numere[x])
#         numere.remove(numere[x+1])
# print(numere)

'''11.
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
Itereaza prin listă alte_numere
Populează corect celelalte liste
Afișează cele 4 liste la final'''
#
# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# numere_pare = []
# numere_impare = []
# numere_pozitive = []
# numere_negative = []
#
# for x in range(len(alte_numere)):
#     if alte_numere[x] % 2 == 0:
#         numere_pare.append(alte_numere[x])
#     else:
#         numere_impare.append(alte_numere[x])
#     if alte_numere[x] > 0:
#         numere_pozitive.append(alte_numere[x])
#     else:
#         numere_negative.append(alte_numere[x])
# print(numere_pare)
# print(numere_impare)
# print(numere_pozitive)
# print(numere_negative)

'''12. Aceeași listă:
Ordonează crescător lista fară să folosești sort.'''
# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
#
# for i in range(len(alte_numere)):
#     for j in range(len(alte_numere) - i - 1):
#         if alte_numere[j] > alte_numere[j + 1]:
#             alte_numere[j], alte_numere[j + 1] = alte_numere[j + 1], alte_numere[j]
#
# print(f'Lista sortata: {alte_numere}')


'''13. Ghicitoare de număr:
numar_secret = Generați un număr random între 1 și 30
Numar_ghicit = None
Folosind un while
   User alege un număr
   Programul îi spune:
Nr secret e mai mare
Nr secret e mai mic
Felicitări! Ai ghicit!'''

# import random
# numar_secret = random.randint(1, 30)
# guessed = False
# while not guessed:
#     numar_ghicit = int(input("Introduceti un nr de la 1 la 30:"))
#     if numar_ghicit == numar_secret:
#         print('Felicitari ai ghicit numarul!')
#         guessed = True
#     elif numar_ghicit > numar_secret:
#         print('Numarul introdus este prea mare!')
#     else:
#         print('Numarul este prea mic')

'''14. Alege un număr de la tastatură
Ex: 7
Scrie un program care să genereze în consolă următoarea piramidă
1
22
333
4444
55555
666666
7777777

Ex:3
1
22
333
'''
# numar = int(input("introduceti un nr"))
# i = 1
# while i <= numar:
#     print(str(i) * i)
#     i += 1

'''15.
tastatura_telefon = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [0]
]
Iterează prin listă 2d
Printează ‘Cifra curentă este x’
(hint: nested for - adică for în for)
'''
# tastatura_telefon = [
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9],
#   [0]
# ]
# for a in tastatura_telefon:
#     for item in a:
#         print(item)
