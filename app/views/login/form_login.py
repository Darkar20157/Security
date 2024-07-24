import tkinter as tk
from customtkinter import * 
import app.utils.generic as utl
import app.views.login.modules.frame_logo as mdl
import app.views.login.modules.frame_form_login as flogin
import os

class Login:
    def __init__(self):
        self.window = CTk()
        self.window.title('Inicio de Sesion')
        self.window.geometry('700x400')
        self.window.config(bg='#fcfcfc')
        self.window.resizable(width=0, height=0)
        utl.center_window(self.window, 700, 400)
        
        image_path = os.path.join(os.getcwd(), 'app', 'resources', 'img', 'logo.png')
        if not os.path.exists(image_path):
            print(f"Error: No se encontró la imagen en {image_path}")
            
        logo = utl.read_image(image_path, (200, 200))
        #Cargamos el logo
        mdl.construct_frame_logo(self.window, logo, 'left', False)
        
        #Cargamos el formulario
        form = flogin.construct_frame_form(self.window)
        
        self.window.mainloop()