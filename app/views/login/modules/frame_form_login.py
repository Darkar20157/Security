import tkinter as tk
from tkinter import messagebox
from customtkinter import *
from PIL import Image
import app.services.login_services as ls
from app.views.form_master import MasterPanel


def construct_frame_form(window):
    #Frame derecho para representar el formulario
    widget_form = tk.Frame(window, relief=tk.SOLID, bg='#fcfcfc')
    widget_form.pack(side='right', expand=tk.YES, fill=tk.BOTH, padx=20)
    
    #Texto titulo
    title_form = CTkLabel(master=widget_form, text="Bienvenido", font=("Arial", 25, "bold"))
    title_form.pack(pady=(30, 0), padx=30, anchor='w')
    
    subtittle_form = CTkLabel(master=widget_form, text="Este un sistema de faceID", font=("Arial", 13, 'bold'), text_color='gray')
    subtittle_form.pack(pady=5, padx=30, anchor='w')
    
    #Campos input
    #User
    #LABEL
    icon_user = CTkImage(light_image=Image.open('./app/resources/icons/user.png'), dark_image=Image.open('./app/resources/icons/user.png'), size=(25, 25))
    title_user = CTkLabel(master=widget_form, image=icon_user, compound='left', text="Usuarios", font=("Arial", 15, "bold"))
    title_user.pack(pady=(20, 0), padx=30, anchor='w')
    
    #ENTRY
    #Creo un input para la entrada de texto
    input_user = CTkEntry(master=widget_form, width=300, placeholder_text='Usuario', height=35)
    input_user.pack(pady=(2, 20), padx=30, anchor='w')
    
    #Password
    #LABEL
    icon_password = CTkImage(light_image=Image.open('./app/resources/icons/password.png'), dark_image=Image.open('./app/resources/icons/password.png'), size=(25, 25))
    title_pass = CTkLabel(master=widget_form, image=icon_password, compound='left', text="Contraseña", font=("Arial", 15, "bold"))
    title_pass.pack(pady=(20, 0), padx=30, anchor='w')
    
    #ENTRY
    input_pass = CTkEntry(master=widget_form, width=300, placeholder_text='Contraseña', height=35)
    input_pass.configure(show='*')
    input_pass.pack(pady=(2, 20), padx=30, anchor='w')
    
    #Creo un boton para ejecutar el login
    button_login = CTkButton(master=widget_form, text="Iniciar Sesion", corner_radius=8, fg_color='#3a7ff6', text_color='white', font=('Arial', 15, 'bold'), command=lambda: verification_logout(window, input_user.get(), input_pass.get()))
    button_login.pack(padx=20, pady=20, fill=tk.X)
    button_login.bind("<Return>", (lambda event=None: button_login.invoke()))
    
def verification_logout(window, user_name, password):
    res = ls.UsersServices.login(user_name, password)
    # print(f"Obtuve la siguiente response {res}")
    if isinstance(res.id, int) and res:
        messagebox.showinfo(message='Te haz logueado', title='Login')
        window.destroy()
        MasterPanel(res)
    elif isinstance(res, str) and "instance matching query does not exist" in res:
        messagebox.showerror(message='No existe el usuario.', title='Login')
    elif isinstance(res, bool) and not res:
        messagebox.showerror(message='La contraseña es incorrecta.', title='Login')
    else:
        messagebox.showerror(message='Error desconocido.', title='Login')
    