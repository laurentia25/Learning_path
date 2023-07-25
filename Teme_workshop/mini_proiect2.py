"""
TodoList
    Atribute: todo (dict, cheia e numele taskului, valoarea e descrierea)
La început nu avem taskuri, dict e gol

     Metode:
adauga_task(nume, descriere) - se va adauga in dict
finalizează_task(nume) - se va sterge din dict
afișează_todo_list() - doar cheile

Ramane ca TEMA:
afișează_detalii_suplimentare(nume_task) - în funcție de numele taskului, printăm detalii suplimentare.
    Dacă taskul nu e în todo list, întrebam utilizatorul dacă vrea să-l adauge.
    Dacă acesta răspunde nu - la revedere
    Dacă răspunde da - îi cerem detalii task și salvăm nume+detalii în dict
"""


class TodoList:
    def __init__(self):
        self.todo = {}

    def adauga_task(self, nume, descriere):
        self.todo[nume] = descriere

    def finalizeaza_task(self, nume):
        if nume in self.todo.keys():
            del self.todo[nume]
        else:
            print("Task inexistent")

    def afiseaza_todolist(self):
        for key in self.todo.keys():
            print(key)

    def check_todolist(self, action):
        print(self.todo.get(action, f'Nu exista acest task!'))
        response = input('Doriti sa il adaugam?')
        if response == 'da':
            detalii = input('Avem nevoie de mai multe detalii:')
            self.todo[action] = detalii
        else:
            print('La revedere!')


task = TodoList()
task.adauga_task('curatenie', 'la ora 10')
print(task.todo)

task.adauga_task('cumparaturi', 'la salar')
print(task.todo)

task.finalizeaza_task('curatenie')
print(task.todo)

task.finalizeaza_task("bani")
task.afiseaza_todolist()
print(task.todo)

task.adauga_task('sedinta', 'ora 11')
task.adauga_task('zi de nastere', 'petrecere')
task.afiseaza_todolist()

task.check_todolist('Plimbare')

task.afiseaza_todolist()
