from connection import get_connection


@get_connection
def read_students_table(cur=None):
    cur.execute("select * from students")
    students = cur.fetchall()
    headers = "№\tИмя\tФамилия\tОтчество\tПол\tНомер телефона\tДата рождения"
    print(headers)
    for student in students:
        print(*student, sep="\t")


@get_connection
def read_teachers_table(cur=None):
    cur.execute("select * from teachers")
    teachers = cur.fetchall()
    headers = "№\tИмя\tФамилия\tОтчество\tПол\tНомер телефона\tДата рождения"
    print(headers)
    lst = []
    for teacher in teachers:
        print(*teacher, sep="\t")
        lst.append(teacher)


@get_connection
def read_subjects_table(cur = None):
    cur.execute("select * from subjects")
    subjects = cur.fetchall()
    headers = "№\tНазвание\t№ учителя"
    print(headers)
    for subject in subjects:
        print(*subject, sep="\t")
    return subjects


@get_connection
def read_marks_table(cur=None):
    cur.execute("select * from marks")
    marks = cur.fetchall()
    headers = "№\tОценка\t№ ученика\t№ предмета"
    print(headers)
    for mark in marks:
        print(*mark, sep="\t")
    return marks

@get_connection
def read_student_result(cur=None):
    read_students_table()
    student_id = ""
    while not student_id.isdigit():
        student_id = input("Введите номер ученика: ")
    student_id = int(student_id)
    cur.execute(f"""
                select first_name, last_name, pater_name, subject_name, avg(mark)
                from marks
                inner join students on fk_student_id = students.student_id
                inner join subjects on fk_subject_id = subjects.subject_id
                where fk_student_id = {student_id}
                group by first_name, last_name, pater_name, subject_name;
                """)
    results = cur.fetchall()
    headers = "Имя\tФамилия\tОтчество\tПредмет\tУспеваемость"
    print(headers)
    for record in results:
        print(*record, sep="\t")
    return results