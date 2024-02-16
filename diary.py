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
    cancel()
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
        if cancel == False:
            print("Операция преравна")
            return None

@get_connection
def add_student(cur = None):
    add_student_or_teacher("ученика", "students", cur)

@get_connection
def add_teachers(cur = None):
    global teachers_list
    identificator, first_name, last_name, pater_name, gender, phone_number, birthday = add_student_or_teacher("учителя", "teachers", cur)
    teachers_list.append((first_name, last_name, pater_name))

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
        cancel()
        subject_id = cur.fetchone[0]()
        try:
            cur.execute(f"""
                        insert into subjects
                        values
                        ({subject_id}, '{subject_name}', {fk_teacher_id})
                        """)        
        except:
            print("Что-то не так")
    else:
        print("Такого учителя нет в списке")
        if cancel == False:
            print("Операция преравна")
            return None

def make_schedule(cur = None):
    global schedule_id

@get_connection
def add_mark(cur = None):
    create_table_marks(cur)
    read_students_table(cur)
    identificator = ""
    while not identificator.isdigit:
        identificator = input("Какому ученику ставим оценку?")
    identificator = int(identificator)
    try:
        cur.execute("""
                    select *
                    from students
                    where student_id=%s
                    """%(identificator))
    except:
        print("Нет такого ученика")
        return None
    read_subjects_table(cur)
    subject_id = ""
    while not subject_id.isdigit:
        subject_id = input("По какому предмету ставим оценку?")
    subject_id = int(subject_id)
    try:
        cur.execute(
            """
                    select *
                    from subjects
                    where subject_id=%s
                    """
            % (subject_id)
        )
    except:
        print("Нет такого предмета")
        return None
    mark = ""
    while mark not in "12345н":
        mark = input("Какую оценку ставим(1 - 5 или н)? ")
    cancel()
    cur.execute(
        """
                    select count(*) from subjects
                    """
    )
    mark_id = cur.fetchone()[0]
    try:
        cur.execute(f"""
                    insert into marks
                    values
                    ({mark_id}, '{mark}', {identificator}, {subject_id})
                    """)
    except:
        print("Что-то не так")
        if cancel == False:
            print("Операция преравна")
            return None

def cancel():
    answer = ""
    while answer != "Да" or answer != "Нет":
        answer = input("Вы подтверждаете операцию(Да или Нет)? ")
        if answer == "Да":
            return True
        else:
            return False

def quit():
    return False

def greeting():
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
        print('5 - поставить оценку')
        print('6 - посмотреть всех учеников')
        print("7 - посмотреть всех учеников(м)")
        print("8 - посмотреть всех учеников(ж)")
        print("9 - посмотреть всех учителей")
        print("10 - посмотреть все предметы")
        print('11 - посмотреть расписание')
        print('12 - посмотреть оценки')
        print('13 - выйти из программы')
        print('14 - инициализировать таблицы')
        action = input(f"Что вы хотите сделать, {name}? ")
        if action == '1':
            add_student(cur)
        if action == '2':
            add_teachers(cur)
        if action == '3':
            add_subject(cur)
        if action == '4':
            make_schedule(cur)
        if action == '5':
            add_mark(cur)
        if action == "6":
            read_students_table(cur)
        if action =='9':
            read_teachers_table(cur)
        if action == '10':
            read_subjects_table(cur)
        if action == '12':
            read_marks_table(cur)
        if action == '13':
            run = quit(cur)
        if action == '14':
            create_all_tables()
        input("Нажмите Enter для продолжения")

def create_all_tables():
    create_table_students()
    create_table_teachers()
    create_table_subjects()
    create_table_marks()
    create_table_schedule()

greeting()
