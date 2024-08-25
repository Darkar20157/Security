import math
from PIL import Image, ImageTk
import customtkinter as ctk
import cv2
import mediapipe as mp
import os


img_info = cv2.imread("./app/resources/img/recognition_facial_info.png")
img_look_cam = cv2.imread("./app/resources/img/look_cam.png")
img_look_cam_er = cv2.imread("./app/resources/img/look_cam_error.png")
img_look_cam_sc = cv2.imread("./app/resources/img/look_cam_success.png")
img_blinks = cv2.imread("./app/resources/img/blinks.png")
register_success = cv2.imread("./app/resources/img/register_success.png")

class ScanFaceID:
    def __init__(self, document_nro, on_close_callback=None):
        # Media pipe
        self.faceID_success = False
        self.on_close_callback = on_close_callback
        self.document_nro = document_nro
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
        
        ########################Boton para tomar la capturar la imagen si el parpadeo no funciona###########################
        self.btn_capture = ctk.CTkButton(master=self.window_modal, text='Capture Face', command=self.capture)
        self.btn_capture.pack(pady=10)
        #####################################################################################################################
        
        self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        self.cap.set(3, 1280)
        self.cap.set(4, 720)
        
        self.faces = [] # Lista para almacenar las imagenes de los rostros capturados
        
        self.update_camera()
        self.window_modal.protocol("WM_DELETE_WINDOW", self.on_close)
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
        self.frame_save = frame.copy() # este frame es la foto cuando termina de hacer los 3 parpadeos
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
                                            img_info_y, img_info_x, img_info_b = img_info.shape
                                            
                                            #Se agrega mensajes de faceID
                                            frame[100:100 + img_info_y, 50:50 + img_info_x] = img_info
                                            
                                            frame[400:400 + 200, 1000:1000 + 200] = img_blinks
                                            
                                            #Face_Center
                                            if eyebrow_x1 > pleftx1 and eyebrow_x2 < prightx:
                                                frame[100:100 + 200, 1000:1000 + 200] = img_look_cam_sc #Se coloca 200 ya que la img 200x200 deberia ser configurable
                                                #Draw
                                                cv2.rectangle(frame, (xi, yi, w, h), (0,255,0), 2)
                                            else:
                                                frame[100:100 + 200, 1000:1000 + 200] = img_look_cam_er #Se coloca 200 ya que la img 200x200 deberia ser configurable
                                                cv2.rectangle(frame, (xi, yi, w, h), (0,0,254), 2)
                                                self.count = 0
                                                
                                            #Count Blink
                                            if longitud1 <= 10 and longitud2 <= 10 and self.blink == False:
                                                self.count = self.count + 1
                                                self.blink = True
                                            elif longitud1 > 10 and longitud2 > 10 and self.blink == True:
                                                self.blink = False
                                                
                                            cv2.putText(frame, f'{int(self.count)}', (1090, 520), cv2.QT_FONT_NORMAL, 0.8, (255, 255, 255), 2)
                                            if self.count >= 3:
                                                #Open Eyes
                                                if longitud1 > 15 and longitud2 > 15:
                                                    #save face
                                                    cut = self.frame_save[yi:yf, xi:xf]
                                                    # cv2.imwrite(f"./app/resources/faces/{self.user.entry_document_nro.get()}.png", cut)
                                                    cv2.imwrite(f"./app/resources/faces/{self.document_nro}.png", cut)
                                                    #Step1
                                                    self.step = 1
                                                    
                                        if self.step == 1:
                                            self.faceID_success = True
                                            frame[100:100 + 200, 50:50 + 300] = register_success
                                            cv2.rectangle(frame, (xi, yi, w, h), (0,255,0), 2)
                    
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
        cv2.destroyAllWindows()
        self.window_modal.destroy()
        if self.on_close_callback:
            self.on_close_callback()
        
if __name__ == "__main__":
    app = ScanFaceID(1005714270)