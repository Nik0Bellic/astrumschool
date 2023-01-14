import sqlite3
from typing import Set
from database.structs import Tutor

# class DBPupilManager:
#     def __init__(self) -> None:
#         self.connection = sqlite3.connect("pupils.db")
#         self.cursor = self.connection.cursor()
#         self.cursor.execute("DROP TABLE IF EXISTS pupils")
#         self.cursor.execute("CREATE TABLE IF NOT EXISTS pupils (id INTEGER PRIMARY KEY, name TEXT, subjects TEXT, grade INTEGER)")
#         self.connection.commit()

#     def add_user(self, user: User) -> None:
#         self.cursor.execute("INSERT INTO pupils VALUES (?, ?, ?, ?)", (user.id, user.name, str(user.subjects), user.grade))
#         self.connection.commit()
    
#     def get_user(self, id_: int):
#         self.cursor.execute("SELECT * FROM pupils WHERE id = ?", (id_,))
#         user = self.cursor.fetchone()

#         parsed_subjects = set()
#         set_string = user[2][1:-1]
#         for i in set_string.split(", "):
#             parsed_subjects.add(int(i))
#         return User(user[0], user[1], parsed_subjects, user[3])

#     def update_user_subjects(self, id_: int, subjects: Set[int]) -> None:
#         self.cursor.execute("UPDATE pupils SET subjects = ? WHERE id = ?", (str(subjects), id_))
#         self.connection.commit()
        
        
# def sql_start():
#     conn = sq.connect('tutors.db')
#     if conn:
#         print('Db connected')
#     with conn:
#         conn.execute("CREATE TABLE IF NOT EXISTS tutors (id TEXT PRIMARY KEY, name TEXT, subjects TEXT, grade INTEGER, busy BOOLEAN default FALSE)")
#     conn.close()
    

# def add_tutor(state):
#     conn = sq.connect('tutors.db')
#     with conn.cursor() as cur:
#         with state.proxy() as data:
#             cur.execute("INSERT INTO tutors VALUES (?, ?, ?, ?)", tuple(data.values()))
#     conn.close()
        


class DBTutorManager:
    connection = sqlite3.connect("tutors.db")
    
    def __init__(self, force=False) -> None:
        
        if force:
            conn = self.connection
            cur = conn.cursor()
            
            try:
                cur.execute("DROP TABLE IF EXISTS tutors")
            except:
                print('error dropping')
                
            cur.execute("CREATE TABLE IF NOT EXISTS tutors (id TEXT PRIMARY KEY, name TEXT, subjects TEXT, grade INTEGER, busy BOOLEAN default FALSE)")
            
            conn.commit()
            print('dropped')

    def add_tutor(self, state, username) -> None:
        conn = self.connection
        cur = conn.cursor()
        with state.proxy() as data:
            cur.execute("INSERT INTO tutors VALUES (?, ?, ?, ?)", username + tuple(data.values()))
        conn.commit()
    
    # async def get_tutor(self, id_: int):
    #     self.cursor.execute("SELECT * FROM tutors WHERE id = ?", (id_,))
    #     tutor = self.cursor.fetchone()

    #     parsed_subjects = set()
    #     set_string = tutor[2][1:-1]
    #     for i in set_string.split(", "):
    #         parsed_subjects.add(int(i))
    #     return Tutor(tutor[0], tutor[1], parsed_subjects, tutor[2])

    # async def update_tutor_subjects(self, id_: int, subjects: Set[int]) -> None:
    #     self.cursor.execute("UPDATE tutors SET subjects = ? WHERE id = ?", (str(subjects), id_))
    #     self.connection.commit()


# # db_user = DBPupilManager()
db_tutor = DBTutorManager()