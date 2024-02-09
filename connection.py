import psycopg2
import random

database = {
    "database":"school",
    "user":"postgres",
    "password":"postgres",
    "host":"localhost",
    "port":5432
}
subject_id = 1
schedule_id = 1

teachers_list = []

def get_connection(func):
    def wrapper(cur = None):
        with psycopg2.connect(**database) as conn:
            with conn.cursor() as cur:
                func(cur)
    return wrapper