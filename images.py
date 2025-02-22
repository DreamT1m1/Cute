from PIL import Image
import customtkinter as ctk

bg = ctk.CTkImage(
    light_image=Image.open("images\\bg.jpg"),
    dark_image=Image.open("images\\bg.jpg"),
    size=(1280,720)
)
