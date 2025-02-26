import customtkinter as ctk
from buttons_functions.button_functions import *
from images import sticker_intro


def make_frame_main_frame(master):
    return ctk.CTkFrame(
        master,
        border_width=5,
        border_color="#FF83C6",
        fg_color="#FFC4E4",
        width=200,
        height=200
    )


def make_intro_frame(master):
    return ctk.CTkFrame(
        master,
        width=624,
        height=400,
        border_width=0,
        bg_color="#860C4D",
        fg_color="#860C4D"
    )


def make_about_text(master):
    return ctk.CTkTextbox(
        master.intro_frame,
        width=624,
        height=250,
        border_spacing=5,
        border_color="#FF80C4",
        font=("Arial", 20),
        corner_radius=30,
        bg_color="#860C4D",
        fg_color="#860C4D"
    )


def make_intro_button(master):
    return ctk.CTkButton(
        master.frame,
        text="О приложении",
        command=lambda: toggle_window(master.intro_frame),
        bg_color="#f48d90"
    )


def make_intro_sticker(master):
    return ctk.CTkLabel(
        master.intro_frame,
        text='',
        image=sticker_intro,
        corner_radius=0,
        bg_color="#860C4D",
        fg_color="#860C4D"
    )
