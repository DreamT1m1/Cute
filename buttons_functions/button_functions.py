import os

import widgets.widgets
from images import *
from random import choice
import customtkinter as ctk


def toggle_window(window: ctk.CTkTextbox | ctk.CTkLabel | ctk.CTkFrame):
    if not window.winfo_ismapped():
        window.place(x=300, y=125)
    else:
        window.place_forget()


def open_toplevel(master, top_level_window_name, window_title: str, window_type: str):
    if (
            master.__dict__[top_level_window_name] is None
            or not master.__dict__[top_level_window_name].winfo_exists()
    ):
        master.__dict__[top_level_window_name] = ctk.CTkToplevel(window_title)
        master.__dict__[top_level_window_name].attributes('-topmost', True)
        master.__dict__[top_level_window_name].grab_set()

        if window_type == "compliment":
            master.__dict__[top_level_window_name].bg = ctk.CTkLabel(
                master.__dict__[top_level_window_name],
                image=compliment_window,
                text=''
            )
            master.__dict__[top_level_window_name].bg.place(
                relheight=1,
                relwidth=1
            )
            master.__dict__[top_level_window_name].iconbitmap(f"{os.getcwd()}\\images\\compliment.ico")

            with open("data\\compliments.txt", 'r', encoding='utf-8') as inp:
                data = [line.strip() for line in inp.readlines()]

            compliment = choice(data)

            compliment_text = widgets.widgets.make_compliment(
                master.__dict__[top_level_window_name],
                compliment
            )

            compliment_text.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

    else:
        master.__dict__[top_level_window_name].focus()
