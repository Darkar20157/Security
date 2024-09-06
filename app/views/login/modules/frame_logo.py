import tkinter as tk
import customtkinter as ctk
from app.views.scan.scan_face__id_sign import FaceIDSign
from PIL import Image
    
def construct_frame_logo(window, logo, position, btn_scan):
    try:
        #Frame izquierdo para representa logo
        #Creamos un frame para que en la ventana tome backgrounds, ancho, padding x o y 
        
        widget_logo = tk.Frame(window, width=300, relief=tk.SOLID, padx=0, pady=10, bg='#3a7ff6')
        #En el frame le decimos hacia que lado lo vamos a dirigir en este caso left
        
        #Indicamos la posicion del contenedor que va hacer left y ponemos que no se Expandible
        widget_logo.pack(side=position, expand=tk.NO, fill=tk.BOTH)
        
        #Agregamos un label (imagen) dentro del frame_logo que seria el widget y le damos un background 
        # y le damos la img procesada
        label = tk.Label(widget_logo, image=logo, bg='#3a7ff6')
        
        #Posicionamos el label
        label.place(x=0, y=0, relwidth=1, relheight=1)
        if btn_scan:
            logo_imagen = ctk.CTkImage(light_image=Image.open('./app/resources/img/logo.png'), dark_image=Image.open('./app/resources/img/logo.png'), size=(200, 200))
            button_scan = ctk.CTkButton(master=widget_logo, image=logo_imagen, text='', bg_color='transparent', fg_color='transparent', hover=None, width=300, height=200, corner_radius=0, command=lambda: FaceIDSign(on_person_recognized=post_scan_callback))
            button_scan.pack(pady=(140))
    except Exception as e:
        print(f"Error: {e}")
    return widget_logo

def post_scan_callback(name):
    try:
        print(f"Entra a procesar quien es {name}")
    except ValueError as e:
        print("Error "+e)