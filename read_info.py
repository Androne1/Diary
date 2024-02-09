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
    cur.execute("select * from students")
    teachers = cur.fetchall()
    headers = "№\tИмя\tФамилия\tОтчество\tПол\tНомер телефона\tДата рождения"
    print(headers)
    for teacher in teachers:
        print(*teacher, sep="\t")
    return teachers


@get_connection
def read_subjects_table(cur = None):
    cur.execute("select * from subjects")
    subjects = cur.fetchall()
    headers = "№\tНазвание\t№ учителя"
    print(headers)
    for subject in subjects:
        print(*subject, sep="\t")
    return subjects
