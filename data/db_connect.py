"""
    Ce fichier ne dispose que d'une seul responsablité : connecté la base des données.

    Un connecteur pour la BD db_record.db et un autre pour la db_questions.db.

    A chaque appele, le connecteur renvoi une connection a la BD le concernant.

    Si le fichier BD n'existe pas, il le crée automatiquement.
"""

import sqlite3
import os

BASE_DIRE = os.path.dirname(os.path.abspath(__file__))

try:
    con = sqlite3.connect(os.path.join(BASE_DIRE, "db_record.db"))
    cur = con.cursor()
except sqlite3.Error as er:
    print(f"Erreur SQLite : {er}")

try:
    con2 = sqlite3.connect(os.path.join(BASE_DIRE, "db_questions.db"))
    cur2 = con2.cursor()
except sqlite3.Error as er2:
    print(f"Erreur SQLite : {er2}")


