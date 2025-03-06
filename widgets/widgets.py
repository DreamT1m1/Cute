import customtkinter as ctk
from buttons_functions.button_functions import toggle_window, open_toplevel
from images import about_icon, sticker_intro, compliment_icon


def make_menu_frame(master):
    return ctk.CTkFrame(
        master,
        corner_radius=40,
        border_width=3,
        border_color="#fbdbde",
        fg_color="#860C4D",
        bg_color="#000001",
        width=250,
        height=680
    )


def make_intro_frame(master):
    return ctk.CTkFrame(
        master,
        width=630,
        height=400,
        border_width=5,
        border_color="#fbdbde",
        bg_color="#f7b2b5",
        fg_color="#860C4D"
    )


def make_about_text(master):
    return ctk.CTkTextbox(
        master.intro_frame,
        width=620,
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
        fg_color="#b05a5e",
        bg_color="#860C4D",
        border_width=3,
        border_color="#fbdbde",
        image=about_icon
    )


def make_intro_sticker(master):
    return ctk.CTkLabel(
        master.intro_frame,
        text='',
        image=sticker_intro,
        corner_radius=25,
        bg_color="#860C4D",
        fg_color="#860C4D"
    )


def make_compliment_frame(master):
    return ctk.CTkFrame(
        master,
        width=630,
        height=400,
        border_width=5,
        border_color="#fbdbde",
        bg_color="#f7b2b5",
        fg_color="#860C4D"
    )


def make_compliment_button(master):
    return ctk.CTkButton(
        master.frame,
        text="Генератор комплиментов",
        command=lambda: open_toplevel(master, "compliment_window", "Комплименты от меня :)", window_type="compliment"),
        fg_color="#b05a5e",
        bg_color="#860C4D",
        border_width=3,
        border_color="#fbdbde",
        image=compliment_icon
    )


def make_compliment(master, compliment: str):
    return ctk.CTkLabel(
        master,
        text=compliment,
        corner_radius=30,
        fg_color="#e99cae",
        bg_color="#db839b",
        text_color="#000000",
        width=130,
        height=180,
        wraplength=110
    )
