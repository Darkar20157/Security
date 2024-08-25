import re
import cv2
from PIL import ImageTk, Image, ImageDraw

def read_image(path, size):
    try:
        image = Image.open(path)
        image = image.resize(size, Image.LANCZOS)
        photo_image = ImageTk.PhotoImage(image)
        return photo_image
    except IOError as e:
        print(f"No se pudo abrir la imagen {path}")
        return None;
    except Exception as e:
        print(f"Error al redimensionar la imagen: {e}")
        return None
    

def center_window(window, aplication_width, aplication_height):
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    x = int((width/2) - (aplication_width/2))
    y = int((height/2) - (aplication_height/2))
    return window.geometry(f"{aplication_width}x{aplication_height}+{x}+{y}")

def add_corners(img, rad, backgroundStyle):
    
    background = Image.new('RGBA', img.size, (245, 245, 245)) 
    
    # Asegúrate de que la imagen es cuadrada
    w, h = img.size
    if w != h:
        raise ValueError("La imagen debe ser cuadrada para aplicar esquinas redondeadas")

    # Crear una imagen en escala de grises del tamaño adecuado para el radio
    circle = Image.new('L', (rad * 2, rad * 2), 0)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, rad * 2, rad * 2), fill=255)  # Usa rad * 2 para el tamaño completo del círculo

    # Crear una máscara alfa del tamaño de la imagen original
    alpha = Image.new('L', img.size, 255)
    
    # Pegar las esquinas redondeadas en la máscara alfa
    alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))  # Esquina superior izquierda
    alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))  # Esquina inferior izquierda
    alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))  # Esquina superior derecha
    alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))  # Esquina inferior derecha
    
    if backgroundStyle:
        # Aplicar la máscara alfa a la imagen original
        background.putalpha(alpha)    
        background.paste(img, (0, 0), img)
        return background
    else:
        img.putalpha(alpha)
        return img
    
def valid_email(email):
    pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if re.match(pat, email):
        return True
    else:
        return False
    
    
def check_image_bit(path_image):
    img = cv2.imread(path_image, cv2.IMREAD_UNCHANGED)
    if img.dtype == 'uint8':
        print(f"8 bits {img.dtype}")
        return True
    elif img.dtype == 'uint16':
        print(f"16 bits {img.dtype}")
        return False
    else:
        print(f"No es 8 bits")
        return False;