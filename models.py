from images import *
from texts.texts import *
from widgets.widgets import *


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title = "Love app"
        self.geometry("1280x720")

        # Set up a background
        self.bg = ctk.CTkLabel(self, image=bg, text='')
        self.bg.place(relheight=1, relwidth=1)

        self.frame = make_frame_main_frame(self)

        self.intro_button = make_intro_button(self)

        self.intro_frame = make_intro_frame(self)

        self.about_text = make_about_text(self)

        self.intro_sticker = make_intro_sticker(self)

        # Place menu frame
        self.frame.place(x=20, y=20)
        # Pack intro button
        self.intro_button.pack()
        # Pack about text
        self.about_text.pack()
        # Insert text into about text box
        self.about_text.insert(0.0, text=intro_text)
        # Pack intro sticker
        self.intro_sticker.pack(anchor=ctk.SE)
