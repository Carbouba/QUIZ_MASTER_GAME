"""
    Ce ficihier contient le dictionnaire des questions reponses.
    Le choix d'un dictionnaire permet de lier une question à sa reponse

    Ici la fonction get_question() renvoie le dictionnaire entier a celui qui l'appele,
    facilitant ainsi l'import du module 
    
"""

def get_question():
    # Dictionnaire contenant les questions et leurs reponses
    # Ici chaque question est une 'clé' et la reponse est la 'valeur' les deux sont liées
    Questions = {
        "Quelle est la capitale du Niger ?": "Niamey",
        "En quelle année le Niger a-t-il obtenu \nson indépendance ?": "1960",
        "Comment s'appelle la célèbre viande séchée \net épicée du Niger ?": "Kilishi",
        "Quel grand fleuve traverse le sud-ouest \ndu pays ?": "Niger",
        "Quelle ville est célèbre pour sa grande \nmosquée en terre et son désert ?": "Agadez",
        "Quel est le surnom de l'équipe nationale \nde football du Niger ?": "Mena",
        "Quelle est la monnaie utilisée au Niger ?": "CFA",
        "Quel animal est le symbole national \ndu Niger ?": "Gazelle",
        "Combien de couleurs y a-t-il sur le drapeau \ndu Niger ?": "3",
        "Comment appelle-t-on le thé vert très sucré \nbu toute la journée ?": "Ataya"
    }

    return Questions




