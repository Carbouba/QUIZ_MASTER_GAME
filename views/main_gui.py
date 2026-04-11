"""
Module principal de l'interface graphique du Quiz Master Game.

Ce fichier contient toute la logique d'affichage et de navigation de l'UI :
  - main_view()  : point d'entrée, crée la fenêtre et lance le menu principal.
  - main_menu()  : affiche l'écran d'accueil avec le record et les boutons.
  - game_ui()    : affiche l'écran de jeu (questions, score, saisie).

L'interface est construite avec CustomTkinter (ctk).
"""

import os
import sys
import random

from tkinter import END
from PIL import Image
import customtkinter as ctk
import CTkMessagebox as ctkm

# Ajout des répertoires parents au chemin Python pour les imports relatifs
sys.path.append("..")
sys.path.append("../configs")
sys.path.append("../data")
sys.path.append("../images")

# Chemin absolu vers le dossier images, calculé depuis ce fichier
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = os.path.join(BASE_DIR, "..", "images")

from questions import get_question
from db_call import get_record, insert_record, init_db
from style import COLORS, FONTS, DIMENSIONS
from db_connect import con, cur, cur2, con2


# ── Variables globales de session ─────────────────────────────────────────────

user_score = 0                        # Score courant du joueur
good_response = 0                     # Compteur de bonnes réponses
false_response = 0                    # Compteur de mauvaises réponses
dico_question = len(get_question())
remain_questions = dico_question      # Nombre de questions restantes
all_questions = dico_question         # Nombre total de questions (invariant)


# ── Point d'entrée de l'interface ─────────────────────────────────────────────

def main_view():
    """Initialise la fenêtre principale et lance la boucle d'événements Tkinter.

    Cette fonction crée :
      - La fenêtre `app` avec son titre et ses dimensions.
      - Le bandeau titre en haut (titre_frame).
      - Le cadre central `main_frame` qui accueille les écrans successifs.
    Elle appelle ensuite main_menu() pour afficher l'écran d'accueil.
    """
    last_record = get_record()

    # ── Fenêtre principale ─────────────────────────────────────────────────────
    app = ctk.CTk()
    app.title("QUIZ MASTER GAME")
    app.geometry("500x700")
    app.resizable(False, False)
    app.configure(fg_color=COLORS["bg"])

    # ── Bandeau titre ──────────────────────────────────────────────────────────
    title_frame = ctk.CTkFrame(
        app,
        fg_color=COLORS["surface"],
        width=500,
        height=60,
        corner_radius=0,
    )
    title_frame.pack(pady=(0, 5))
    title_frame.pack_propagate(False)

    title_lbl = ctk.CTkLabel(
        title_frame,
        text="🎮 QUIZ MASTER GAME 🎮",
        text_color=COLORS["text"],
        font=FONTS["title"],
    )
    title_lbl.pack(expand=True)

    # ── Cadre central (zone de contenu interchangeable) ───────────────────────
    main_frame = ctk.CTkFrame(
        app,
        fg_color=COLORS["bg"],
        width=500,
        height=700,
        corner_radius=0,
    )
    main_frame.pack()
    main_frame.pack_propagate(False)

    # ── Fonctions internes ─────────────────────────────────────────────────────

    def clear_screen():
        """Détruit tous les widgets du cadre central avant de charger un nouvel écran."""
        for widget in main_frame.winfo_children():
            widget.destroy()

    def main_menu():
        """Affiche l'écran d'accueil avec le record, le bouton de démarrage et les options."""
        clear_screen()

        # ── Panneau supérieur : icône, bienvenue, record ───────────────────────
        top_panel = ctk.CTkFrame(
            main_frame,
            fg_color=COLORS["bg"],
            width=300,
            height=280,
            corner_radius=0,
        )
        top_panel.pack(pady=(10, 5))
        top_panel.pack_propagate(False)

        game_icon = ctk.CTkButton(
            top_panel,
            text="🎮",
            font=FONTS["h1"],
            fg_color=COLORS["primary_dim"],
            border_width=1,
            border_color=COLORS["border"],
            corner_radius=DIMENSIONS["border"],
            hover=False,
            width=70,
            height=70,
        )
        game_icon.pack(pady=(20, 15))

        welcome_lbl = ctk.CTkLabel(
            top_panel,
            text="BIENVENUE",
            text_color=COLORS["text"],
            font=FONTS["h1"],
        )
        welcome_lbl.pack(pady=5)

        subtitle_lbl = ctk.CTkLabel(
            top_panel,
            text="Repondez aux questions et battez le \nrecord",
            text_color=COLORS["text_muted"],
            font=("Roboto", 18),
        )
        subtitle_lbl.pack(pady=(0, 5))

        record_badge = ctk.CTkButton(
            top_panel,
            text=f"🏆 Record à battre : {last_record} pts",
            text_color=COLORS["white"],
            font=("Roboto", 18),
            fg_color=COLORS["surface"],
            border_width=1,
            border_color=COLORS["primary_dim"],
            corner_radius=8,
            hover=False,
            width=100,
            height=50,
        )
        record_badge.pack_propagate(False)
        record_badge.pack(pady=(10, 5), ipadx=10)

        # ── Panneau central : boutons d'action ────────────────────────────────
        center_panel = ctk.CTkFrame(
            main_frame,
            fg_color=COLORS["bg"],
            width=300,
            height=500,
            corner_radius=0,
        )
        center_panel.pack(pady=(10, 5))
        center_panel.pack_propagate(False)

        def refresh_record():
            """Réinitialise le record à 0 et met à jour l'affichage du badge."""
            insert_record(0)
            new_record = get_record()
            record_badge.configure(text=f"🏆 Record à battre : {new_record} pts")

        start_btn = ctk.CTkButton(
            center_panel,
            text=" Commencer",
            text_color=COLORS["white"],
            font=FONTS["title"],
            image=ctk.CTkImage(Image.open(os.path.join(IMG_DIR, "play.png"))),
            compound="left",
            fg_color=COLORS["primary"],
            hover_color=COLORS["primary_hover"],
            width=350,
            height=70,
            corner_radius=DIMENSIONS["border"],
            cursor="hand2",
            command=game_ui,
        )
        start_btn.pack(pady=10)

        reset_record_btn = ctk.CTkButton(
            center_panel,
            text="Reinitialiser le record",
            text_color=COLORS["warning"],
            font=FONTS["title"],
            image=ctk.CTkImage(Image.open(os.path.join(IMG_DIR, "sync.png"))),
            compound="left",
            fg_color=COLORS["surface"],
            hover=False,
            width=350,
            height=70,
            corner_radius=DIMENSIONS["border"],
            border_width=1,
            border_color=COLORS["warning_hover"],
            cursor="hand2",
            command=refresh_record,
        )
        reset_record_btn.pack(pady=10)

        quit_btn = ctk.CTkButton(
            center_panel,
            text="Quitter",
            text_color=COLORS["danger"],
            font=FONTS["title"],
            image=ctk.CTkImage(Image.open(os.path.join(IMG_DIR, "quit.png"))),
            compound="left",
            fg_color=COLORS["surface"],
            hover=False,
            width=350,
            height=70,
            corner_radius=DIMENSIONS["border"],
            border_width=1,
            border_color=COLORS["danger_hover"],
            cursor="hand2",
            command=app.quit,
        )
        quit_btn.pack(pady=10)

    def game_ui():
        """Affiche l'écran de jeu : questions, saisie du joueur et gestion du score."""
        global remain_questions, user_score

        # Réinitialisation de la session à chaque nouvelle partie
        remain_questions = all_questions
        user_score = 0
        good_response = 0
        false_response = 0

        # ── Chargement et mélange des questions ───────────────────────────────
        question_items = get_question()
        question_list = list(question_items.keys())
        random.shuffle(question_list)
        current_question = question_list.pop()

        clear_screen()

        last_record = get_record()

        # ── Dialogue de confirmation avant de quitter le jeu ──────────────────
        def confirm_quit():
            """Affiche une boîte de dialogue si le joueur tente de quitter en cours de partie."""
            if remain_questions > 0:
                response = ctkm.CTkMessagebox(
                    title="",
                    message=(
                        f"Etes vous sur de quitter le jeux ?\n"
                        f"Il vous reste encore {remain_questions} questions"
                    ),
                    icon="question",
                    option_1="Oui",
                    option_2="Non",
                )
                if response.get() == "Oui":
                    main_menu()  # Retour à l'écran d'accueil

        # ── Barre du haut : bouton retour, record, score ───────────────────────
        top_frame = ctk.CTkFrame(
            main_frame,
            fg_color=COLORS["bg"],
            width=400,
            height=100,
            corner_radius=0,
        )
        top_frame.pack(pady=(20, 10))
        top_frame.pack_propagate(False)

        back_btn = ctk.CTkButton(
            top_frame,
            text="Retour",
            image=ctk.CTkImage(
                Image.open(os.path.join(IMG_DIR, "back.png")), size=(6, 7)
            ),
            text_color=COLORS["danger"],
            font=("Roboto", 15),
            fg_color=COLORS["surface"],
            corner_radius=DIMENSIONS["border"],
            border_width=1,
            border_color=COLORS["danger_hover"],
            hover=False,
            cursor="hand2",
            width=90,
            height=30,
            command=confirm_quit,
        )
        back_btn.grid(row=0, column=0, padx=10)

        record_badge = ctk.CTkButton(
            top_frame,
            text=f"Record à battre : {last_record} pts",
            text_color=COLORS["primary_hover"],
            font=("Roboto", 15),
            fg_color=COLORS["surface"],
            corner_radius=DIMENSIONS["border"],
            border_width=1,
            border_color=COLORS["primary_hover"],
            hover=False,
            width=180,
            height=30,
        )
        record_badge.grid_propagate(False)
        record_badge.grid(row=0, column=1, padx=10)

        score_badge = ctk.CTkButton(
            top_frame,
            text=f"Score : {user_score}",
            text_color=COLORS["success_hover"],
            font=("Roboto", 15),
            fg_color=COLORS["surface"],
            corner_radius=DIMENSIONS["border"],
            border_width=1,
            border_color=COLORS["success_hover"],
            hover=False,
            width=100,
            height=30,
        )
        score_badge.grid_propagate(False)
        score_badge.grid(row=0, column=2, padx=10)

        # ── Barre de progression des questions restantes ───────────────────────
        remaining_frame = ctk.CTkFrame(
            main_frame,
            fg_color=COLORS["surface"],
            width=400,
            height=70,
            corner_radius=DIMENSIONS["border"],
            border_width=1,
            border_color=COLORS["border"],
        )
        remaining_frame.pack(pady=(10, 5))
        remaining_frame.pack_propagate(False)
        
        remaining_label = ctk.CTkLabel(
            remaining_frame,
            text="Questions \nrestantes",
            text_color=COLORS["text_muted"],
            font=FONTS["question"],
            justify="left",
        )
        remaining_label.grid(column=0, row=0, pady=(10, 5), padx=20, ipadx=20)

        progress_bar = ctk.CTkProgressBar(
            master=remaining_frame,
            width=100,
            height=10,
            corner_radius=10,
            border_width=1,
            border_color=COLORS["border"],
            progress_color=COLORS["primary"],
            orientation="horizontal",
        )
        progress_bar.set(remain_questions / all_questions)
        progress_bar.grid(column=1, row=0, pady=(10, 5), padx=20, ipadx=20, sticky="ew")

        # ── Carte de la question ───────────────────────────────────────────────
        question_frame = ctk.CTkFrame(
            main_frame,
            fg_color=COLORS["surface3"],
            width=400,
            height=150,
            corner_radius=DIMENSIONS["border"],
            border_width=1,
            border_color=COLORS["border"],
        )
        question_frame.pack(pady=(10, 5))
        question_frame.pack_propagate(False)

        questions_count_badge = ctk.CTkButton(
            question_frame,
            text=f"Questions restantes : {remain_questions}/{all_questions}",
            text_color=COLORS["white"],
            font=FONTS["badge"],
            fg_color=COLORS["primary_dim"],
            corner_radius=6,
            hover=False,
            width=50,
            height=22,
        )
        questions_count_badge.pack_propagate(False)
        questions_count_badge.pack(pady=(10, 5), anchor="center", ipadx=2)

        question_lbl = ctk.CTkLabel(
            question_frame,
            text=current_question,
            text_color=COLORS["text"],
            font=FONTS["question"],
        )
        question_lbl.pack(pady=10, anchor="center")

        # ── Zone de saisie et bouton de validation ─────────────────────────────
        bottom_frame = ctk.CTkFrame(
            main_frame,
            fg_color=COLORS["surface"],
            width=400,
            height=300,
            corner_radius=DIMENSIONS["border"],
            border_width=1,
            border_color=COLORS["border"],
        )
        bottom_frame.pack(pady=(10, 5))
        bottom_frame.pack_propagate(False)

        response_lbl = ctk.CTkLabel(
            bottom_frame,
            text="Ta réponse :",
            text_color=COLORS["text_muted"],
            font=FONTS["placeholder"],
        )
        response_lbl.pack(pady=(5, 0), anchor="w")

        user_input = ctk.CTkEntry(
            bottom_frame,
            fg_color=COLORS["surface3"],
            text_color=COLORS["text"],
            border_width=1,
            border_color=COLORS["border"],
            width=400,
            height=40,
            corner_radius=8,
        )
        user_input.pack(pady=5)

        # ── Logique de validation d'une réponse ───────────────────────────────
        def on_submit(player_answer):
            """Évalue la réponse du joueur, met à jour le score et passe à la question suivante.

            Args:
                player_answer (str): La réponse saisie par le joueur.
            """
            nonlocal current_question, question_list
            global remain_questions, user_score

            all_q = get_question()
            expected_answer = all_q[current_question]

            if player_answer.strip().lower() != expected_answer.lower():
                # ── Mauvaise réponse ───────────────────────────────────────────
                user_score -= 1
                feedback = ctk.CTkLabel(
                    bottom_frame,
                    text="❌ Aïe... Raté !",
                    font=FONTS["button"],
                    fg_color=COLORS["danger_light"],
                    width=100,
                    height=20,
                )
                feedback.pack(pady=20)
                feedback.after(2000, feedback.destroy)

            else:
                # ── Bonne réponse ──────────────────────────────────────────────
                user_score += 1
                feedback = ctk.CTkLabel(
                    bottom_frame,
                    text="✅ Bravo ! Bonne réponse ! Tu gagnes 1 point.",
                    font=FONTS["button"],
                    fg_color=COLORS["success_hover"],
                    width=100,
                    height=20,
                )
                feedback.pack(pady=20)
                feedback.after(5000, feedback.destroy)

            # ── Mise à jour de l'interface après chaque réponse ───────────────
            remain_questions -= 1
            progress_bar.set(remain_questions / all_questions)  # ← recalcul à chaque réponse
            user_input.delete(0, END)

            if remain_questions > 0 and question_list:
                # Passage à la question suivante
                current_question = question_list.pop()
                question_lbl.configure(text=current_question)

                # Mise à jour du badge de score
                displayed_score = user_score if user_score > 0 else 0
                score_badge.configure(
                    text=f"Score : {displayed_score}"
                )

                # Alerte visuelle quand il reste peu de questions
                if remain_questions <= 3:
                    questions_count_badge.configure(
                        fg_color=COLORS["danger_light"]
                    )
                questions_count_badge.configure(
                    text=f"Question(s) restante(s) : {remain_questions}/{all_questions}"
                )
            else:
                # ── Fin du quiz : enregistrement du record si battu ────────────
                if user_score > last_record:
                    insert_record(user_score)
                record_badge.configure(text=f"🏆 Record à battre : {last_record} pts")
                # Retour au menu principal après un court délai
                app.after(1500, main_menu)

        submit_btn = ctk.CTkButton(
            bottom_frame,
            text="Envoyer",
            text_color=COLORS["white"],
            font=FONTS["subtitle"],
            fg_color=COLORS["primary"],
            hover_color=COLORS["primary_hover"],
            width=60,
            height=30,
            corner_radius=DIMENSIONS["border"],
            command=lambda: on_submit(user_input.get()),
        )
        submit_btn.pack(anchor="w")

    # ── Lancement de l'application ─────────────────────────────────────────────
    main_menu()
    game_ui()
    app.mainloop()


# ── Point d'entrée du script ───────────────────────────────────────────────────
main_view()
