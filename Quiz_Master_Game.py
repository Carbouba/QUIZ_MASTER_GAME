# Fonction pour enregistré le nouveau score
def new_score(score):
    with open("record.txt", "w") as f: # Ouverture du fichier en mode ecriture ("w" créer un s'il n'xiste pas)   
        f.write(str(f"{score}")) # Ecrire le score en tant que nombre entier

# Fonction pour chargé l'iancien score
def get_record():
    try: # Essaie d'ouvrir le fichier (previent les craches)
        with open(f"record.txt", "r") as f: # Ouvre le fichier en mode lecture
            record = f.read()
            return int(record)
            """ for record in f: # Parcour le fichier ligne par ligne (chaque ligne correspond a 'record')
                print(f"\n📜 Record actuel à battre : {record} points\n") # Affiche un message avec le contenu de la variable 'record' """
    except FileNotFoundError: # Si le fichier n'existe pas renvoie un message
        return 0 # Si pas de fichier, le record est 0
    except ValueError:
        return 0 # Si le fichier est vide ou corrompu
        #print("") # Message vide pour une meilleur experience utilisateur

# Dictionnaire contenant les questions et leurs reponses
# Ici chaque question est une 'clé' et la reponse est la 'valeur' les deux sont liées
Questions = {
    "Quelle est la capitale du Niger ?": "Niamey",
    "En quelle année le Niger a-t-il obtenu son indépendance ?": "1960",
    "Comment s'appelle la célèbre viande séchée et épicée du Niger ?": "Kilishi",
    "Quel grand fleuve traverse le sud-ouest du pays ?": "Niger",
    "Quelle ville est célèbre pour sa grande mosquée en terre et son désert ?": "Agadez",
    "Quel est le surnom de l'équipe nationale de football du Niger ?": "Mena",
    "Quelle est la monnaie utilisée au Niger ?": "CFA",
    "Quel animal est le symbole national du Niger ?": "Gazelle",
    "Combien de couleurs y a-t-il sur le drapeau du Niger ?": "3",
    "Comment appelle-t-on le thé vert très sucré bu toute la journée ?": "Ataya"
}

Score = 0 # Le score dans le jeu
reponse_correcte = 0 # Ajoute des points losque la reponse correcte
reponse_incorrecte = 0 # enléve des points losque la reponse incorrecte
questions_restante = len(Questions) # Utilisé pour controler le nombre de questions restantes
total_questions = len(Questions) # utilisé pour stocker la quantité total des question

# Appele de la fonction pour charger l'ancien score 
ancien_record = get_record()

# while True: # Boucle infinie jusqu'a la fin des questions

print(f"\n📜 Record actuel à battre : {ancien_record} points\n") # Affiche un message avec le contenu de la variable 'record'
print("\n===== 🎮 QUIZ MASTER GAME 🎮 =====")
for question in Questions: # Boucle : parcour le dictionnair pour poser les questions
        print(f"Question(s) restante(s) : {questions_restante}")
        print("-------------------------")
        print(f"❓ Questions : {question}")
        print("-------------------------")

        reponse_joueur = input("👉 Ta reponse : ").strip().lower() # Récupére la saisie externe avec (strip : pour suprimer les espaces) et (lower : pour mettre tout le contenu en miniscule)
        bonne_reponse = Questions[question] # Variable pour stocker la vrais reponse
        if reponse_joueur == bonne_reponse.lower(): # Compare si la saisie et la vrais reponse correspondent (lower : tout en miniscule)
            print("\n=========================")
            print(f"✅ Bravo ! Bonne réponse ! Tu gagnes 1 point.") # Si vrais affiche ce message
            Score += 1 # Ajoute 1 au score
            print(f"👉 Ton score actuel est : {Score}")
            print("=========================\n")
            reponse_correcte += 1 # Ajoute 1 a la variable reponse_correcte
            questions_restante -= 1 # Enléve 1 dans la variable questions_restante
        else: # Sinon la saisie et la vrais reponse ne correspondent
            print("\n=========================")
            print(f"❌ Aïe... Raté ! La bonne réponse était : '{bonne_reponse}'.") # Si faux affiche ce message
            print("Tu a perdu 1 point !")
            Score -= 1 # Enléve 1 point dans le score
            reponse_incorrecte += 1 # Ajoute 1 a la variable reponse_correcte
            if Score > 0: # Condition permettant d'afficher le score s'il n'est pas inferieure 0
                print(f"Ton score actuel est : {Score}")
            else: # Si le score est inferieure à 0, alors affiche '0', au lieu d'un nombre negatif
                print("Ton score actuel est de 0.")
            print("=========================\n")
            questions_restante -= 1 # Enléve 1 dans la variable questions_restante
        if questions_restante == 0: # Si le nombre de question epuisé
            print("🎉 ===== FIN DU QUIZ ===== 🎉") # Fin du quize
            print(f"✅ Réponses correctes : {reponse_correcte}") # Simple message
            print(f"❌ Réponses incorrectes : {reponse_incorrecte}") # Simple message
            if Score > 0: # Si le score est superieure à 0, alors affiche le resultat final
                print(f"🏆 Score final : {Score}/{total_questions}")
            else:
                 print(f"🏆 Score final : 0")
            print("=========================\n")
            if Score < ancien_record:
                print(f"🚀 INCROYABLE ! NOUVEAU RECORD ! (Ancien : {ancien_record})")
                new_score(Score)
            else:
                print(f"😐 Tu n'as pas battu le record de {ancien_record}. Essaie encore !")
                
    

        