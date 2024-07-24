import customtkinter as ctk

def construct_frame_logo_scan(window, logo, position):
    try:
        #Frame izquierdo para representa logo
        #Creamos un frame para que en la ventana tome backgrounds, ancho, padding x o y 
        
        widget_logo = ctk.CTkFrame(window, width=300, relief=ctk.SOLID, padx=0, pady=10, bg='#3a7ff6')
        #En el frame le decimos hacia que lado lo vamos a dirigir en este caso left
        
        #Indicamos la posicion del contenedor que va hacer left y ponemos que no se Expandible
        widget_logo.pack(side=position, expand=tk.NO, fill=tk.BOTH)
        
        #Agregamos un label (imagen) dentro del frame_logo que seria el widget y le damos un background 
        # y le damos la img procesada
        label = tk.Label(widget_logo, image=logo, bg='#3a7ff6')
        
        #Posicionamos el label
        label.place(x=0, y=0, relwidth=1, relheight=1)
    except Exception as e:
        print(f"Error: {e}")
    return widget_logo