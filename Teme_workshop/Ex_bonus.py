"""
1. Implementeaza o clasa Employee.
Atribute:
- id
- name
- salary
- department

Metode:
- assign_department - schimba departamentul angajatului.
- print_employee_details - afiseaza detaliile despre angajat
- calculate_salary - calculeaza salariul angajatului.
Aceasta metoda ia doua argumente: salary si hours_worked.
Daca angajatul a lucrat mai mult de 50 de ore, atunci la salariu
se va adauga plata pe overtime, aceasta fiind orele extra * salariu/50.
"""


# class Employee:
#     def __init__(self, id, name, salary, department):
#         self.id = id
#         self.name = name
#         self.salary = salary
#         self.department = department
#
#     def assign_department(self, new_department):
#         self.department = new_department
#         return f'The new department of the employee {self.name} is {self.department}'
#
#     def print_employee_details(self):
#         return f'{self.id} | {self.name} | {self.salary} | {self.department}'
#
#     def calculate_salary(self, salary, hours_worked):
#         if hours_worked > 50:
#             salary = salary + (hours_worked-50) * salary/50
#             return f'Salary + OT payment = {salary}'
#         else:
#             return f'Salary = {salary}'
#
#
# employee1 = Employee('E7876', 'ADAMS', 50000, 'Accounting')
# print(employee1.print_employee_details())
# print(employee1.assign_department('Finance'))
# print(employee1.calculate_salary(60000, 75))
# print(employee1.calculate_salary(60000, 45))

"""
2. 
Clasa MenuItem:
- atribute: id, nume, ingrediente, cantitate, pret, alergeni, categorie
- metode:
    -- print_menu_item - afiseaza detaliile despre preparat

Clasa Restaurant:
- atribute: 
    -- nume
    -- menu_items (o lista cu elemente de tip MenuItem)
    -- booked_tables

- metode:
    -- add_items_to_menu
    -- delete_item_from_menu
    -- reserve_table
    -- print_menu
    -- print_booked_tables
"""


# class MenuItem:
#     def __init__(self, id, nume, ingrediente, cantitate, pret, alergeni, categorie):
#         self.id = id
#         self.nume = nume
#         self.ingrediente = ingrediente
#         self.cantitate = cantitate
#         self.pret = pret
#         self.alergeni = alergeni
#         self.categorie = categorie
#
#     def print_menu_item(self):
#         print(f'Detalii: {self.id}, {self.nume}, {self.ingrediente}, {self.cantitate}, {self.pret}, {self.alergeni}, {self.categorie}')
#
#
# class Restaurant(MenuItem):
#     def __init__(self, id, ingrediente, cantitate, pret, alergeni, categorie, nume, menu_items, booked_tables):
#         super().__init__(id, nume, ingrediente, cantitate, pret, alergeni, categorie)
#         self.menu_items = menu_items
#         self.booked_tables = booked_tables
#
#     def add_items_to_menu(self, new_menu_item):
#         self.menu_items.append(new_menu_item)
#         return self.menu_items
#
#     def delete_item_from_menu(self, item_to_delete):
#         self.menu_items.remove(item_to_delete)
#         return self.menu_items
#
#     def reserve_table(self):
#         self.booked_tables += 1
#         return f'Your table is booked!'
#
#     def print_menu(self):
#         print(self.menu_items)
#
#     def print_booked_tables(self):
#         print(self.booked_tables)
#
#
# restaurant = Restaurant(1,
#     ['rosii', 'busuioc', 'usturoi', 'paine'],
#     ['2 buc', '7 frunze', '3 catei', '4 felii'],
#     '25 lei',
#     'busuioc',
#     'aperitive',
#     'Bruschette',
#     ['salata greceasca', 'paste', 'legume grill', 'bruschette'],
#     7)
#
# restaurant.add_items_to_menu('piept de pui cu ciuperci')
# restaurant.print_menu()
# restaurant.delete_item_from_menu('paste')
# restaurant.print_menu()
# restaurant.print_booked_tables()
# print(restaurant.reserve_table())
# restaurant.print_booked_tables()
# restaurant.print_menu_item()


"""
3. Clasa BankAccount
- atribute:
    -- account_number
    -- balance
    -- customer_name
- metode:
    -- withdraw
    -- deposit
    -- check_balance
"""


# class BankAccount:
#     def __init__(self, account_number, balance, customer_name):
#         self.account_number = account_number
#         self.balance = balance
#         self.customer_name = customer_name
#
#
#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print(f'Successful withdraw for {amount}.New balance:{self.balance} lei')
#             return self.balance
#         else:
#             print('Insufficient funds!')
#             return self.balance
#
#     def deposit(self, amount):
#         self.balance += amount
#         print(f'Successful deposit for {amount}. New balance:{self.balance} lei')
#
#     def check_balance(self):
#         print(f"{self.account_number} account's balance is {self.balance} lei")
#
#
# account = BankAccount('97684738546835', 3000, 'Ioana Popescu')
# account.deposit(1000)
# account.withdraw(5000)
# account.withdraw(3000)
# account.check_balance()



"""
4. Implementeaza un decorator care converteste rezultatul returnat de
o functie la int. Daca conversia nu se poate face, trebuie afisat
un mesaj sugestiv ca nu s-a facut conversia (hint: foloseste-te de
try-except in implementarea decoratorului)
"""


# def converter(func):
#     def wrapper_func():
#         result = func()  # Call the input function
#         try:
#             a = int(result)  # Convert the result to float
#             return a
#         except ValueError:
#             print('Conversia nu poate fi facuta!')
#         except TypeError:
#             print('Conversia nu poate fi facuta!')
#     return wrapper_func
#
#
# def number():
#     return 1.6
#
#
# converted_result = converter(number)
# print(converted_result())
#
#
# def abd():
#     b = 1.1
#     return b
#
#
# d = converter(abd)
# print(d())

"""
5. Implementeaza un decorator ca limiteaza call-ul functiei decorate la 3.
"""


def count_calls_decorator(func):
    def wrapper_func(*args, **kwargs):

        result = func(*args, **kwargs)
        return result
    wrapper_func.call_count = 0
    return wrapper_func

@count_calls_decorator
def number():
    return 1

number()

number()

n = count_calls_decorator(number())
print(n)