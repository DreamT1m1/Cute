from gpt_model import *
from models.models import *


def main():
    ctk.set_default_color_theme("dark-blue")
    ctk.set_appearance_mode("dark")

    app = App()
    bot = AIChat()

    app.mainloop()

if __name__ == "__main__":
    main()