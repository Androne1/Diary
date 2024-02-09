from connection import *
from init import *
from read_info import *

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


def add_student_or_teacher(who, table_name, cur=None):
    create_table_students(cur)
    create_table_teachers(cur)
    first_name = input(f"Назовите имя {who}: ")
    while not first_name or first_name.isdigit():
        first_name = input(f"Назовите имя {who}: ")
    last_name = input(f"Назовите фамилию {who}: ")
    while not last_name or last_name.isdigit():
        last_name = input(f"Назовите фамилию {who}: ")
    pater_name = input(f"Назовите отчество {who}: ")
    while not pater_name or pater_name.isdigit():
        pater_name = input(f"Назовите отчество {who}: ")
    gender = input(
        f"Назовте пол {who}: м или ж (при любом другом варианте пол будет случайным): "
    )
    if not gender == "м" or not gender == "ж":
        random.choice(["м", "ж"])
    phone_number = input(f"Назовите номер телефона {who}: ")
    while len(phone_number) < 5 and not phone_number.isdigit:
        phone_number = input(f"Назовите номер телефона {who} без пробелов: ")
    birthday = input(f"Назовите дату рождения {who}(пример:2008-08-14): ")
    cur.execute(f"select count(*) from {table_name}")
    identificator = cur.fetchone()[0] + 1
    try:
        cur.execute(
            f"""
                    insert into {table_name}
                    values
                    ({identificator}, '{first_name}', '{last_name}', '{pater_name}', '{gender}', '{phone_number}', '{birthday}')
                    """
        )
        print("Новые значения добавлены в таблицу")
        return identificator, first_name, last_name, pater_name, gender, phone_number, birthday
        
    except:
        print("Что-то не так")

@get_connection
def add_student(cur = None):
    add_student_or_teacher("ученика", "students", cur)

@get_connection
def add_teachers(cur = None):
    global teachers_list
    identificator, first_name, last_name, pater_name, gender, phone_number, birthday = add_student_or_teacher("учителя", "teachers", cur)
    teachers_list.append((first_name, last_name, pater_name))
    


# @get_connection
# def add_student(cur = None):
#     global student_id
#     create_table_students(cur)
#     first_name = input('Назовите имя ученика: ')
#     while not first_name or first_name.isdigit():
#         first_name = input('Назовите имя ученика: ')
#     last_name = input('Назовите фамилию ученика: ')
#     while not last_name or last_name.isdigit():
#         last_name = input('Назовите фамилию ученика: ')
#     pater_name = input('Назовите отчество ученика: ')
#     while not pater_name or pater_name.isdigit():
#         pater_name = input('Назовите отчество ученика: ')
#     gender = input('Назовте пол ученика: м или ж (при любом другом варианте пол будет случайным): ')
#     if not gender == 'м' or not gender == 'ж':
#         random.choice(["м", "ж"])
#     phone_number = input('Назовите номер телефона ученика: ')
#     while len(phone_number) < 5 and not phone_number.isdigit:
#         phone_number = input("Назовите номер телефона ученика без пробелов: ")
#     birthday = input('Назовите дату рождения ученика(пример:2008-08-14): ')
#     try:
#         cur.execute(f"""
#                     insert into students
#                     values
#                     ({student_id}, '{first_name}', '{last_name}', '{pater_name}', '{gender}', '{phone_number}', '{birthday}')
#                     """)
#         print("Добавлен новый ученик")
#         student_id += 1
#         return main_menu()
#     except:
#         print('Что-то не так')
#         return add_student()

# @get_connection
# def add_teacher(cur = None):
#     create_table_teachers(cur)
#     global teacher_id
#     global teachers_list
#     first_name = input('Назовите имя учителя: ')
#     last_name = input('Назовите фамилию учителя: ')
#     pater_name = input('Назовите отчество учителя: ')
#     gender = input('Назовте пол учителя: м или ж(при любом другом варианте пол будет случайным): ')
#     if gender == 'м' or gender == 'ж':
#         random.choice(["м", "ж"])
#     phone_number = input('Назовите номер телефона учителя: ')
#     while len(phone_number) < 5 and not phone_number.isdigit:
#         phone_number = input("Назовите номер телефона учителя без пробелов: ")
#     birthday = input('Назовите дату рождения учителя(пример:2008-08-14): ')
#     try:
#         cur.execute(f"""
#                     insert into teachers
#                     values
#                     ({teacher_id}, {first_name}, {last_name}, {pater_name}, {gender}, {phone_number}, {birthday})
#                     """)
#         print('Добавлен новый учитель')
#         teachers_list.append((first_name, last_name, pater_name))
#         teacher_id += 1
#         return main_menu()
#     except:
#         print("Что-то не так")
#         return add_teacher()

@get_connection
def add_subject(cur = None):
    global teachers_list
    create_table_subjects(cur)
    teachers_list = read_teachers_table(cur)
    subject_name = input('Назовите предмет: ')
    teacher_first_name = input("Назовите имя учителя, ведущего данный предмет: ")
    if teachers_list.count(teacher_first_name) == 0:
        input("Введите имя учителя, который есть в списке: ")
    teacher_last_name = input("Назовите фамилию учителя, ведущего данный предмет: ")
    if teachers_list.count(teacher_last_name) == 0:
        input("Введите фамилию учителя, который есть в списке: ")
    teacher_pater_name = input("Назовите отчество учителя, ведущего данный предмет: ")
    if teachers_list.count(teacher_pater_name) == 0:
        input("Введите отчество учителя, который есть в списке: ")
    if (teacher_first_name, teacher_last_name, teacher_pater_name) in teachers_list:
        fk_teacher_id = teachers_list.index(teacher_first_name) + 1
        cur.execute("""
                    select count(*) from subjects
                    """)
        subject_id = cur.fetchone[0]()
        try:
            cur.execute(f"""
                        insert into subjects
                        values
                        ({subject_id}, {subject_name}, {fk_teacher_id})
                        """)
            subject_id += 1
        
        except:
            print("Что-то не так")
    else:
        print("Такого учителя нет в списке")

def make_schedule(cur = None):
    global schedule_id

@get_connection
def add_mark(cur = None):
    read_students_table(cur)
    identificator = ""
    while not identificator.isdigit:
        identificator = input("Какому ученику ставим оценку?")
    identificator = int(identificator)
    try:
        cur.execute("""
                    select *
                    from students
                    where students=%s
                    """%(identificator))
    except:
        print("Нет такого ученика")
        return None
    
def quit(cur = None):
    return False

def greeting(cur = None):
    global name
    print("Это школьный дневник")
    name = input("Как к вам обращаться? ")
    return main_menu()

def main_menu(cur = None):
    global name
    
    run = True
    while run:
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
            add_teachers(cur)
        if action == '3':
            add_subject(cur)
        if action == '4':
            make_schedule(cur)
        if action == '6':
            run = quit(cur)
        input("Нажмите Enter для продолжения")


greeting()
