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
