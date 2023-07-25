"""
Exercitii recapitulative
"""

"""
1. Creaza o functie Python care inversează și returnează un număr întreg pozitiv.
În cazul unui număr negativ, afișează o eroare.

Exemple: 
reverse(1234567) => 7654321
reverse(10) => 1
reverse(101) => 101
reverse(10000000) => 1
reverse(-65) => eroare -> ValueError
"""


# def reverse(x):
#     if x > 0:
#         y = str(x)
#         return int(y[::-1])
#     else:
#         raise ValueError('numarul nu e pozitiv')
#
#
# a = reverse(10)
# print(a)

"""
2. Creaza o functie Python care primește o lista și un număr întreg pozitiv k, si roteste lista cu k pozitii.
 
Exemple:
rotate([1, 2, 3, 4, 5], 2) => [3, 4, 5, 1, 2]
rotate([1, 2, 3, 4, 5], 4) => [5, 1, 2, 3, 4]
rotate([1, 2, 3, 4, 5], 8) => [4, 5, 1, 2, 3]
rotate([1, 2, 3, 4, 5], 5) => [1, 2, 3, 4, 5]
rotate([1, 2, 3, 4, 5], 6) => [2, 3, 4, 5, 1]
rotate([1, 2, 3, 4, 5], 7) => [3, 4, 5, 1, 2]
"""


# def rotate(lista, k):
#     k = k % len(lista)
#     lista_v2 = lista[k:] + lista[0:k]
#     print(lista_v2)
#
#
# rotate([1, 2, 3, 4, 5], 14)

"""
3. Creaza o functie Python care primește 2 stringuri, și verifica dacă acestea sunt anagrame (case-insensitive).

Exemple:
is_anagram(‘Adela’, ‘ealad’) => True
is_anagram(‘ITFactory’, ‘acfiorty’) => True
is_anagram(‘Stringy’, ‘gringsty’) => False
is_anagram(‘ana’, ‘ioana’) => False
"""


# def is_anagram(cuvant1, cuvant2):
#     if sorted(cuvant1.upper()) == sorted(cuvant2.upper()):
#         print("Sunt anagrams.")
#     else:
#         print("The strings aren't anagrams.")
#
#
# cuvant1 = input("string1 =  ")
# cuvant2 = input("string2 = ")
# is_anagram(cuvant1, cuvant2)

"""
4. Creaza o functie Python care primeste o lista de numere, si il returneaza pe al doilea cel mai mare numar distinct.

Exemple:
get_second_biggest([1,2,3,4,5]) => 4
get_second_biggest([1,2,3,4,4]) => 3
get_second_biggest([1,2,4,4,4]) => 2
get_second_biggest([-1,-2,-3,-4,-5]) => -2
"""


# def get_second_bigest(list):
#     list.sort()
#     a = list[len(list)-2]
#     return a
#
#
# print(get_second_bigest([1, 3, 4, 5, 7, 4, 9]))

"""
5. Creaza o functie Python care primeste doua stringuri ce reprezinta niste numere foarte mari,
si returneaza rezultatul adunarii “numerelor”, tot sub format string:

Exemple:
add_two(‘12345’, ‘12345’) => ‘24690’
add_two(‘1234’, ‘4321’) => ‘5555’
add_two(‘563895634’, ‘548967348053’) => ‘549531243687’
"""

# def add_two(a, b):
#     a = int(a)
#     b = int(b)
#     c = a + b
#     return str(c)
#
#
# a = str(input('Introduceti un nr1'))
# b = str(input('Introduceti un nr2'))
#
# print(add_two(a, b))

"""
6. Creaza o functie Python care primeste un numar n, si o lista de numere de dimensiune n-1.
In lista se afla toate numerele de la 1 la n, in afara de 1.
Functia trebuie sa gaseasca acel numar in cel mai eficient mod posibil si sa-l returneze.

Exemple:
find_missing(5, [1,2,3,5]) => 4
find_missing(2, [1]) => 2
find_missing(7, [6,5,1,3,2,7]) => 4
"""


# def find_missing(n, numbers):
#     numbers.sort()
#     for i in range(n-1):
#         i += 1
#         if numbers[i] - numbers[i-1] > 1:
#             return numbers[i] - 1
#
#
# print(find_missing(5, [1, 3, 2, 5]))
# print(find_missing(7, [6, 5, 1, 3, 2, 7]))
# print(find_missing(6, [6, 4, 1, 3, 2]))


"""
7. Creaza o clasa Calendar, care primeste ca unic parametru un an, si genereaza “calendarul” acelui an.
Se va tine cont de faptul daca anul este bisect sau nu.
Metode:
-> init(an) 
-> print_calendar(luna) - va printa calendarul pentru luna menționată intr-un format user-friendly, ex

October 2022
Mo 	Tu 	We 	Th 	Fr 	Sa 	Su
1 	2
3 	4 	5 	6 	7 	8 	9
10 	11 	12 	13 	14 	15 	16
17 	18 	19 	20 	21 	22 	23
24 	25 	26 	27 	28 	29 	30
31

-> get_day_of_week(zi, luna) - va returna ce zi din saptamna este, exemplu ‘Marti’
-> get_days_in_month(luna) - va returna numarul de zile din luna respectivă;
"""

import calendar


class Calendar:

    def __init__(self, year):
        self.year = year

    def print_calendar(self, month):
        _, num_days = calendar.monthrange(self.year, month)
        month_name = calendar.month_name[month]
        print(f'{month_name}, {self.year}')
        print('Mo  Tu  We  Th  Fr  Sa  Su')
        # Obținem ziua săptămânii pentru prima zi a lunii (0 - Monday, 1 - Tuesday, etc.)
        first_weekday = calendar.weekday(self.year, month, 1)
        # Adăugăm spații pentru a alinia prima zi a lunii cu ziua săptămânii corespunzătoare
        for _ in range(first_weekday):
            print("   ", end=" ")
        # Iterăm prin zilele lunii și le afisam
        for day in range(1, num_days+1):
            print(f'{day:2}', end='  ')
            # Trecem la următoarea linie când este sfârșitul săptămânii
            if (first_weekday + day) % 7 == 0:
                print()
        # Trecem la următoarea linie dacă ultima zi a lunii nu se termină într-o duminică
        if (first_weekday + num_days) % 7 != 0:
            print()


calendar_2023 = Calendar(2023)
for i in range(1, 13):
    calendar_2023.print_calendar(i)
