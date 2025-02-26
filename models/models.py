import customtkinter as ctk
from images import *
from button_functions import *


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title = "Love app"
        self.geometry("1280x720")


        self.bg = ctk.CTkLabel(self, image=bg, text='')
        self.bg.place(relheight=1, relwidth=1)

        self.frame = ctk.CTkFrame(
            self,
            border_width=1,
            border_color="#FF83C6",
            fg_color="#FFC4E4"
        )

        self.intro_button = ctk.CTkButton(
            self.frame,
            text="О приложении",
            command=about_button
        )

        self.intro_button.pack(anchor=ctk.NW)
        self.frame.pack(anchor=ctk.NW, fill=ctk.Y, padx=5, pady=5)

    @staticmethod
    def button_callback():
        print("button clicked")
