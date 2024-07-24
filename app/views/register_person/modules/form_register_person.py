from customtkinter import *
from tkcalendar import Calendar
from app.model.persons import Persons
from app.views.scan.scan_face_id import ScanFaceID

class RegisterPerson:
    def __init__(self, window):
        self.new_window = CTkToplevel(window)
        self.new_window.title('Registrar Persona')
        self.new_window.geometry("500x600")
        
        self.frame_main = CTkFrame(master=self.new_window, fg_color='#fcfcfc')
        self.frame_main.pack(fill='x')
        
        self.title = CTkLabel(master=self.frame_main, text='Registrar Persona', font=('Arial', 20, 'bold'))
        self.title.pack(pady=10)
        
        #Form
        
        #LEFT FORM
        self.frame_secondary_left = CTkFrame(master=self.new_window, fg_color='#f5f5f5')
        self.frame_secondary_left.pack(side='left', expand=True)
        
        #DOCUMENT_TYPE
        self.label_document_type = CTkLabel(master=self.frame_secondary_left, text='Tipo Documento', font=('Arial', 15, 'bold')) #LABEL
        self.label_document_type.pack(pady=(5, 0), padx=10, anchor='w') #LABEL.pack
        
        self.entry_document_type = CTkComboBox(master=self.frame_secondary_left, values=['Cedula Ciudadania', 'Tarjeta Identidad'], width=200, height=35) #ENTRY
        self.entry_document_type.pack(pady=5, padx=5, anchor='w') #ENTRY.pack
        
        #FIRST_NAME
        self.label_first_name = CTkLabel(master=self.frame_secondary_left, text='Nombre', font=('Arial', 15, 'bold')) #LABEL
        self.label_first_name.pack(pady=(5, 0), padx=10, anchor='w') #LABEL.pack
        
        self.entry_first_name = CTkEntry(master=self.frame_secondary_left, width=200, placeholder_text='Digite su Nombre', height=35) #ENTRY
        self.entry_first_name.pack(pady=5, padx=5, anchor='w') #ENTRY.pack
        
        #PHONE
        self.label_phone = CTkLabel(master=self.frame_secondary_left, text='Celular', font=('Arial', 15, 'bold')) #LABEL
        self.label_phone.pack(pady=(5, 0), padx=10, anchor='w') #LABEL.pack
        
        self.entry_phone = CTkEntry(master=self.frame_secondary_left, width=200, placeholder_text='Digite su Numero Celular', height=35) #ENTRY
        self.entry_phone.pack(pady=5, padx=5, anchor='w') #ENTRY.pack
        
        #HAPPY BIRTHDAY
        self.label_birthday = CTkLabel(master=self.frame_secondary_left, text='Fecha Nacimiento', font=('Arial', 15, 'bold')) #LABEL
        self.label_birthday.pack(pady=(5, 0), padx=10, anchor='w') #LABEL.pack
        
        self.entry_birthday = Calendar(master=self.frame_secondary_left, selectmode='day', font=('Arial', 10, 'bold'), showweeknumbers=False, cursor="hand2", date_pattern= 'yyyy-mm-dd', borderwidth=0, bordercolor='white')
        self.entry_birthday.pack(pady=5, padx=5, anchor='w')
        
        
        #RIGHT FORM
        self.frame_secondary_right = CTkFrame(master=self.new_window, fg_color='#f5f5f5')
        self.frame_secondary_right.pack(side='right', expand=True)
        
        #DOCUMENT_NRO
        self.label_document_nro = CTkLabel(master=self.frame_secondary_right, text='Numero Documento', font=('Arial', 15, 'bold')) #LABEL
        self.label_document_nro.pack(pady=(5, 0), padx=10, anchor='w') #LABEL.pack
        
        self.entry_document_nro = CTkEntry(master=self.frame_secondary_right, placeholder_text='Digita el Numero Documento', width=200, height=35) #ENTRY
        self.entry_document_nro.pack(pady=5, padx=5, anchor='w') #ENTRY.pack
        
        #LAST_NAME
        self.label_last_name = CTkLabel(master=self.frame_secondary_right, text='Apellido', font=('Arial', 15, 'bold')) #LABEL
        self.label_last_name.pack(pady=(5, 0), padx=10, anchor='w') #LABEL.pack
        
        self.entry_last_name = CTkEntry(master=self.frame_secondary_right, width=200, placeholder_text='Digite su Apellido', height=35) #ENTRY
        self.entry_last_name.pack(pady=5, padx=5, anchor='w') #ENTRY.pack
        
        #EMAIL
        self.label_email = CTkLabel(master=self.frame_secondary_right, text='Correo', font=('Arial', 15, 'bold')) #LABEL
        self.label_email.pack(pady=(5, 0), padx=10, anchor='w') #LABEL.pack
        
        self.entry_email = CTkEntry(master=self.frame_secondary_right, width=200, placeholder_text='Digite su Numero Celular', height=35) #ENTRY
        self.entry_email.pack(pady=5, padx=5, anchor='w') #ENTRY.pack
        
        #ADDRESS
        self.label_address = CTkLabel(master=self.frame_secondary_right, text='Dirección', font=('Arial', 15, 'bold')) #LABEL
        self.label_address.pack(pady=(5, 0), padx=10, anchor='w') #LABEL.pack
        
        self.entry_address = CTkEntry(master=self.frame_secondary_right, width=200, placeholder_text='Digite la Dirección Residencia', height=35) #ENTRY
        self.entry_address.pack(pady=5, padx=5, anchor='w') #ENTRY.pack
        
        #FACEID
        self.label_faceID = CTkLabel(master=self.frame_secondary_right, text='Escaneo Facial', font=('Arial', 15, 'bold')) #LABEL
        self.label_faceID.pack(pady=(5, 0), padx=10, anchor='w') #LABEL.pack
        
        self.entry_faceID = CTkButton(master=self.frame_secondary_right, text='Escanear', fg_color='#3a7ff6', width=200, height=95, command=lambda: activate_scan_faceID(self))
        self.entry_faceID.pack(pady=5, padx=5, anchor='w') #ENTRY.pack
        
        # self.entry_birthday = CTkEntry(master=self.frame_secondary_right, width=190, placeholder_text='Coloca la Fecha Nacimiento', height=35) #ENTRY
        # self.entry_birthday.pack(pady=5, padx=5, anchor='w') #ENTRY.pack
        
        
def activate_scan_faceID(self):
    #CON AYUDA DEL SERVICE COMVERTIMOS LOS DATOS DE SELF EN EL MODELO DE PERSONS Y SE PROCEDE A GUARDAR LA IMAGEN CON EL NRO DOCUMENTO Y SE GUARDARA EN FACES PARA DESPUES GUARDAR
    #EL PERSON
    ScanFaceID(self)
        
        
        