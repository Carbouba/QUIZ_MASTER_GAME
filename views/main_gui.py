import glob
import os
import sys
import random

from tkinter import END
from turtle import delay
from PIL import Image
import customtkinter as ctk
import CTkMessagebox as ctkm

sys.path.append("..")
sys.path.append("../configs")
sys.path.append("../data")
sys.path.append("../images")

BASE_DIRE = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = os.path.join(BASE_DIRE, "..", "images")

from questions import get_question
from db_call import get_record, insert_record, init_db
from style import COLORS, FONTS, DIMENSIONS
from db_connect import con, cur, cur2, con2


USER_SCORE = 0 # Le score dans le jeu
good_response = 0 # Ajoute des points losque la reponse correcte
false_response = 0 # enléve des points losque la reponse incorrecte
dico_question = len(get_question())
remain_questions = dico_question # Utilisé pour controler le nombre de questions restantes
all_questions = dico_question # utilisé pour stocker la quantité total des question

def main_view():


    #insert_record(0)
    last_record = get_record()

    app = ctk.CTk()
    app.title("QUIZ MASTER GAME")
    app.geometry("500x700")
    app.resizable(False, False)
    app.configure(fg_color=COLORS["bg"])

    # ── Main Title frame ───────────────────────────────────────────────title
    title_fram = ctk.CTkFrame(app, fg_color=COLORS["surface"],
                          width=500, height=60, corner_radius=0)
    title_fram.pack(pady=(0, 5))
    title_fram.pack_propagate(False)
    title_lbl = ctk.CTkLabel(title_fram,
                         text="🎮 QUIZ MASTER GAME 🎮",
                         text_color=COLORS["text"],
                         font=FONTS["title"])
    title_lbl.pack(expand=True)
    
    main_fram = ctk.CTkFrame(app, fg_color=COLORS["bg"],
                         width=500, height=700, corner_radius=0)
    main_fram.pack()
    main_fram.pack_propagate(False)

        # Nettoyage d'écran
    def nettoyage():


        # Efface les widgets affichés dans la zone centrale avant de charger un nouvel écran.
        for widgets in main_fram.winfo_children():
            widgets.destroy()

    def main_menu():


        # Efface les widgets affichés dans la zone centrale avant de charger un nouvel écran.
        nettoyage()

        # ── SubTitle frame ───────────────────────────────────────────────
        second_frame = ctk.CTkFrame(main_fram, fg_color=COLORS["bg"],
                             width=300, height=280, corner_radius=0)
        second_frame.pack(pady=(10, 5))
        second_frame.pack_propagate(False)

        game_icon = ctk.CTkButton(second_frame,
                           text=f"🎮",
                           #text_color=COLORS["white"],
                           font=FONTS["h1"],
                           fg_color=COLORS["primary_dim"],
                           border_width=1,
                           border_color=COLORS["border"],
                           corner_radius=DIMENSIONS["border"], hover=False,
                           width=70, height=70)
        game_icon.pack(pady=(20,15))

        wel_lbl = ctk.CTkLabel(second_frame,
                        text="BIENVENUE",
                        text_color=COLORS["text"], font=FONTS["h1"])
        wel_lbl.pack(pady=5) 

        sub_lbl = ctk.CTkLabel(second_frame,
                        text="Repondez aux questions et battez le \nrecord",
                        text_color=COLORS["text_muted"], font=("Roboto", 18))
        sub_lbl.pack(pady=(0,5))   

        rec_badge = ctk.CTkButton(second_frame,
                           text=f"🏆 Record à battre : {last_record} pts",
                           text_color=COLORS["white"],
                           font=("Roboto", 18),
                           fg_color=COLORS["surface"],
                           border_width=1,
                           border_color=COLORS["primary_dim"],
                           corner_radius=8, hover=False,
                           width=100, height=50)
        rec_badge.pack_propagate(False)
        rec_badge.pack(pady=(10,5), ipadx=10) 

        # ── Center frame ───────────────────────────────────────────────
        center_frame = ctk.CTkFrame(main_fram, fg_color=COLORS["bg"],
                             width=300, height=500, corner_radius=0)
        center_frame.pack(pady=(10, 5))
        center_frame.pack_propagate(False)

        start_btn = ctk.CTkButton(center_frame, text=" Commencer", text_color=COLORS["white"],
                                    font=FONTS["title"], 
                                    image=ctk.CTkImage(Image.open(os.path.join(IMG_DIR, "play.png"))),
                                    compound="left",
                                    fg_color=COLORS["primary"], hover_color=COLORS["primary_hover"],
                                    width=350, height=70,
                                    corner_radius=DIMENSIONS["border"],
                                    cursor="hand2",
                                    command=game_ui
                                    )
        start_btn.pack(pady=10)

        def refresh_record():
            insert_record(0)
            last_record = get_record()
            rec_badge.configure(text=f"🏆 Record à battre : {last_record} pts")

        reco_init_btn = ctk.CTkButton(center_frame, text="Reinitialiser le record", text_color=COLORS["warning"],
                                        font=FONTS["title"],
                                        image=ctk.CTkImage(Image.open(os.path.join(IMG_DIR, "sync.png"))),
                                        compound="left",
                                        fg_color=COLORS["surface"], hover=False,
                                        width=350, height=70,
                                        corner_radius=DIMENSIONS["border"],
                                        border_width=1,
                                        border_color=COLORS["warning_hover"],
                                        cursor="hand2",
                                        command=refresh_record
                                        )
        reco_init_btn.pack(pady=10)

        quit_init_btn = ctk.CTkButton(center_frame, text="Quitter", text_color=COLORS["danger"],
                                    font=FONTS["title"],
                                    image=ctk.CTkImage(Image.open(os.path.join(IMG_DIR, "quit.png"))),
                                    compound="left",
                                    fg_color=COLORS["surface"], hover=False,
                                    width=350, height=70,
                                    corner_radius=DIMENSIONS["border"],
                                    border_width=1,
                                    border_color=COLORS["danger_hover"],
                                    cursor="hand2",
                                    command=app.quit    
                                    )
        quit_init_btn.pack(pady=10)
        

    def game_ui():

        # ── Recuperation des questions ────────────────────────────────────────────
        ques_items = get_question() 
        list_questions = list(ques_items.keys())

        random.shuffle(list_questions)

        current_question = list_questions.pop()

        #print(current_question)
        
        # ── Nettoyage d'écran ────────────────────────────────────────────
        nettoyage()

        # ── Recuperation du record ────────────────────────────────────────────
        last_record = get_record()

        # ── Quitter le jeu ────────────────────────────────────────────
        def confirm_quit():
            if remain_questions > 0:
                response = ctkm.CTkMessagebox(
                    title=f"",
                    message=f"Etes vous sur de quitter le jeux ?\nIl vous reste encore {remain_questions} questions",
                    icon="question",
                    option_1="Oui",
                    option_2="Non"
                )
                if response.get() == "Oui":
                    main_menu() # Retour à l'écran de d'acceuil

        # ── Top frame ───────────────────────────────────────────────
        top_frame = ctk.CTkFrame(main_fram, fg_color=COLORS["bg"],
                          width=400, height=100, corner_radius=0)
        top_frame.pack(pady=(20, 10))
        top_frame.pack_propagate(False)

        back_menu_btn = ctk.CTkButton(top_frame, text="Retour",
                                    image=ctk.CTkImage(Image.open(os.path.join(IMG_DIR, "back.png")), size=(6,7)),
                                    text_color=COLORS["danger"],
                                font=("Roboto", 15),
                                fg_color=COLORS["surface"],
                                corner_radius=DIMENSIONS["border"],
                                border_width=1,
                                border_color=COLORS["danger_hover"],
                                hover=False,
                                cursor="hand2",
                                width=90, height=30,
                                command=confirm_quit
                                    )
        back_menu_btn.grid(row=0, column=0, padx=10)

        rec_badge = ctk.CTkButton(top_frame,
                           text=f"Record à battre : {last_record} pt",
                           text_color=COLORS["primary_hover"],
                                font=("Roboto", 15),
                                fg_color=COLORS["surface"],
                                corner_radius=DIMENSIONS["border"],
                                border_width=1,
                                border_color=COLORS["primary_hover"],
                                hover=False,
                           width=180, height=30)
        rec_badge.grid_propagate(False)
        rec_badge.grid(row=0, column=1, padx=10)

        cur_rec_badge = ctk.CTkButton(top_frame,
                                text=f"Score : {USER_SCORE}",
                                text_color=COLORS["success_hover"],
                                font=("Roboto", 15),
                                fg_color=COLORS["surface"],
                                corner_radius=DIMENSIONS["border"],
                                border_width=1,
                                border_color=COLORS["success_hover"],
                                hover=False,
                                width=95, height=30)
        cur_rec_badge.grid_propagate(False)
        cur_rec_badge.grid(row=0, column=2, padx=10)

        # ── remaing questions frame ───────────────────────────────────────────────
        remai_frame = ctk.CTkFrame(main_fram, fg_color=COLORS["surface"],
                             width=400, height=70,
                             corner_radius=DIMENSIONS["border"],
                             border_width=1,
                             border_color=COLORS["border"])
        remai_frame.pack(pady=(10, 5))
        remai_frame.pack_propagate(False)
        

        remaiinig_badge = ctk.CTkLabel(remai_frame,
                                text=f"Questions \nrestantes",
                                text_color=COLORS["text_muted"],
                                font=FONTS["question"],
                                justify="left")
        remaiinig_badge.grid(column=0, row=0, pady=(10,5), ipadx=2)

        progressbar = ctk.CTkProgressBar(master=remai_frame,
                                        width=200,
                                        height=10,
                                        corner_radius=10,
                                        border_width=1,
                                        border_color=COLORS["border"],
                                        progress_color=COLORS["primary"],
                                        orientation="horizontal",
                                        )
        progressbar.set(remain_questions/all_questions)
        progressbar.grid(column=1, row=0, pady=(10,5), ipadx=2)
        

        # ── Center frame ───────────────────────────────────────────────
        center_frame = ctk.CTkFrame(main_fram, fg_color=COLORS["surface3"],
                             width=400, height=150,
                             corner_radius=DIMENSIONS["border"],
                             border_width=1,
                             border_color=COLORS["border"])
        center_frame.pack(pady=(10, 5))
        center_frame.pack_propagate(False)

        remaiinig_badge = ctk.CTkButton(center_frame,
                                 text=f"Questions restantes : {remain_questions}/{all_questions}",
                                 text_color=COLORS["white"],
                                 font=FONTS["badge"],
                                 fg_color=COLORS["primary_dim"],
                                 corner_radius=6, hover=False,
                                 width=50, height=22)
        remaiinig_badge.pack_propagate(False)
        remaiinig_badge.pack(pady=(10,5), anchor="center", ipadx=2)

        question_lbl = ctk.CTkLabel(center_frame, text=current_question,
                             text_color=COLORS["text"],
                             font=FONTS["question"])
        question_lbl.pack(pady=10, anchor="center")

        # ── Buttom frame ───────────────────────────────────────────────
        bottom_frame = ctk.CTkFrame(main_fram, fg_color=COLORS["surface"],
                             width=400, height=300,
                             corner_radius=DIMENSIONS["border"],
                             border_width=1,
                             border_color=COLORS["border"])
        bottom_frame.pack(pady=(10, 5))
        bottom_frame.pack_propagate(False)

        response_lbl = ctk.CTkLabel(bottom_frame, text="Ta réponse :",
                             text_color=COLORS["text_muted"],
                             font=FONTS["placeholder"])
        response_lbl.pack(pady=(5, 0), anchor="w")

        user_in = ctk.CTkEntry(bottom_frame,
                        fg_color=COLORS["surface3"],
                        text_color=COLORS["text"],
                        border_width=1,
                        border_color=COLORS["border"],
                        width=400, height=40,
                        corner_radius=8)
        user_in.pack(pady=5)

        # ── On submit fonction ───────────────────────────────────────────────
        def on_submit(usr_in):
            nonlocal current_question, list_questions
            global remain_questions
            global USER_SCORE 
            
            reponse_attendue = get_question()
            bonne_reponse_attendue = reponse_attendue[current_question]

            if usr_in.strip().lower() != bonne_reponse_attendue.lower():
                print("Echec")
                USER_SCORE -= 1
                msg = ctk.CTkLabel(bottom_frame, text="❌ Aïe... Raté !",
                                    font=FONTS["button"], fg_color=COLORS["danger_light"],
                                    width=100, height=20)
                msg.pack(pady=20)
                msg.after(2000, msg.destroy)

            else:
                print("win")
                print(usr_in)
                USER_SCORE += 1
                msg = ctk.CTkLabel(bottom_frame, text="✅ Bravo ! Bonne réponse ! Tu gagnes 1 point.",
                                    font=FONTS["button"], fg_color=COLORS["success_hover"],
                                    width=100, height=20
                                    )
                msg.pack(pady=20)
                msg.after(5000, msg.destroy)
                
            remain_questions -= 1
            progressbar.step()
            user_in.delete(0, END)
            if remain_questions > 0:
                current_question = list_questions.pop()
                question_lbl.configure(text=current_question)
                if USER_SCORE > 0:
                    cur_rec_badge.configure(text=f"Ton score actuel est : {USER_SCORE}")
                else:
                    cur_rec_badge.configure(text=f"Ton score actuel est : 0")
                
                if remain_questions <= 3:
                    remaiinig_badge.configure(fg_color=COLORS["danger_light"])
                remaiinig_badge.configure(text=f"Question(s) restante(s) : {remain_questions}/{all_questions}")
            else:
                if USER_SCORE > last_record:
                    insert_record(USER_SCORE)
                #cur_rec_badge.configure(text=f"Ton score actuel est : {USER_SCORE}")
                app.after(1500, main_menu)

        submit_res = ctk.CTkButton(bottom_frame, text="Envoyer", text_color=COLORS["white"],
                                    font=FONTS["subtitle"],
                                    fg_color=COLORS["primary"], hover_color=COLORS["primary_hover"],
                                    width=60, height=30,
                                    corner_radius=DIMENSIONS["border"],
                                    command=lambda:on_submit(user_in.get())
                                    )
        submit_res.pack(anchor="w")
        
    main_menu()
    game_ui()
    app.mainloop()


main_view()
