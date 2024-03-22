import sqlite3
import datetime
import random


def get_connection(func):
    def wrapper(cur=None, *args, **kwargs):
        with sqlite3.connect("database.db") as conn:
            cur = conn.cursor()
            func(cur)
    return wrapper

def logger(record):
    with open("journal.log", "a", encoding = "utf-8") as file:
        file.write(str(datetime.datetime.now()) + " " + record + "\n")

@get_connection
def create_table_songs(cur=None):
    cur.execute("""
                create table if not exists music
                (
	                song_id int primary key,
	                song_name text not null,
                    band_name text not null,
	                mood text
                )
                """)
    logger("Таблица успешно создна")

@get_connection
def add_music(cur=None):
    global song_name, band_name, mood
    cur.execute("select count(*) from music")
    music_id = cur.fetchone()[0] + 1
    cur.execute(f"""
                select *
                from music
                where (song_name='{song_name}' and band_name='{band_name}');
                """)
    is_film_there = cur.fetchone()
    if is_film_there:
        return None
    try:
        cur.execute(f"""
                    insert into music
                    values
                    ({music_id}, '{song_name}', '{band_name}', '{mood}')
                    """)
        return True
    except:
        return False

@get_connection
def delete_music(cur=None):
    global song_name, band_name
    try:
        cur.execute(f"delete from music where song_name = '{song_name}' and band_name = '{band_name}'")
        # cur.execute("select * from music")
        # music = cur.fetchall()
        # cur.execute("delete * from music")
        # for iden, song in enumerate(music, start = 1):
        #     music_id, song_name, band_name, mood = song
        #     cur.execute(f"""
        #                 insert into music
        #                 values
        #                 ({iden}, '{song_name}', '{band_name}', '{mood}')
        #                 """)
        return True
    except:
        return False

@get_connection
def get_music(cur=None):
    global mood
    cur.execute(f"select * from music where mood = '{mood}'")
    music = cur.fetchall()
    return random.choice(music)

song_name = "Awake and alive"
band_name = "Skillet"
mood = "energy"
# delete_music()
# add_music()
get_music()
# create_table_songs()