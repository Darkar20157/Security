import math
from PIL import Image, ImageTk
import customtkinter as ctk
import cv2
import face_recognition as fr
import numpy as np
import mediapipe as mp
# import app.utils.generic as utl
import os


class FaceIDSign:  
    def __init__(self) -> None:
        self.top_window = ctk.CTk()
        # self.top_window = ctk.CTkToplevel()
        self.top_window.title("BIOMETRIC SIGN UP")
        self.top_window.geometry("1280x720")
        
        self.video_frame = ctk.CTkLabel(master=self.top_window)
        self.video_frame.pack(padx=20, pady=20)
        
        self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        self.cap.set(3, 1280)
        self.cap.set(4, 720)
        
        self.mp_face_detection = mp.solutions.face_detection
        self.face_detection = self.mp_face_detection.FaceDetection(min_detection_confidence=0.2)
        self.mp_drawing = mp.solutions.drawing_utils
        
        #Logica principal
        self.images = []
        self.var_class = []
        self.files = os.listdir("./app/resources/faces")
        
        #Eliminamos de la lista imagen default
        if "default.png" in self.files:
            self.files.remove('default.png')
            
        for image in self.files:
            if self.check_image_bit(f"./app/resources/faces/{image}"):
                img = cv2.imread(f"./app/resources/faces/{image}")
                if img is not None:
                    self.images.append(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
                    self.var_class.append(os.path.splitext(image)[0])
                else:
                    print(f"No se pudo cargar la imagen: {image}")
        
        self.faces_encondings = self.code_image_initial()
        self.update_camera()
        self.top_window.protocol("WM_DELETE_WINDOW", self.on_close)
        self.top_window.mainloop()
    
    def update_camera(self):
        ret, frame = self.cap.read()
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        if ret:
            display_frame = frame.copy()
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
                        match = fr.compare_faces(self.faces_encondings, faces_encoding)
                        similarity = fr.face_distance(self.faces_encondings, faces_encoding)
                        minimum = np.argmin(similarity)
                        if match[minimum]:
                            print("Si existe esa persona")
            
            display_frame = cv2.cvtColor(display_frame, cv2.COLOR_BGR2RGB)
            display_frame = cv2.resize(display_frame, (1280, 720))  # Redimensionar para que se ajuste al tamaño de la ventana
            display_frame = Image.fromarray(display_frame)
            display_frame = ImageTk.PhotoImage(image=display_frame)
            self.video_frame.configure(image=display_frame)
            self.video_frame.image = display_frame  # Actualiza la referencia interna en customtkinter
        
        self.top_window.after(30, self.update_camera)
        
    
    def code_image_initial(self):
        list_code = []
        for img in self.images:
            try:
                encoding = fr.face_encodings(img)
                if encoding:
                    list_code.append(encoding[0])
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
        
    def on_close(self):
        cv2.destroyAllWindows()
        self.top_window.destroy()
        self = None
        # if self.on_close_callback:
        #     self.on_close_callback()
        
res = FaceIDSign()