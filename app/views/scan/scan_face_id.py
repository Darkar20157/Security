import math
from PIL import Image, ImageTk
import customtkinter as ctk
import cv2
import face_recognition as fr
import numpy as np
import mediapipe as mp
import os

class ScanFaceID:
    def __init__(self, user):
        # Media pipe
        self.user = user
        self.blink = False
        self.count = 0
        self.see = 0
        self.step = 0
        self.offsety = 40
        self.offsetx = 20
        self.config_thres_hold = 0.5
        
        self.mp_draw = mp.solutions.drawing_utils
        
        self.config_draw = self.mp_draw.DrawingSpec(thickness=1, circle_radius=1)
        
        self.face_mesh_object = mp.solutions.face_mesh
        
        self.face_mesh = self.face_mesh_object.FaceMesh(max_num_faces=1)
        
        self.face_object = mp.solutions.face_detection
        self.detector = self.face_object.FaceDetection(min_detection_confidence=0.5, model_selection=1)
        
        self.window_modal = ctk.CTkToplevel()
        self.window_modal.geometry("1280x720")
        self.window_modal.title("Face ID Scanner")
        
        self.label = ctk.CTkLabel(master=self.window_modal, text="Camera Feed")
        self.label.pack(padx=20, pady=20)
        
        self.video_frame = ctk.CTkLabel(master=self.window_modal)
        self.video_frame.pack(padx=20, pady=20)
        
        self.btn_capture = ctk.CTkButton(master=self.window_modal, text='Capture Face', command=self.capture)
        self.btn_capture.pack(pady=10)
        
        self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        self.cap.set(3, 1280)
        self.cap.set(4, 720)
        
        self.faces = [] # Lista para almacenar las imagenes de los rostros capturados
        
        self.update_camera()
        
        self.window_modal.mainloop()
        
    def capture(self):
        ret, frame = self.cap.read()
        print(ret)
        if ret:
            self.faces.append(frame)
            print(f" Face captured! Total faces: {len(self.faces)}")
    
    def update_camera(self):
        ret, frame = self.cap.read()
        self.frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.frame_save = frame.copy()
        if ret:
            res = self.face_mesh.process(self.frame_rgb)
            px = []
            py = []
            list = []
            if res.multi_face_landmarks:
                for face_landmarks in res.multi_face_landmarks:
                    self.mp_draw.draw_landmarks(frame, face_landmarks, self.face_mesh_object.FACEMESH_TESSELATION, self.config_draw, self.config_draw)
                    for id, points in enumerate(face_landmarks.landmark):
                        #Valores frame.
                        hframe, wframe, c = frame.shape
                        x, y = int(points.x * wframe), int(points.y * hframe)
                        px.append(x)
                        py.append(y)
                        list.append([id, x, y])
                        
                        # 468 puntos 
                        if len(list) == 468:
                            #Eye left
                            x1, y1 = list[145][1:]
                            x2, y2 = list[159][1:]
                            #Draw point eye
                            cv2.circle(frame, (x1, y1), 2, (255,0,0), cv2.FILLED)
                            cv2.circle(frame, (x2, y2), 2, (255,0,0), cv2.FILLED)
                            longitud1 = math.hypot(x2-x1, y2-y1)
                            
                            #Pariental Izquierdo
                            pleftx1, plefty1 = list[139][1:]
                            cv2.circle(frame, (pleftx1, plefty1), 2,(0, 255, 0), cv2.FILLED)
                            
                            #Eyebrow Left
                            eyebrow_x1, eyebrow_y1 = list[70][1:]
                            cv2.circle(frame, (eyebrow_x1, eyebrow_y1), 2, (0, 255, 0), cv2.FILLED)
                            
                            #Eye Right
                            x3, y3 = list[374][1:]
                            x4, y4 = list[386][1:]
                            longitud2 = math.hypot(x4 - x3, y4 - y3)
                            
                            #Pariental Derecho
                            prightx, prighty = list[368][1:]
                            cv2.circle(frame, (prightx, prighty), 2, (0, 0, 255), cv2.FILLED)
                            
                            #Eyebrow Right
                            eyebrow_x2, eyebrow_y2 = list[300][1:]
                            cv2.circle(frame, (eyebrow_x2, eyebrow_y2), 2, (0, 0, 255), cv2.FILLED)
                            
                            
                            #Draw point eye
                            cv2.circle(frame, (x3, y3), 2, (255,0,0), cv2.FILLED)
                            cv2.circle(frame, (x4, y4), 2, (255,0,0), cv2.FILLED)
                            
                            faces = self.detector.process(self.frame_rgb)
                            if faces.detections is not None:
                                for face in faces.detections:
                                    score = face.score
                                    score = score[0]
                                    bbox = face.location_data.relative_bounding_box
                                    if score > self.config_thres_hold:
                                        #Pixels
                                        xi, yi, w, h, = bbox.xmin, bbox.ymin, bbox.width, bbox.height
                                        xi, yi, w, h = int(xi * wframe), int(yi * hframe), int(w * wframe), int(h * hframe)
                                        
                                        #Offset X
                                        offset_w = (self.offsetx / 100) * w
                                        x1 = int(xi - int(offset_w / 2))
                                        w = int(w + offset_w)
                                        xf = xi + w
                                        
                                        #Offset Y
                                        offset_h = (self.offsetx / 100) * h
                                        yi = int(yi - offset_h)
                                        h = int(h + offset_h)
                                        yf = yi + h
                                        
                                        #Steps
                                        if self.step == 0:
                                            # print(f"Ceja Izquierda {eyebrow_x1}")
                                            # print(f"Parental Derecho {prightx}")
                                            #Face_Center
                                            if eyebrow_x1 > pleftx1 and eyebrow_x2 < prightx:
                                                #Draw
                                                cv2.rectangle(frame, (xi, yi, w, h), (0,255,0), 2)
                                            else:
                                                cv2.rectangle(frame, (xi, yi, w, h), (0,0,254), 2)
                                                print("Se reinicia el conteo")
                                                self.count = 0
                                                
                                            #Count Blink
                                            if longitud1 <= 10 and longitud2 <= 10 and self.blink == False:
                                                self.count = self.count + 1
                                                self.blink = True
                                                print(f"Parpadeos {self.count}")
                                            elif longitud1 > 10 and longitud2 > 10 and self.blink == True:
                                                self.blink = False
                                                
                                            if self.count >= 3: 
                                                #Open Eyes
                                                if longitud1 > 12 and longitud2 > 12:
                                                    #save face
                                                    cut = self.frame_save[yi:yf, xi:xf]
                                                    cv2.imwrite(f"./app/resources/faces/{self.user.entry_first_name.get()}.png", cut)
                                                    
                                                    #Step1
                                                    self.step = 1
                                                    
                                        if self.step == 1:
                                            print("Se ha terminado el reconocimiento facial")
                                            cv2.rectangle(frame, (xi, yi, w, h), (0,255,0), 2)
                                            self.window_modal.protocol("WM_DELETE_WINDOW", self.on_close)
                                                    
                                    #Draw rectangle
                                    # cv2.rectangle(frame, (xi, yi, w, h), (255, 255, 255), 2)
                    
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.resize(frame, (1280, 720))  # Redimensionar para que se ajuste al tamaño de la ventana
            frame = Image.fromarray(frame)
            frame = ImageTk.PhotoImage(image=frame)
            self.video_frame.configure(image=frame)
            self.video_frame.image = frame  # Actualiza la referencia interna en customtkinter
            
        self.window_modal.after(30, self.update_camera)
        
    def on_close(self):
        self.count = 0
        self.blink = False
        self.step = 0
        self.cap.release()
        self.window_modal.destroy()
        
if __name__ == "__main__":
    app = ScanFaceID()