from PIL import Image
from customtkinter import *
from tkcalendar import Calendar
from tkinter import messagebox


from app.model.persons import Persons
import app.utils.generic as utl
from app.views.scan.scan_face_id_register import ScanFaceID
from app.services.person_services import PersonServices

class RegisterPerson:
    def __init__(self, window):
        self.new_window = CTkToplevel(window)
        self.new_window.title('Registrar Persona')
        self.new_window.geometry("500x600")
        
        self.frame_main = CTkScrollableFrame(master=self.new_window, fg_color='#fcfcfc', orientation='vertical')
        self.frame_main.pack(fill='both', expand=True)
        
        self.title = CTkLabel(master=self.frame_main, text='Registrar Persona', font=('Arial', 20, 'bold'))
        self.title.pack(pady=10)
        
        #Form
        
        #UP FORM
        self.frame_up = CTkFrame(master=self.frame_main, fg_color='#f5f5f5', corner_radius=50)
        self.frame_up.pack(side='top', pady=10)
        
        self.image_person = CTkImage(light_image=utl.add_corners(Image.open("./app/resources/faces/default.png"), 100, True), dark_image=utl.add_corners(Image.open("./app/resources/faces/default.png"), 100, True),
                                     size=(150, 150))
        self.label_image_person = CTkLabel(master=self.frame_up, text="", image=self.image_person, corner_radius=50)
        self.label_image_person.pack(pady=10, padx=16)
        
        #LEFT FORM
        self.frame_secondary_left = CTkFrame(master=self.frame_main, fg_color='#f5f5f5')
        self.frame_secondary_left.pack(side='left', expand=True)
        
        #DOCUMENT_TYPE
        self.label_document_type = CTkLabel(master=self.frame_secondary_left, text='Tipo Documento (*)', font=('Arial', 15, 'bold')) #LABEL
        self.label_document_type.pack(pady=(5, 0), padx=10, anchor='w') #LABEL.pack
        
        self.entry_document_type = CTkComboBox(master=self.frame_secondary_left, values=['Cedula Ciudadania', 'Tarjeta Identidad'], width=200, height=35) #ENTRY
        self.entry_document_type.pack(pady=5, padx=5, anchor='w') #ENTRY.pack
        
        #FIRST_NAME
        self.label_first_name = CTkLabel(master=self.frame_secondary_left, text='Nombre (*)', font=('Arial', 15, 'bold')) #LABEL
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
        self.frame_secondary_right = CTkFrame(master=self.frame_main, fg_color='#f5f5f5')
        self.frame_secondary_right.pack(side='right', expand=True)
        
        #DOCUMENT_NRO
        self.label_document_nro = CTkLabel(master=self.frame_secondary_right, text='Numero Documento (*)', font=('Arial', 15, 'bold')) #LABEL
        self.label_document_nro.pack(pady=(5, 0), padx=10, anchor='w') #LABEL.pack
        
        self.entry_document_nro = CTkEntry(master=self.frame_secondary_right, placeholder_text='Digita el Numero Documento', width=200, height=35) #ENTRY
        self.entry_document_nro.pack(pady=5, padx=5, anchor='w') #ENTRY.pack
        
        #LAST_NAME
        self.label_last_name = CTkLabel(master=self.frame_secondary_right, text='Apellido (*)', font=('Arial', 15, 'bold')) #LABEL
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
        
        self.entry_faceID = CTkButton(master=self.frame_secondary_right, text='Escanear', fg_color='#3a7ff6', width=200, height=47, command=lambda: self.activate_scan_faceID())
        self.entry_faceID.pack(pady=5, padx=5, anchor='w') #ENTRY.pack
        
        self.new_window.protocol("WM_DELETE_WINDOW", self.on_close)
        
    def activate_scan_faceID(self):
        if self.entry_document_nro.get() is None or self.entry_document_nro.get() == "":
            messagebox.showerror(title="Información", message="No puedes registrar un FaceID sino haz colocado el numero de documento")
            return False
        
        if self.entry_document_nro.get() is not None or self.entry_document_nro.get() != "":
            person = PersonServices.get_person_filter(self.entry_document_nro.get(), None, None)
            if person is not None:
                messagebox.showinfo(title="Información", message="La persona ya fue creada hazle el escaneo facial")
                return False
    #CON AYUDA DEL SERVICE COMVERTIMOS LOS DATOS DE SELF EN EL MODELO DE PERSONS Y SE PROCEDE A GUARDAR LA IMAGEN CON EL NRO DOCUMENTO Y SE GUARDARA EN FACES PARA DESPUES GUARDAR
    #EL PERSON
        def post_scan_callback():
            try:
                if os.path.exists(f"./app/resources/faces/{self.entry_document_nro.get()}.png"):
                    #Seteamos la imagen en el label que tomamos del faceID
                    self.image_person = CTkImage(light_image=utl.add_corners(Image.open(f"./app/resources/faces/{self.entry_document_nro.get()}.png"), 100, False), dark_image=utl.add_corners(Image.open(f"./app/resources/faces/{self.entry_document_nro.get()}.png"), 100, False), size=(200,200))
                    self.label_image_person.configure(image=self.image_person)
                    
                    self.button_save_form = CTkButton(master=self.frame_secondary_right, text="Guardar Persona", fg_color="#00bb00", width=200, height=47, command=lambda: self.save_form(self.entry_document_nro.get(), self.entry_document_type.get(), self.entry_first_name.get(),
                                            self.entry_last_name.get(), self.entry_phone.get(), self.entry_email.get(), self.entry_birthday.get_date(), self.entry_address.get()))
                    self.button_save_form.pack(side='bottom', pady=5, padx=5, anchor='w')
            except ValueError as e:
                messagebox.showerror("Error al ingresar los datos", message=e)        
        ScanFaceID(self.entry_document_nro.get(), on_close_callback=post_scan_callback)
        
    def save_form(self, document_nro, type_document, first_name, last_name, phone, email, age, location):
        try:
            result = PersonServices.save_person(document_nro, type_document, first_name, last_name, phone, email, age, location)
            if result is not None and int(result.id):
                messagebox.showinfo("Proceso Exitoso", message=f"La persona {result.first_name} {result.last_name} fue guardado correctamente")
                self.on_close
        except Exception as e:
            messagebox.showerror("Ups hubo un error inesperado", message=f"El usuario no fue guardado por motivo: {e}")
    
    def on_close(self):
        self.new_window.destroy()
        self = None
    