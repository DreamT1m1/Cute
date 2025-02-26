import customtkinter as ctk
from customtkinter import CTkLabel, CTkCanvas
from images import *
from buttons_functions.button_functions import *
from texts.texts import *


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title = "Love app"
        self.geometry("1280x720")


        self.bg = ctk.CTkLabel(self, image=bg, text='')
        self.bg.place(relheight=1, relwidth=1)

        self.frame = ctk.CTkFrame(
            self,
            border_width=5,
            border_color="#FF83C6",
            fg_color="#FFC4E4",
            width=200,
            height=200
        )

        self.intro_frame = ctk.CTkFrame(
            self,
            width=624,
            height=400,
            border_width=5,
            border_color="#FF83C6",
            bg_color="#f7b7bb",
            fg_color="#860C4D"
        )

        self.about_text = ctk.CTkTextbox(
            self.intro_frame,
            width=624,
            height=200,
            border_width=1,
            border_spacing=5,
            border_color="#FF80C4",
            font=("Arial", 20),
            corner_radius=30,
            bg_color="#f7b7bb",
            fg_color="#B0457E"
        )

        self.intro_button = ctk.CTkButton(
            self.frame,
            text="О приложении",
            command=lambda: toggle_window(self.intro_frame)
        )

        self.frame.place(x=20, y=20)
        self.intro_button.pack()
        self.about_text.pack()
        self.about_text.insert(0.0, text=intro_text)

    @staticmethod
    def button_callback():
        print("button clicked")
