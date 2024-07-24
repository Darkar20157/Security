import tkinter as tk
from tkinter import messagebox
from customtkinter import *
from PIL import Image
import app.services.login_services as ls
from app.views.register_person.modules.form_register_person import RegisterPerson

def contruct_form_register_person(window, first_name, last_name):
    widget_form = CTkFrame(window, fg_color='#fcfcfc')
    widget_form.pack(side='right', expand=tk.YES, fill=tk.BOTH, padx=20)
    
    #Texto titulo
    title_form = CTkLabel(master=widget_form, text="Bienvenido "+first_name+" "+last_name, font=("Arial", 25, "bold"))
    title_form.pack(pady=(30, 10), padx=30, anchor='w')
    
    #list_widget
    list_widget_frame1 = CTkFrame(master=widget_form, fg_color='#3a7ff6', border_width=4, border_color='#3576e6', corner_radius=15)
    list_widget_frame1.pack(pady=10, side='top', fill='x')
    
    data1 = CTkLabel(master=list_widget_frame1, text="Usuario: Danny Alejandro, Ultima Entrada: 25-08-2024 13:00:01, Hora Salida: 26-08-2024 07:05:00", font=('Arial', 15), wraplength=452)
    data1.pack(pady=15, padx=15, anchor='w')
    
    list_widget_frame2 = CTkFrame(master=widget_form, fg_color='#3a7ff6', border_width=4, border_color='#3576e6', corner_radius=15)
    list_widget_frame2.pack(pady=10, side='top', fill='x')
    
    data2 = CTkLabel(master=list_widget_frame2, text="Usuario: Danny Alejandro, Ultima Entrada: 25-08-2024 13:00:01, Hora Salida: 26-08-2024 07:05:00", font=('Arial', 15), wraplength=452)
    data2.pack(pady=15, padx=15, anchor='w')
    
    list_widget_frame3 = CTkFrame(master=widget_form, fg_color='#3a7ff6', border_width=4, border_color='#3576e6', corner_radius=15)
    list_widget_frame3.pack(pady=10, side='top', fill='x')
    
    data3 = CTkLabel(master=list_widget_frame3, text="Usuario: Danny Alejandro, Ultima Entrada: 25-08-2024 13:00:01, Hora Salida: 26-08-2024 07:05:00", font=('Arial', 15), wraplength=452)
    data3.pack(pady=15, padx=15, anchor='w')
    
    list_widget_frame4 = CTkFrame(master=widget_form, fg_color='#3a7ff6', border_width=4, border_color='#3576e6', corner_radius=15)
    list_widget_frame4.pack(pady=10, side='top', fill='x')
    
    data4 = CTkLabel(master=list_widget_frame4, text="Usuario: Danny Alejandro, Ultima Entrada: 25-08-2024 13:00:01, Hora Salida: 26-08-2024 07:05:00", font=('Arial', 15), wraplength=452)
    data4.pack(pady=15, padx=15, anchor='w')
    
    #Buttons Options
    frame_options = CTkFrame(master=widget_form, fg_color='#fcfcfc')
    frame_options.pack(pady=10, side='left', fill='x')
    
    #button exit
    icon_exit = CTkImage(light_image=Image.open('./app/resources/icons/salir.png'), dark_image=Image.open('./app/resources/icons/salir.png'), size=(50, 50))
    btn_exit = CTkButton(master=frame_options, image=icon_exit, fg_color='#3a7ff6', command=lambda: btn_exit_program(window))
    btn_exit.pack(padx=10, side='left')
    
    #Button register person
    icon_register_person = CTkImage(light_image=Image.open('./app/resources/icons/addPerson.png'), dark_image=Image.open('./app/resources/icons/addPerson.png'), size=(50, 50))
    btn_register_person = CTkButton(master=frame_options, image=icon_register_person, fg_color='#3a7ff6', command=lambda: register_person_form(window))
    btn_register_person.pack(padx=10, side='left')
    

def btn_exit_program(window):
    window.destroy()
    os.startfile('main.py')
    
def register_person_form(window):
    RegisterPerson(window)