import customtkinter as ctk
import os
from images import *


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
    else:
        master.__dict__[top_level_window_name].focus()
