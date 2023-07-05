"""

OOP - advance

Exerciții - studiu în workshopul de weekend

1. ABSTRACTION
Clasa abstractă FormaGeometrica
Conține un field PI=3.14
Conține o metodă abstractă aria (opțional)
Conține o metodă a clasei descrie() - aceasta printează pe ecran ‘Cel mai probabil am colturi’
"""
from abc import ABC, abstractmethod


class FormaGeometrica(ABC):
    PI = 3.14

    @abstractmethod
    def aria(self):
        pass

    def descrie(self):
        print('Cel mai probabil am colturi')


"""
2. INHERITANCE
Clasa Pătrat - moștenește FormaGeometrica
constructor pentru latură

ENCAPSULATION
latura este proprietate privată
Implementează getter, setter, deleter pentru latură
Implementează metoda cerută de interfață (opțional, doar dacă ai ales să implementezi metoda abstractă aria)
"""

class Patrat(FormaGeometrica):

    def __init__(self, latura):
        self.__latura = latura

    @property
    def latura(self):
        return self.__latura

    @latura.setter
    def latura(self, latura_noua):
        self.__latura = latura_noua


    @latura.deleter
    def latura(self):
        self.__latura = None

    def aria(self):
        return self.__latura * self.__latura

patrat1 = Patrat(15)
print(patrat1.latura)
print(patrat1.aria())
patrat1.latura = 5
print(patrat1.latura)

del patrat1.latura
print(patrat1.latura)


"""
3. Clasa Cerc - moștenește FormaGeometrica
constructor pentru rază
raza este proprietate privată
Implementează getter, setter, deleter pentru rază
Implementează metoda cerută de interfață - în calcul folosește field PI mostenit din clasa părinte (opțional, doar dacă ai ales să implementezi metoda abstractă aria)

POLYMORPHISM 
Definește o nouă metodă descrie - printează ‘Eu nu am colturi’
"""

class Cerc(FormaGeometrica):

    def __init__(self, raza):
        self.__raza = raza

    def aria(self):
        return self.__raza * self.PI

    def descrie(self):
        print('Eu nu am colturi')

    @property
    def raza(self):
        return self.__raza

    @raza.setter
    def raza(self, raza_noua):
        self.__raza = raza_noua

    @raza.deleter
    def raza(self):
        self.__raza = 0

cerc1 = Cerc(3)
print(cerc1.aria())
print(cerc1.raza)  # getter!
cerc1.raza = 5  # setter!
print(cerc1.raza)  # getter!
print(cerc1.aria())
cerc1.descrie()
del cerc1.raza  # deleter
print(cerc1.raza)  # getter!

"""
4. Creează un obiect de tip Pătrat și joacă-te cu metodele lui
Creează un obiect de tip Cerc și joacă-te cu metodele lui
"""

patrat2 = Patrat(10)
print(patrat2.aria())
patrat2.descrie() # metoda contine deja un print, prin urmare trebuie doar s-o apelez ca sa afiseze cv
print(patrat2.PI) # constanta la nivel de clasa parinte -> obiectul patrat o mosteneste, chiar daca nu are nevoie de ea


cerc2 = Cerc(6)
cerc2.descrie()
print(cerc2.aria())
