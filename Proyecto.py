import tkinter as tk
from tkinter import filedialog, ttk, messagebox, simpledialog
from PIL import Image, ImageTk
from Funciones_proyecto import * #Importa todas las funciones del otro archivo

#VARIABLES GLOBALES
img_original = None #Imagen cargada originalmente
img_actual = None #Imagen actual modificada
img_fusionada = None #Imagen resultante de fusiones
gris_activo = False #Indica si la imagen está en escala de grises

#FUNCIONES PRINCIPALES
# Función para cargar una imagen
def cargar_imagen():
    global img_original, img_actual, img_fusionada, gris_activo #Variables globales
    path = filedialog.askopenfilename(filetypes=[("Imágenes", "*.jpg *.png *.jpeg *.bmp *.tiff")]) #Abre el diálogo para seleccionar imagen
    if path:
        img_original = Image.open(path).convert("RGB") #Carga la imagen y la convierte a RGB
        img_actual = img_original.copy() #Copia la imagen original para editar
        img_fusionada = None #Resetea la imagen fusionada
        gris_activo = False #Resetea el estado de escala de grises
        mostrar_imagen(img_actual) #Muestra la imagen en la interfaz

# Función para guardar la imagen actual
def guardar_imagen(): 
    global img_actual  #Variable global
    if img_actual is None: #No hay imagen cargada
        messagebox.showwarning("Advertencia", "No hay imagen para guardar")
        return
    path = filedialog.asksaveasfilename( #Diálogo para guardar imagen
        defaultextension=".png", #Extensión por defecto
        filetypes=[("PNG", "*.png"), ("JPEG", "*.jpg"), ("BMP", "*.bmp"), ("TIFF", "*.tiff")]
    )
    if path: #Si se selecciona una ruta
        img_actual.save(path) #Guarda la imagen actual
        messagebox.showinfo("Éxito", "Imagen guardada correctamente")

# Función para mostrar la imagen en la interfaz
def mostrar_imagen(img): 
    # Redimensionar para ajustar a la ventana si es muy grande
    max_size = (800, 500)
    img_display = img.copy() #Copia la imagen para mostrar
    img_display.thumbnail(max_size, Image.LANCZOS) #Redimensiona manteniendo proporciones
    
    img_tk = ImageTk.PhotoImage(img_display) #Convierte la imagen a formato compatible con Tkinter
    lbl_img.config(image=img_tk) #Actualiza la etiqueta con la nueva imagen
    lbl_img.image = img_tk #Mantiene una referencia para evitar que se elimine

#Funcion para ajustar brillo con slider
def ajustar_brillo_slider(valor):
    global img_actual, img_original, img_fusionada, gris_activo
    if img_original is None: #Verifica si hay imagen cargada
        return
    try: #Convierte el valor del slider a float
        factor = float(valor)
    except:
        return
    base = img_fusionada if img_fusionada is not None else img_original #Usa la imagen fusionada si existe
    result = ajustar_brillo(base, factor) #Aplica la funcion ajuste de brillo
    if gris_activo: #Si está en escala de grises, convierte el resultado
        result = escala_grises_promedio(result) #Convierte a escala de grises
    img_actual = result #Actualiza la imagen actual
    mostrar_imagen(img_actual) #Muestra la imagen actualizada

#Funcion para aplicar canales RGB
def aplicar_canales_rgb():
    global img_actual, img_original, img_fusionada, gris_activo
    if img_original is None: #Verifica si hay imagen cargada
        return
    base = img_fusionada if img_fusionada is not None else img_original #Usa la imagen fusionada si existe
    result = aplicar_canales(base, var_r.get(), var_g.get(), var_b.get()) #Aplica la funcion de canales RGB
    if gris_activo: #Si está en escala de grises, convierte el resultado
        result = escala_grises_promedio(result) #Convierte a escala de grises
    img_actual = result #Actualiza la imagen actual
    mostrar_imagen(img_actual) #Muestra la imagen actualizada

#Funcion para fusionar imagenes
def fusionar(): 
    global img_actual, img_fusionada, img_original, gris_activo
    path = filedialog.askopenfilename(filetypes=[("Imágenes", "*.jpg *.png *.jpeg *.bmp *.tiff")]) #Abre el diálogo para seleccionar imagen
    if path and img_original is not None: #Verifica si hay imagen cargada
        img2 = Image.open(path).convert("RGB") #Carga la segunda imagen y la convierte a RGB
        base = img_fusionada if img_fusionada is not None else img_original #Usa la imagen fusionada si existe
        img_fusionada = fusionar_imagenes(base, img2) #Aplica la funcion de fusionar imagenes
        img_actual = escala_grises_promedio(img_fusionada) if gris_activo else img_fusionada.copy() #Actualiza la imagen actual
        mostrar_imagen(img_actual) #Muestra la imagen actualizada

#Funcion para fusionar imagenes con ecualizacion
def fusionar_con_ecualizacion(): 
    global img_actual, img_fusionada, img_original, gris_activo
    if img_original is None: #Verifica si hay imagen cargada
        messagebox.showwarning("Advertencia", "Carga primero una imagen")
        return 
    path = filedialog.askopenfilename(filetypes=[("Imágenes", "*.jpg *.png *.jpeg *.bmp *.tiff")]) #Abre el diálogo para seleccionar imagen
    if path:
        img2 = Image.open(path).convert("RGB") #Carga la segunda imagen y la convierte a RGB
        base = img_fusionada if img_fusionada is not None else img_original #Usa la imagen fusionada si existe
        img_fusionada = fusionar_ecualizadas(base, img2) #Aplica la funcion de fusionar ecualizadas
        img_actual = escala_grises_promedio(img_fusionada) if gris_activo else img_fusionada.copy() #Actualiza la imagen actual
        mostrar_imagen(img_actual) #Muestra la imagen actualizada

#Funcion para activar/desactivar escala de grises
def escala_grises_toggle(): 
    global img_actual, img_original, img_fusionada, gris_activo
    if img_original is None: #Verifica si hay imagen cargada
        return 
    if not gris_activo: #Si no está en escala de grises, la convierte
        base = img_fusionada if img_fusionada is not None else img_original
        img_actual = escala_grises_promedio(base) #Convierte a escala de grises
        gris_activo = True #Actualiza el estado
    else: #Si ya está en escala de grises, restaura la imagen original o fusionada
        img_actual = img_fusionada.copy() if img_fusionada is not None else img_original.copy() #Restaura la imagen
        gris_activo = False #Actualiza el estado
    mostrar_imagen(img_actual) #Muestra la imagen actualizada

#Funcion para aplicar negativo
def aplicar_negativo(): 
    global img_actual, img_original #Variable global
    if img_original is None: #Verifica si hay imagen cargada
        return 
    base = img_actual #Usa la imagen actual
    img_actual = foto_negativa(base) #Aplica la funcion de negativo
    mostrar_imagen(img_actual) #Muestra la imagen actualizada

#Funcion para aplicar contraste logarítmico
def aplicar_contraste_log():
    global img_actual, img_original 
    if img_original is None: #Verifica si hay imagen cargada
        return
    base = img_actual #Usa la imagen actual
    img_actual = contraste_log(base) #Aplica la funcion de contraste logarítmico
    mostrar_imagen(img_actual) #Muestra la imagen actualizada

#Funcion para aplicar contraste exponencial
def aplicar_contraste_exp(): 
    global img_actual, img_original 
    if img_original is None: #Verifica si hay imagen cargada
        return 
    base = img_actual #Usa la imagen actual
    img_actual = contraste_exp(base) #Aplica la funcion de contraste exponencial
    mostrar_imagen(img_actual) #Muestra la imagen actualizada

#Funcion para binarizar con slider
def binarizar_slider(valor): #Funcion para binarizar con slider
    global img_actual, img_original, img_fusionada, gris_activo
    if img_original is None:#Verifica si hay imagen cargada
        return
    try: #Convierte el valor del slider a float
        umbral = float(valor)
    except: 
        return
    if gris_activo: #Si está en gris usa la version de la imagen base 
        fuente = escala_grises_promedio(img_fusionada if img_fusionada is not None else img_original)
    else: #Si no está en gris usa la version original
        fuente = img_fusionada if img_fusionada is not None else img_original
    resultado = binarizar_imagen(fuente, umbral) #Aplica la funcion de binarizacion
    img_actual = resultado #Actualiza la imagen actual
    mostrar_imagen(img_actual) #Muestra la imagen actualizada

#FUNCIONES PARA SLIDERS DE ROTACION Y ZOOM
def rotar_slider(valor): 
    global img_actual, img_original, img_fusionada, gris_activo
    if img_original is None: #Verifica si hay imagen cargada
        return
    try: #Convierte el valor del slider a float
        angulo = float(valor)
    except: 
        return
    base = img_fusionada if img_fusionada is not None else img_original #Usa la imagen fusionada si existe
    result = rotar_imagen(base, angulo) #Aplica la funcion de rotacion
    if gris_activo:#Si está en escala de grises, convierte el resultado
        result = escala_grises_promedio(result) #Convierte a escala de grises
    img_actual = result #Actualiza la imagen actual
    mostrar_imagen(img_actual) #Muestra la imagen actualizada

#Funcion para aplicar zoom con slider
def zoom_slider(valor):  
    global img_actual, img_original, img_fusionada, gris_activo
    if img_original is None: #Verifica si hay imagen cargada
        return
    try:
        factor = float(valor) #Convierte el valor del slider a float
    except:
        return
    base = img_fusionada if img_fusionada is not None else img_original #Usa la imagen fusionada si existe
    result = zoom_central(base, zoom_factor=factor) #Aplica la funcion de zoom
    if gris_activo: #Si está en escala de grises, convierte el resultado
        result = escala_grises_promedio(result) #Convierte a escala de grises
    img_actual = result #Actualiza la imagen actual
    mostrar_imagen(img_actual) #Muestra la imagen actualizada

#Funcion para restaurar la imagen original
def restaurar_original():
    global img_actual, img_original, img_fusionada, gris_activo
    if img_original is None: #Verifica si hay imagen cargada
        return
    img_fusionada = None #Resetea la imagen fusionada
    gris_activo = False #Resetea el estado de escala de grises
    img_actual = img_original.copy() #Restaura la imagen original
    mostrar_imagen(img_actual) #Muestra la imagen restaurada

#Funcion para ver histograma
def ver_histograma():
    global img_actual
    if img_actual is None: #Verifica si hay imagen cargada
        messagebox.showwarning("Advertencia", "No hay imagen cargada")
        return
    mostrar_histograma(img_actual) #Muestra el histograma de la imagen actual

#Aplicar ecualizacion
def aplicar_ecualizacion(): 
    global img_actual, img_original 
    if img_original is None: #Verifica si hay imagen cargada
        return
    base = img_actual #Usa la imagen actual
    img_actual = ecualizar_histograma(base) #Aplica la funcion de ecualizacion
    mostrar_imagen(img_actual) #Muestra la imagen actualizada

#Funcion para recortar imagen mediante GUI
def recortar_imagen_gui():
    global img_actual, img_original
    if img_original is None: #Verifica si hay imagen cargada
        messagebox.showwarning("Advertencia", "No hay imagen cargada")
        return
    
    # Obtener dimensiones de la imagen
    arr = np.array(img_actual) #Convierte la imagen actual a un arreglo numpy
    h, w = arr.shape[:2] #Obtiene las dimensiones de la imagen
    
    # Solicitar coordenadas
    try:
        x1 = simpledialog.askinteger("Recorte", f"X inicial (0-{w}):", minvalue=0, maxvalue=w)
        if x1 is None:
            return
        y1 = simpledialog.askinteger("Recorte", f"Y inicial (0-{h}):", minvalue=0, maxvalue=h)
        if y1 is None:
            return
        x2 = simpledialog.askinteger("Recorte", f"X final ({x1}-{w}):", minvalue=x1, maxvalue=w)
        if x2 is None:
            return
        y2 = simpledialog.askinteger("Recorte", f"Y final ({y1}-{h}):", minvalue=y1, maxvalue=h)
        if y2 is None:
            return
        
        img_actual = recortar_imagen(img_actual, x1, y1, x2, y2) #Aplica la funcion de recorte
        mostrar_imagen(img_actual) #Muestra la imagen recortada
    except Exception as e: #Maneja errores de entrada
        messagebox.showerror("Error", f"Error al recortar: {str(e)}") #Muestra mensaje de error

#FUNCIONES PARA CANALES RGB Y CMYK
def extraer_canal_r():  
    global img_actual, img_original
    if img_original is None: #Verifica si hay imagen cargada
        return 
    base = img_fusionada if img_fusionada is not None else img_original #Usa la imagen fusionada si existe
    img_actual = extraer_canal_rgb(base, 'R') #Aplica la funcion de extraer canal R
    mostrar_imagen(img_actual) #Muestra la imagen actualizada

#Funcion para extraer canal G
def extraer_canal_g():
    global img_actual, img_original
    if img_original is None: #Verifica si hay imagen cargada
        return
    base = img_fusionada if img_fusionada is not None else img_original #Usa la imagen fusionada si existe
    img_actual = extraer_canal_rgb(base, 'G') #Aplica la funcion de extraer canal G
    mostrar_imagen(img_actual) #Muestra la imagen actualizada

#Funcion para extraer canal B
def extraer_canal_b():
    global img_actual, img_original 
    if img_original is None:   #Verifica si hay imagen cargada
        return 
    base = img_fusionada if img_fusionada is not None else img_original #Usa la imagen fusionada si existe
    img_actual = extraer_canal_rgb(base, 'B') #Aplica la funcion de extraer canal B
    mostrar_imagen(img_actual) #Muestra la imagen actualizada

#Funcion para aplicar canal C
def aplicar_cyan(): 
    global img_actual, img_original #Variable global
    if img_original is None: #Verifica si hay imagen cargada
        return
    base = img_fusionada if img_fusionada is not None else img_original #Usa la imagen fusionada si existe
    img_actual = color_cyan(base) #Aplica la funcion de color cyan
    mostrar_imagen(img_actual) #Muestra la imagen actualizada

#Funcion para aplicar canal M
def aplicar_magenta():
    global img_actual, img_original 
    if img_original is None: #Verifica si hay imagen cargada
        return 
    base = img_fusionada if img_fusionada is not None else img_original #Usa la imagen fusionada si existe
    img_actual = color_magenta(base) #Aplica la funcion de color magenta
    mostrar_imagen(img_actual) #Muestra la imagen actualizada

#Funcion para aplicar canal Y
def aplicar_amarillo(): 
    global img_actual, img_original
    if img_original is None: #Verifica si hay imagen cargada
        return
    base = img_fusionada if img_fusionada is not None else img_original #Usa la imagen fusionada si existe
    img_actual = color_amarillo(base) #Aplica la funcion de color amarillo
    mostrar_imagen(img_actual) #Muestra la imagen actualizada

#INTERFAZ GRAFICA

root = tk.Tk() #Crea la ventana principal
root.title("Editor de Imágenes") #Título de la ventana
root.geometry("1000x750") #Tamaño inicial de la ventana

# Frame superior para botones principales
frame_top = ttk.Frame(root, padding=10) #Parte superior de botones 
frame_top.pack(fill="x") #Empaqueta el frame

# Primera fila de botones
#BOTON CARGAR IMAGEN 
btn_cargar = ttk.Button(frame_top, text="Cargar Imagen", command=cargar_imagen)
btn_cargar.grid(row=0, column=0, padx=3)

#BOTON GUARDAR IMAGEN 
btn_guardar = ttk.Button(frame_top, text="Guardar Imagen", command=guardar_imagen)
btn_guardar.grid(row=0, column=1, padx=3)

#BOTON FUSIONAR IMAGENES 
btn_fusion = ttk.Button(frame_top, text="Fusionar", command=fusionar)
btn_fusion.grid(row=0, column=2, padx=3)

#BOTON FUSIONAR CON ECUALIZACION
btn_fusion_eq = ttk.Button(frame_top, text="Fusionar Ecualizadas", command=fusionar_con_ecualizacion)
btn_fusion_eq.grid(row=0, column=3, padx=3)

#BOTON ESCALA DE GRISES 
btn_grises = ttk.Button(frame_top, text="Escala de Grises", command=escala_grises_toggle)
btn_grises.grid(row=0, column=4, padx=3)

#BOTON IMAGEN NEGATIVA 
btn_negativo = ttk.Button(frame_top, text="Negativo", command=aplicar_negativo)
btn_negativo.grid(row=0, column=5, padx=3)

#BOTON RESTAURAR IMAGEN ORIGINAL
btn_restaurar = ttk.Button(frame_top, text="Restaurar", command=restaurar_original)
btn_restaurar.grid(row=0, column=6, padx=3)


# Segunda fila de botones
#BOTON CONTRASTE LOGARITMICO
btn_contraste_log = ttk.Button(frame_top, text="Contraste Log", command=aplicar_contraste_log)
btn_contraste_log.grid(row=1, column=0, padx=3, pady=5)

#BOTON CONTRASTE EXPONENCIAL
btn_contraste_exp = ttk.Button(frame_top, text="Contraste Exp", command=aplicar_contraste_exp)
btn_contraste_exp.grid(row=1, column=1, padx=3, pady=5)

#BOTON VER HISTOGRAMA
btn_histograma = ttk.Button(frame_top, text="Ver Histograma", command=ver_histograma)
btn_histograma.grid(row=1, column=2, padx=3, pady=5)

#BOTON APLICAR ECUALIZACION
btn_ecualizar = ttk.Button(frame_top, text="Ecualizar", command=aplicar_ecualizacion)
btn_ecualizar.grid(row=1, column=3, padx=3, pady=5)
#BOTON RECORTAR IMAGEN
btn_recortar = ttk.Button(frame_top, text="Recortar", command=recortar_imagen_gui)
btn_recortar.grid(row=1, column=4, padx=3, pady=5)

# Frame para controles deslizantes
frame_sliders = ttk.LabelFrame(root, text="Controles Deslizantes", padding=10)
frame_sliders.pack(fill="x", padx=10, pady=5)

# Slider Brillo 
#Slider con rango de 0.5 a 2.0 para ajustar el brillo
ttk.Label(frame_sliders, text="Brillo:").grid(row=0, column=0, pady=5, sticky="w")
slider_brillo = ttk.Scale(frame_sliders, from_=0.5, to=2.0, value=1.0, orient="horizontal",
                          command=ajustar_brillo_slider, length=250)
slider_brillo.grid(row=0, column=1, columnspan=3, sticky="ew", pady=5, padx=5)

# Slider Umbral binarización
ttk.Label(frame_sliders, text="Umbral (0-255):").grid(row=1, column=0, pady=5, sticky="w")
slider_umbral = ttk.Scale(frame_sliders, from_=0, to=255, value=128, orient="horizontal",
                          command=binarizar_slider, length=250)
slider_umbral.grid(row=1, column=1, columnspan=3, sticky="ew", pady=5, padx=5)

# Slider para Rotación 
ttk.Label(frame_sliders, text="Rotación (°):").grid(row=2, column=0, pady=5, sticky="w")
slider_rotar = ttk.Scale(frame_sliders, from_=-180, to=180, value=0, orient="horizontal",
                         command=rotar_slider, length=250)
slider_rotar.grid(row=2, column=1, columnspan=3, sticky="ew", pady=5, padx=5)

# Slider para Zoom
ttk.Label(frame_sliders, text="Zoom:").grid(row=3, column=0, pady=5, sticky="w")
slider_zoom = ttk.Scale(frame_sliders, from_=0.5, to=3.0, value=1.0, orient="horizontal",
                        command=zoom_slider, length=250)
slider_zoom.grid(row=3, column=1, columnspan=3, sticky="ew", pady=5, padx=5)

# Frame para canales RGB (Checkbuttons y botones)
frame_rgb = ttk.LabelFrame(root, text="Canales RGB", padding=10)
frame_rgb.pack(fill="x", padx=10, pady=5)

# Variables para los Checkbuttons
var_r = tk.BooleanVar(value=True)
var_g = tk.BooleanVar(value=True)
var_b = tk.BooleanVar(value=True)

# Checkbuttons para activar/desactivar canales RGB
ttk.Label(frame_rgb, text="Activar/Desactivar:").grid(row=0, column=0, padx=5)
ttk.Checkbutton(frame_rgb, text="R", variable=var_r, command=aplicar_canales_rgb).grid(row=0, column=1, padx=5)
ttk.Checkbutton(frame_rgb, text="G", variable=var_g, command=aplicar_canales_rgb).grid(row=0, column=2, padx=5)
ttk.Checkbutton(frame_rgb, text="B", variable=var_b, command=aplicar_canales_rgb).grid(row=0, column=3, padx=5)

#Separador vertical
ttk.Separator(frame_rgb, orient="vertical").grid(row=0, column=4, sticky="ns", padx=10)

# Botones para extraer canales RGB
ttk.Label(frame_rgb, text="Extraer canal:").grid(row=0, column=5, padx=5)
ttk.Button(frame_rgb, text="Solo R", command=extraer_canal_r).grid(row=0, column=6, padx=3)
ttk.Button(frame_rgb, text="Solo G", command=extraer_canal_g).grid(row=0, column=7, padx=3)
ttk.Button(frame_rgb, text="Solo B", command=extraer_canal_b).grid(row=0, column=8, padx=3)

# Frame para canales CMYK
frame_cmyk = ttk.LabelFrame(root, text="Canales CMYK", padding=10)
frame_cmyk.pack(fill="x", padx=10, pady=5)

# Botones para aplicar efectos CMYK
ttk.Label(frame_cmyk, text="Aplicar efecto:").grid(row=0, column=0, padx=5)
ttk.Button(frame_cmyk, text="Cyan (C)", command=aplicar_cyan).grid(row=0, column=1, padx=5)
ttk.Button(frame_cmyk, text="Magenta (M)", command=aplicar_magenta).grid(row=0, column=2, padx=5)
ttk.Button(frame_cmyk, text="Amarillo (Y)", command=aplicar_amarillo).grid(row=0, column=3, padx=5)

# Frame para mostrar la imagen
frame_img = ttk.Frame(root)
frame_img.pack(fill="both", expand=True, padx=10, pady=10)
# Etiqueta para mostrar la imagen
lbl_img = ttk.Label(frame_img, text="Carga una imagen para comenzar", 
                    font=("Arial", 10), background="#f0f0f0")
lbl_img.pack(fill="both", expand=True)

root.mainloop()