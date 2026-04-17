"""
Module de requêtes vers les bases de données du Quiz Master Game.

Responsabilité : encapsuler toutes les opérations d'entrée/sortie (CRUD)
sur la base de données. Chaque fonction a un rôle précis et unique.

Fonctions disponibles :
  - init_db()         : crée la table si elle n'existe pas encore.
  - insert_record()   : met à jour le record en base de données.
  - get_record()      : récupère le record actuel depuis la base de données.
"""

from db_connect import con, cur


def init_db():
    """Crée la table 'current_record' si elle n'existe pas encore."""
    cur.execute("""
        CREATE TABLE IF NOT EXISTS current_record (
            record INTEGER
        )
    """)
    con.commit()


def insert_record(new_record):
    """Met à jour le record en base de données avec la valeur fournie.

    Args:
        new_record (int): Le nouveau score à enregistrer comme record.
    """
    cur.execute("UPDATE current_record SET record = ?", (new_record,))
    con.commit()


def get_record():
    """Récupère le record actuel depuis la base de données.

    Returns:
        int: La valeur du record enregistré en base.
    """
    cur.execute("SELECT record FROM current_record")
    result = cur.fetchone()
    return result[0]
