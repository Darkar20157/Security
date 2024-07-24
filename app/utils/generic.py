from PIL import ImageTk, Image

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