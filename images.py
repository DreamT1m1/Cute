from PIL import Image
from customtkinter import CTkImage

bg = CTkImage(
    light_image=Image.open("images\\bg.jpg"),
    dark_image=Image.open("images\\bg.jpg"),
    size=(1280,720)
)
