from connection import get_connection

@get_connection
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

@get_connection
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
                    mark_id int primary key,
                    mark varchar(1) not null,
                    fk_student_id int references students(student_id),
                    fk_subject_id int references subjects(subject_id)
                )
                """)


@get_connection
def create_table_students(cur=None):
    cur.execute(
        """
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
                """
    )
