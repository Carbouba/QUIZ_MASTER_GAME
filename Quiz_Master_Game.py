"""
Quiz Master Game — Version texte (console).

Ce fichier est la version originale du jeu en mode console (terminal).
Il pose les questions du dictionnaire une par une, évalue les réponses
du joueur et gère le score ainsi que le record via un fichier texte.

Note : Ce fichier est distinct de l'interface graphique (views/main_gui.py).
"""


# ── Fonctions utilitaires ──────────────────────────────────────────────────────

def save_record(score):
    """Enregistre un nouveau record dans le fichier 'record.txt'.

    Args:
        score (int): Le score à enregistrer.
    """
    # Ouverture en mode écriture ("w" crée le fichier s'il n'existe pas)
    with open("record.txt", "w") as f:
        f.write(str(score))


def get_record():
    """Charge et retourne le record depuis le fichier 'record.txt'.

    Returns:
        int: Le record lu dans le fichier, ou 0 si le fichier est
             introuvable ou corrompu.
    """
    try:
        # Ouverture en mode lecture
        with open("record.txt", "r") as f:
            record = f.read()
            return int(record)
    except FileNotFoundError:
        # Le fichier n'existe pas encore : le record démarre à 0
        return 0
    except ValueError:
        # Le fichier est vide ou contient une valeur non numérique
        return 0


# ── Données du jeu ─────────────────────────────────────────────────────────────

# Dictionnaire des questions : chaque clé est une question,
# chaque valeur est la réponse attendue.
questions = {
    "Quelle est la capitale du Niger ?": "Niamey",
    "En quelle année le Niger a-t-il obtenu son indépendance ?": "1960",
    "Comment s'appelle la célèbre viande séchée et épicée du Niger ?": "Kilishi",
    "Quel grand fleuve traverse le sud-ouest du pays ?": "Niger",
    "Quelle ville est célèbre pour sa grande mosquée en terre et son désert ?": "Agadez",
    "Quel est le surnom de l'équipe nationale de football du Niger ?": "Mena",
    "Quelle est la monnaie utilisée au Niger ?": "CFA",
    "Quel animal est le symbole national du Niger ?": "Gazelle",
    "Combien de couleurs y a-t-il sur le drapeau du Niger ?": "3",
    "Comment appelle-t-on le thé vert très sucré bu toute la journée ?": "Ataya",
}


# ── Point d'entrée principal ───────────────────────────────────────────────────

if __name__ == "__main__":

    score = 0               # Score courant du joueur
    reponses_correctes = 0  # Compteur de bonnes réponses
    reponses_incorrectes = 0  # Compteur de mauvaises réponses
    questions_restantes = len(questions)  # Nombre de questions restantes
    total_questions = len(questions)      # Nombre total de questions

    ancien_record = get_record()

    print(f"\n📜 Record actuel à battre : {ancien_record} points\n")
    print("\n===== 🎮 QUIZ MASTER GAME 🎮 =====")

    for question in questions:
        print(f"Question(s) restante(s) : {questions_restantes}")
        print("-------------------------")
        print(f"❓ Question : {question}")
        print("-------------------------")

        # Récupération de la saisie et normalisation (sans espaces, en minuscules)
        reponse_joueur = input("👉 Ta reponse : ").strip().lower()
        bonne_reponse = questions[question]

        if reponse_joueur == bonne_reponse.lower():
            print("\n=========================")
            print("✅ Bravo ! Bonne réponse ! Tu gagnes 1 point.")
            score += 1
            print(f"👉 Ton score actuel est : {score}")
            print("=========================\n")
            reponses_correctes += 1
        else:
            print("\n=========================")
            print(
                f"❌ Aïe... Raté ! La bonne réponse était : '{bonne_reponse}'."
            )
            print("Tu as perdu 1 point !")
            score -= 1
            reponses_incorrectes += 1
            # On affiche 0 plutôt qu'un score négatif
            score_affiche = score if score > 0 else 0
            print(f"Ton score actuel est : {score_affiche}")
            print("=========================\n")

        questions_restantes -= 1

        if questions_restantes == 0:
            print("🎉 ===== FIN DU QUIZ ===== 🎉")
            print(f"✅ Réponses correctes   : {reponses_correctes}")
            print(f"❌ Réponses incorrectes : {reponses_incorrectes}")
            score_final = score if score > 0 else 0
            print(f"🏆 Score final : {score_final}/{total_questions}")
            print("=========================\n")

            if score > ancien_record:
                print(
                    f"🚀 INCROYABLE ! NOUVEAU RECORD ! "
                    f"(Ancien : {ancien_record})"
                )
                save_record(score)
            else:
                print(
                    f"😐 Tu n'as pas battu le record de {ancien_record}. "
                    f"Essaie encore !"
                )