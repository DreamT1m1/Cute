import pywinstyles
from texts.texts import *
from widgets.widgets import *
from images import bg
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

        # Menu frame
        self.frame = make_menu_frame(self)
        # App info button
        self.intro_button = make_intro_button(self)
        # Intro frame
        self.intro_frame = make_intro_frame(self)
        # Text inside intro frame
        self.about_text = make_about_text(self)
        # Sticker inside intro frame
        self.intro_sticker = make_intro_sticker(self)
        # Compliment button
        self.compliment_button = make_compliment_button(self)
        # Compliment TopLevel window
        self.compliment_window = None

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
