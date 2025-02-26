import pywinstyles
from texts.texts import *
import customtkinter as ctk
from widgets.widgets import *
import os


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title = "Love app"
        self.geometry("1280x720")
        self.iconbitmap(f"{os.getcwd()}\\images\\app-icon.ico")
        self.maxsize(width=1280, height=720)
        self.minsize(width=1280, height=720)

        # Set up a background
        self.bg = ctk.CTkLabel(self, image=bg, text='')
        self.bg.place(relheight=1, relwidth=1)

        self.frame = make_menu_frame(self)

        self.intro_button = make_intro_button(self)

        self.intro_frame = make_intro_frame(self)

        self.about_text = make_about_text(self)

        self.intro_sticker = make_intro_sticker(self)

        self.compliment_button = make_compliment_button(self)

        self.compliment_window = ToplevelWindow("Комплименты от меня :)")

        # Place menu frame
        self.frame.place(x=20, y=20)
        pywinstyles.set_opacity(self.frame, color="#000001")
        # Pack intro button
        self.intro_button.place(x=53, y=30)
        # Pack about text
        self.about_text.place(x=5, y=15)
        # Insert text into about text box
        self.about_text.insert(0.0, text=intro_text)
        # Pack intro sticker
        self.intro_sticker.place(x=400, y=260)
        # Pack compliment button
        self.compliment_button.place(x=25, y=75)


class ToplevelWindow(ctk.CTkToplevel):
    def __init__(self, title, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x300")
        self.title(title)
