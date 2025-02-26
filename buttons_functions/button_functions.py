import customtkinter as ctk


def toggle_window(window: ctk.CTkTextbox | ctk.CTkLabel | ctk.CTkFrame):
    if not window.winfo_ismapped():
        window.place(x=300, y=125)
    else:
        window.place_forget()

