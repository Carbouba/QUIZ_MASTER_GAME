"""
Module de connexion aux bases de données SQLite du Quiz Master Game.

Responsabilité unique : établir les connexions aux deux bases de données :
  - db_record.db  : stocke le record (meilleur score) du joueur.
  - db_questions.db : stocke les questions et réponses (usage futur).

Les connexions et curseurs sont exportés pour être utilisés par db_call.py.
Si le fichier de base de données n'existe pas, SQLite le crée automatiquement.
"""

import os
import sqlite3

# Répertoire absolu de ce fichier, utilisé pour construire les chemins des BD
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ── Connexion à la base du record ─────────────────────────────────────────────
try:
    con = sqlite3.connect(os.path.join(BASE_DIR, "db_record.db"))
    cur = con.cursor()
except sqlite3.Error as error:
    print(f"Erreur SQLite (db_record) : {error}")

# ── Connexion à la base des questions ─────────────────────────────────────────
try:
    con2 = sqlite3.connect(os.path.join(BASE_DIR, "db_questions.db"))
    cur2 = con2.cursor()
except sqlite3.Error as error2:
    print(f"Erreur SQLite (db_questions) : {error2}")
