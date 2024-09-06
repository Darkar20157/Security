from PIL import Image, ImageTk
import customtkinter as ctk
import cv2
import face_recognition as fr
import numpy as np
import mediapipe as mp
# import app.utils.generic as utl
import os

img_scan_sign_success = cv2.imread("./app/resources/img/scan_sign_success.png")
img_scan_sign_error = cv2.imread("./app/resources/img/scan_sign_error.png")
img_scan_sign_process = cv2.imread("./app/resources/img/scan_sign_process.png")

class FaceIDSign:  
    def __init__(self, on_person_recognized=None) -> None:
        self.on_person_recognized = on_person_recognized
        
        self.top_window = ctk.CTkToplevel()
        self.top_window.geometry("1280x720")
        self.top_window.title("Face ID Scanner")
        
        self.video_frame = ctk.CTkLabel(master=self.top_window)
        self.video_frame.pack(padx=20, pady=20)
        
        self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        self.cap.set(3, 1280)
        self.cap.set(4, 720)
        
        self.reconigtion = False
        self.mp_face_detection = mp.solutions.face_detection
        self.face_detection = self.mp_face_detection.FaceDetection(min_detection_confidence=0.2)
        self.mp_drawing = mp.solutions.drawing_utils
        
        print("Tamaño de la imagen de error:", img_scan_sign_error.shape)

        
        #Logica principal
        self.face_data = {}
        self.frame_count = 0
        self.images = []
        self.var_class = []
        self.files = os.listdir("./app/resources/faces")
        
        #Eliminamos de la lista imagen default
        if "default.png" in self.files:
            self.files.remove('default.png')
        
        self.faces_encondings = self.code_image_initial()
        self.update_camera()
        
        self.top_window.protocol("WM_DELETE_WINDOW", self.on_close)
        self.top_window.mainloop()
    
    def update_camera(self):
        ret, frame = self.cap.read()
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        if ret:
            if self.reconigtion is False:
                self.person_exist = img_scan_sign_process
            #Este es un contador para saber cada cuanto hacer el reconocimiento facial
            self.frame_count += 1
            display_frame = frame.copy()
            #Cada 40 frames hace un reconocimiento facil sin esto la camara se veria muy lagueada
            if self.frame_count % 50 == 0:    
                res = self.face_detection.process(frame_rgb)
                if res.detections:
                    for detections in res.detections:
                        bboxC = detections.location_data.relative_bounding_box
                        ih, iw, _ = frame.shape
                        x, y, w, h = int(bboxC.xmin * iw), int(bboxC.ymin * ih), int(bboxC.width * iw), int(bboxC.height * ih)
                        cv2.rectangle(display_frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                        faces = fr.face_locations(frame_rgb)
                        faces_encoding = fr.face_encodings(frame_rgb, faces)
                        for faces_encoding, faces_location in zip(faces_encoding, faces):
                            match = fr.compare_faces(list(self.faces_encondings.keys()), faces_encoding)
                            similarity = fr.face_distance(list(self.faces_encondings.keys()), faces_encoding)
                            minimum = np.argmin(similarity)
                            if similarity[minimum] < 0.6:
                                name = list(self.faces_encondings.values())[minimum]
                                self.person_exist = img_scan_sign_success
                                self.reconigtion = True
                                if self.on_person_recognized:
                                    self.top_window.after(2000, self.on_close(name))
                                    print("Si existe esa persona")
                                    return True
                            else:
                                self.person_exist = img_scan_sign_error
                                self.reconigtion = True
                                print("Esa persona no existe")
                                
            if self.frame_count % 70 == 0:
                self.reconigtion = False
            display_frame[100:100 + 200, 1000:1000 + 200] = self.person_exist
            display_frame = cv2.cvtColor(display_frame, cv2.COLOR_BGR2RGB)
            display_frame = cv2.resize(display_frame, (1280, 720))  # Redimensionar para que se ajuste al tamaño de la ventana
            display_frame = Image.fromarray(display_frame)
            display_frame = ImageTk.PhotoImage(image=display_frame)
            self.video_frame.configure(image=display_frame)
            self.video_frame.image = display_frame  # Actualiza la referencia interna en customtkinter
        
        self.top_window.after(30, self.update_camera)
        
    
    def code_image_initial(self):
        list_code = {}
        try:
            for image in self.files:
                if self.check_image_bit(f"./app/resources/faces/{image}"):
                    img = cv2.imread(f"./app/resources/faces/{image}")
                    if img is not None:
                        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                        encoding = fr.face_encodings(img)
                        if encoding:
                            list_code[tuple(encoding[0])] = os.path.splitext(image)[0]
                else:
                    print(f"No se pudo cargar la imagen: {image}")
        except Exception as e:
            print(e)        
            return e
        return list_code
            

    def check_image_bit(self, path_image):
        img = cv2.imread(path_image, cv2.IMREAD_UNCHANGED)
        if img.dtype == 'uint8':
            print(f"8 bits {img.dtype}")
            return True
        elif img.dtype == 'uint16':
            print(f"16 bits {img.dtype}")
            return False
        else:
            print(f"No es 8 bits")
            return False
        
    def on_close(self, name=None):
        cv2.destroyAllWindows()
        self.top_window.destroy()
        if self.on_person_recognized and name is not None:
            self.on_person_recognized(name)
        
res = FaceIDSign()