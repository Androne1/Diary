from connection import *
from init import *

def check_field(field):
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    if not field:
        print("Вы забыли ввести значение поля")
        return False
    elif field.isdigit():
        print("Вы ввели число, а так нельзя")
        return False
    elif all([letter in alphabet for letter in field]):
        print('Вы ввели буквы не на русском')
        return False

@get_connection
def add_student(cur = None):
    global student_id
    create_table_students(cur)
    first_name = input('Назовите имя ученика: ')
    while not first_name or first_name.isdigit():
        first_name = input('Назовите имя ученика: ')
    second_name = input('Назовите фамилию ученика: ')
    while not second_name or second_name.isdigit():
        second_name = input('Назовите фамилию ученика: ')
    pater_name = input('Назовите отчество ученика: ')
    while not pater_name or pater_name.isdigit():
        pater_name = input('Назовите отчество ученика: ')
    gender = input('Назовте пол ученика: м или ж (при любом другом варианте пол будет случайным): ')
    if not gender == 'м' or not gender == 'ж':
        random.choice(["м", "ж"])
    phone_number = input('Назовите номер телефона ученика: ')
    while len(phone_number) < 5 and not phone_number.isdigit:
        phone_number = input("Назовите номер телефона ученика: ")
    birthday = input('Назовите дату рождения ученика(пример:2008-08-14): ')
    try:
        cur.execute(f"""
                    insert into students
                    values
                    ({student_id}, '{first_name}', '{second_name}', '{pater_name}', '{gender}', '{phone_number}', '{birthday}')
                    """)
        print("Добавлен новый ученик")
        return main_menu()
    except:
        print('Что-то не так')
    student_id += 1

@get_connection
def add_teacher(cur = None):
        create_table_teachers(cur)
        global teacher_id
        first_name = input('Назовите имя учителя: ')
        second_name = input('Назовите фамилию учителя: ')
        pater_name = input('Назовите отчество учителя: ')
        gender = input('Назовте пол учителя: м или ж(при любом другом варианте пол будет случайным): ')
        if gender == 'м' or gender == 'ж':
            random.choice(["м", "ж"])
        phone_number = input('Назовите номер телефона учителя: ')
        while len(phone_number) < 5 and not phone_number.isdigit:
            phone_number = input("Назовите номер телефона ученика: ")
        birthday = input('Назовите дату рождения учителя(пример:2008-08-14): ')
        try:
            cur.execute(f"""
                        insert into students
                        values
                        ({teacher_id}, {first_name}, {second_name}, {pater_name}, {gender}, {phone_number}, {birthday})
                        """)
            print('Добавлен новый учитель')
            return main_menu()
        except:
            print("Что-то не так")
        teacher_id += 1

@get_connection
def add_subject(cur = None):
    create_table_subjects(cur)
    subject_name = input('Назовите предмет: ')

def go_out(cur = None):
    return

def greeting(cur = None):
    print("Это школьный дневник")
    name = input("Как к вам обращаться? ")
    return main_menu()
    
def main_menu(cur = None):
    global name
    teachers_list = []
    subject_list = []
    while True:
        print('1 - добавить ученика')
        print('2 - добавить учителя')
        print('3 - добавить предмет')
        print('4 - составить расписание')
        print('5 - постаавить оценку')
        print('6 - выйти из программы')
        action = input(f"Что вы хотите сделать, {name}? ")
        if action == '1':
            add_student(cur)
        if action == '2':
            add_teacher(cur)
        if action == '3':
            add_subject(cur)
        if action == '6':
            go_out(cur)


greeting()