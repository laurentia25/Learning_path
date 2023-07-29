"""
Pachete python. Interacțiune cu fișiere.

1. Create a text file called “hello.txt” and add the following text inside of it:
Python
Java
Javascript
C/C++/C#
PHP
Node.js

Write a short program to read and display the text file
"""
# import csv

# with open('hello.txt', 'w') as f:
#     f.writelines(['Python\n',
#                   'Java\n',
#                   'Javascript\n',
#                   'C/C++/C#\n',
#                   'PHP\n',
#                   'Node.js\n'])
#
# with open('hello.txt', 'r') as f:
#     print(f.read())


# def read_file(file_path):
#     with open(file_path, 'r'):
#         return f.readlines()
#
#
# read_file('hello.txt')

"""
2. Write a short program to append the following lines to “hello.txt”
(you will use a list of strings and a for-loop):
Go
Kotlin
Swift

Display the new contents of the file.
"""

# words = ['Go\n', 'Kotlin\n', 'Swift\n']
#
# for word in words:
#     with open('hello.txt', 'a') as f:
#         f.writelines(word)
# #
# with open('hello.txt', 'r') as f:
#     lines = f.readlines()
#     for line in lines:
#         print(line)

"""
3. Write a short program that reads the “hello.txt” file and displays every other line
(only odd lines).
"""
# Varianta 1:
# with open('hello.txt', 'r') as f:
#     lines = f.readlines()
#     for line in lines:
#         if lines.index(line) % 2 == 0:
#             print(line)

# Vaianta 2:
# with open('hello.txt', 'r') as f:
#     lines = f.readlines()
#     for index, line in enumerate(lines):
#         if (index + 1) % 2 == 0:
#             print(line)

# Varianta 3:
# with open('hello.txt', 'r') as f:
#     lines = f.readlines()
#     for line in range(1, len(lines), 2):
#         print(lines[line])

"""
4. Write a program that generates 26 text files, called `A.txt`, `B.txt`, … `Z.txt`. 
Each file will contain the sentences below:

My name is letter X.
I am the 24th letter of the alphabet.

Make sure you use the correct ending for the letter’s number (e.g. 1st, 2nd, 3rd, etc.)
"""


# Determinare index cu codul ascii:

# for letter in letters:
#     print(letter)
#     print ord(letter)
#     index = ord(letter) - ord('A')


# import string
# index = 0
# letters = string.ascii_uppercase
# print(letters)
# for letter in range(len(letters)):
#     with open(f'{letters[index]}.txt', 'w') as file:
#         if index == 0 or index == 20:
#             file.writelines([f'My name in letter {letters[index]}\n',
#                              f'I am the {index + 1}st letter of the alphabet\n'])
#         elif index == 1 or index == 21:
#             file.writelines([f'My name in letter {letters[index]}\n',
#                              f'I am the {index + 1}nd letter of the alphabet\n'])
#         elif index == 2 or index == 22:
#             file.writelines([f'My name in letter {letters[index]}\n',
#                              f'I am the {index + 1}rd letter of the alphabet\n'])
#         else:
#             file.writelines([f'My name in letter {letters[index]}\n',
#                             f'I am the {index + 1}th letter of the alphabet\n'])
#     index += 1

"""
5. Create a csv file called “students.csv” and add the following text inside of it:
id,fname,lname,age,grade
1,Maria,Popescu,31,7.5
2,Andrei,Ionescu,26,8.0
3,Adriana,Marinescu,21,7.5
4,Matei,Gheorghescu,42,8.5
5,Eusebiu,Pop,33,9.5
6,Ioana,Popa,29,9.0"""

import csv
# data = [
#         ['id', 'fname', 'lname', 'age', 'grade'],
#         ['1', 'Maria', 'Popescu', '31', '7.5'],
#         ['2', 'Andrei', 'Ionescu', '26', '8.0'],
#         ['3', 'Adriana', 'Marinescu', '21', '7.5'],
#         ['4', 'Matei', 'Gheorghescu', '42', '8.5'],
#         ['5', 'Eusebiu', 'Pop', '33', '9.5'],
#         ['6', 'Ioana', 'Popa', '29', '9.0']
#         ]
# with open('students1.csv', 'w', newline="\n") as csv_file:
#     writer = csv.writer(csv_file)
#     writer.writerows(data)


"""Read the file using Python’s `csv` standard library, and display it 
in the terminal as a table, using the options for string formatting from Python:


id	fname		lname		age	grade
---------------------------------------------------
1	Maria		Popescu		31	7.5
2	Andrei		Ionescu		26	8.0
3	Adriana		Marinescu	21	7.5
4	Matei		Gheorghescu	42	8.5
5	Eusebiu		Pop			33	9.5
6	Ioana		Popa		29	9.0
"""

# rows = []
# with open('students1.csv', 'r') as f:
#     reader = csv.reader(f, delimiter=',')
#     for row in reader:
#         rows.append(row)
#
# header_row = ['id', 'fname', 'lname', 'age', 'grade']
# print('\t'.join(header_row))
# print('-' * 40)
#
# # Print the data rows
# for row in rows:
#     print('\t'.join(row))

"""
6. Read again the information from the csv file above, store it all in a list of data, and then write a new file,
called “students.json”, which will contain a valid JSON object. 

Use the following format for each student (and use Python’s standard JSON module):
[
    {
        "id": 1,
        "fname": "Maria",
        "lname": "Popescu",
        "age": 31,
        "grade": 7.5
    },
    ...
]
"""
# students = []
# with open('students1.csv', 'r') as csv_f:
#     reader = csv.DictReader(csv_f)
#     for row in reader:
#         students.append(row)
# print(students)
