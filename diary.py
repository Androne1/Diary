import psycopg2
import random

database = {
    "database":"school",
    "user":"postgres",
    "password":"postgres",
    "host":"localhost",
    "port":5432
}
student_id = 1
teacher_id = 1
subject_id = 1

def get_connection(func):
    def wrapper():
        with psycopg2.connect(**database) as conn:
            with conn.cursor() as cur:
                func(cur)
    return wrapper

def check_field(field):
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    if not field:
        print("Вы забыли ввести значение поля")
        return False
    elif field_isdigit():
        print("Вы ввели число, а так нельзя")
        return False
    elif all([letter in alphabet for letter in field]):
        print('Вы ввели буквы не на русском')
        return False

@get_connection
def add_student(cur = None):
    global student_id
    create_table_students(cur)
    first_name = input('Назовите имя ученика')
    while not first_name or first_name.isdigit():
            first_name = input('Назовите имя ученика')
    second_name = input('Назовите фамилию ученика')
    while not second_name or second_name.isdigit():
            second_name = input('Назовите фамилию ученика')
    pater_name = input('Назовите отчество ученика')
    while not pater_name or pater_name.isdigit():
        pater_name = input('Назовите отчество ученика')
    gender = input('Назовте пол ученика: м или ж (при любом другом варианте пол будет случайным)')
    if gender == 'м' or gender == 'ж':
        random.choice(["м", "ж"])
    phone_number = input('Назовите номер телефона ученика')
    birthday = input('Назовите дату рождения ученика(пример:2008-08-14)')
    cur.execute(f"""
                insert into students
                values
                ({student_id}, {first_name}, {second_name}, {pater_name}, {gender}, {phone_number}, {birthday})
                """)
    student_id += 1
    
@get_connection
def add_teacher(cur = None):
        create_table_teachers(cur)
        global teacher_id
        first_name = input('Назовите имя учителя')
        second_name = input('Назовите фамилию учителя')
        pater_name = input('Назовите отчество учителя')
        gender = input('Назовте пол учителя: м или ж(при любом другом варианте пол будет случайным)')
        if gender == 'м' or gender == 'ж':
            random.choice(["м", "ж"])
        phone_number = input('Назовите номер телефона учителя')
        birthday = input('Назовите дату рождения учителя(пример:2008-08-14)')
        cur.execute(f"""
                    insert into students
                    values
                    ({teacher_id}, {first_name}, {second_name}, {pater_name}, {gender}, {phone_number}, {birthday})                        """)
        teacher_id += 1

@get_connection
def add_subject(cur = None):
        create_table_subjects(cur)
        subject_name = input('Назовите предмет')
        
def main_menu():
    print("Это школьный дневник")
    name = input("Как к вам обращаться?")
    teachers_list = []
    subject_list = []
    
    while True:
        print('1 - добавить ученика')
        print('2 - добавить учителя')
        print('3 - добавить предмет')
        print('4 - составить расписание')
        print('5 - постаавить оценку')
        print('6 - выйти из программы')
        action = input(f"Что вы хотите сделать, {name}")
        if action == '1':
            add_student()
        if action == '2':
            add_teacher()
        if action == '3':
            add_subject()
            
            

@get_connection
def create_table_students(cur = None):
    cur.execute("""
                create table if not exists students
                (
                    student_id int primary key,
                    first_name varchar(64) not null,
                    last_name varchar(64) not null,
                    pater_name varchar(64) not null,
                    gender varchar(1) not null,
                    phone_number varchar(16) not null,
                    birthday date not null
                )
                """)

def create_table_teachers(cur = None):
    cur.execute("""
                create table if not exists teachers
                (
                    teacher_id int primary key,
                    first_name varchar(64) not null,
                    last_name varchar(64) not null,
                    pater_name varchar(64) not null,
                    gender varchar(1) not null,
                    phone_number varchar(16) not null,
                    birthday date not null
                )
                """)

def create_table_schedule(cur = None):
    cur.execute("""
                create table if not exists students
                (
                    schedule_id int primary key,
                    day varchar(12) not null,
                    fk_subject_id int references subject(subject_id)
                )
                """)

@get_connection
def create_table_subjects(cur = None):
    cur.execute("""
                create table if not exists subjects
                (
                    subject_id int primary key,
                    subject_name varchar(128),
                    fk_teacher_id int references teachers(teacher_id)
                )
                """)

@get_connection
def create_table_marks(cur = None):
    cur.execute("""
                create table if not exists marks
                (
                    mark_id int primary key
                    fk_student_id references students(student_id)
                    fk_subject_id references subjects(subject_id)
                )
                """)