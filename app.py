from customtkinter import CTkLabel

from images import *


ctk.set_default_color_theme("dark-blue")
ctk.set_appearance_mode("dark")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title = "Love app"
        self.geometry("1280x720")


        self.bg = CTkLabel(self, image=bg, text='')
        self.bg.place(relheight=1, relwidth=1)

        self.button = ctk.CTkButton(self,
                                    text="Press me",
                                    command=self.button_callback,
                                    font=('Georgia', 12),
                                    fg_color="#A00000")
        self.button.place(x=100, y=100)


    @staticmethod
    def button_callback():
        print("button clicked")
