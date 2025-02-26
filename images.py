from PIL import Image
from customtkinter import CTkImage

bg = CTkImage(
    light_image=Image.open("images\\bg.jpg"),
    dark_image=Image.open("images\\bg.jpg"),
    size=(1280,720)
)

sticker_intro = CTkImage(
    light_image=Image.open("images\\sticker_intro.jpg"),
    dark_image=Image.open("images\\sticker_intro.jpg"),
    size=(100, 100)
)

about_icon = CTkImage(
    light_image=Image.open("images\\about icon.png"),
    dark_image=Image.open("images\\about icon.png"),
    size=(20, 20)
)

compliment_icon = CTkImage(
    light_image=Image.open("images\\compliment.png"),
    dark_image=Image.open("images\\compliment.png"),
    size=(20, 20)
)
