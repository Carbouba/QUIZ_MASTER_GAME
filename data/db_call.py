"""
    Ce fichier a la responsablité de faire appelle a la BD.

    il s'aoccupe des requetes d'entrées et sorties 

    chaque fonction ici joue un role
"""

from db_connect import con, cur, cur2, con2
from questions import get_question


def init_db():


    cur.execute("""
            CREATE TABLE IF NOT EXISTS current_record (
                record INTEGER
            )
        """)
    con.commit()

def insert_record(new_record):


    #cur.execute("INSERT INTO current_record (record) VALUES (?)", (new_record,))
    #cur.execute("DELETE FROM current_record")
    cur.execute("UPDATE current_record SET record = ?", (new_record,))
    con.commit()


def get_record():


    cur.execute("SELECT record FROM current_record")
    res = cur.fetchone()

    rec = res[0]

    return rec

# def insert_question():


#     cur2.execute("""
#             CREATE TABLE IF NOT EXISTS questions (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT, 
#                 question TEXT,
#                 reponse TEXT
#             )
#         """)
#     con2.commit()

#     dico = get_question()

#     for Q, R in dico.items():
#         quest = Q
#         res = R

#         cur2.execute("SELECT * FROM questions WHERE question = ?", (quest,))
        
#         if not cur2.fetchall():
#             cur2.execute("INSERT INTO questions (question, reponse) VALUES (?, ?)", (quest, res))
#             # #cur.execute("DELETE FROM current_record")
#             # #cur.execute("UPDATE current_record SET record = ?", (new_record,))
#             con2.commit()
