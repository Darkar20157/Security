import customtkinter as ctk
import app.utils.generic as utl
import app.services.person_services as ps
import app.views.login.modules.frame_logo as mdl
import app.views.register_person.register_form_person as rfp

class MasterPanel:
    def __init__(self, res):
        print("Pagina Inicial")
        self.window = ctk.CTk()
        self.window.title('Master Panel')
        self.window.geometry('800x600')
        self.window.config(bg='#fcfcfc')
        self.window.resizable(width=0, height=0)
        utl.center_window(self.window, 800, 500)
        
        logo = utl.read_image("./app/resources/img/logo.png", (200, 200))
        mdl.construct_frame_logo(self.window, logo, 'right', True)
        
        form = rfp.contruct_form_register_person(self.window, res.first_name, res.last_name)
        
        self.window.mainloop()
        
    def list_get_person():
        return ps.PersonServices.list_person()
        ps.PersonServices.get_person_filter('1234567890', None, None)