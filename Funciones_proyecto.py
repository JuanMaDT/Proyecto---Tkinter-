import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# FUNCIONES USADAS
#AJUSTE DE BRILLO
def ajustar_brillo(img, factor):
    arr = np.array(img, dtype=np.float32) #Convierte imagen a arreglo 
    arr = arr * factor #Multiplica cada pixel por factor 
    arr = np.clip(arr, 0, 255) #Limite de valores entre 0 y 255 para evitar desbordamiento
    return Image.fromarray(arr.astype(np.uint8)) #Convierte de vuelta a imagen PIL 
#CANALES RGB
def aplicar_canales(img, r_activo, g_activo, b_activo):
    arr = np.array(img, dtype=np.float32) #Convierte la imagen en arreglo
    if not r_activo: 
        arr[:, :, 0] = 0 #Si el rojo no está activo lo pone en 0
    if not g_activo:
        arr[:, :, 1] = 0 #Si el verde no está activo lo pone en 0
    if not b_activo: 
        arr[:, :, 2] = 0 #Si el azul no está activo lo pone en 0 
    return Image.fromarray(arr.astype(np.uint8)) #Reconstruye la imagen con canales modificados 
#FUSION IMAGENES 
def fusionar_imagenes(img1, img2):
    a1 = np.asarray(img1) #Convierte las imagenes a arreglo 
    a2 = np.asarray(img2)
    #Si alguna imagen tiene RGBA se elimina y lleva solo a RGB
    if a1.ndim == 3 and a1.shape[2] == 4:
        a1 = a1[:, :, :3]
    if a2.ndim == 3 and a2.shape[2] == 4:
        a2 = a2[:, :, :3]
    
    #Si están en escala de grises, se lleva a RGB 
    if a1.ndim == 2:
        a1 = np.stack([a1, a1, a1], axis=-1)
    if a2.ndim == 2:
        a2 = np.stack([a2, a2, a2], axis=-1)

    #Se determina el tamaño minimo entre las imagenes para recortar 
    h = min(a1.shape[0], a2.shape[0])
    w = min(a1.shape[1], a2.shape[1])
    #Se recortan ambas imagenes para que coincidan en tamaño 
    a1c = a1[:h, :w, :]
    a2c = a2[:h, :w, :]
    #Lleva valores a rango 0 - 1 si están en 0 - 255
    def to_float01(x):
        x = x.astype(np.float32)
        if x.max() > 1.0:
            x = x / 255.0
        return x
    
    f1 = to_float01(a1c)#Normaliza imagenes 1 y 2 
    f2 = to_float01(a2c)
    imgF = (f1 + f2) / 2.0 #Fusion promediando pixeles 
    return Image.fromarray((imgF * 255).astype(np.uint8))#Se convierte de vuelta a imagen 0-255

#ESCALA DE GRISES 
def escala_grises_promedio(img):
    arr = np.asarray(img, dtype=np.float32) #Convierte la imagen a arreglo 
    if arr.ndim == 3: #Verifica sus dimensiones  
        gris = (arr[:, :, 0] + arr[:, :, 1] + arr[:, :, 2]) / 3 #Calcula promedio RGB
    else:
        gris = arr #Si ya es escala de grises la deja igual  
    return Image.fromarray(gris.astype(np.uint8))  #Devuelve la imagen en PIL e int 8

#BINARIZACION IMAGEN 
def binarizar_imagen(img, umbral):
    arr = np.asarray(img, dtype=np.float32) #Convierte la imagen a arreglo
    if arr.ndim == 3: #Verifica sus tres canales 
        gris = (arr[:, :, 0] + arr[:, :, 1] + arr[:, :, 2]) / 3 #La lleva a escala de grises usando el promedio
    else:
        gris = arr #Si ya es escala de grises la deja igual
    thr = float(umbral) #Convierte el umbral a float
    if thr <= 1.0:
        thr = thr * 255.0 #Si el umbral está entre 0 y 1 lo lleva a 0-255
    img_bin = (gris > thr).astype(np.uint8) * 255 #Binariza la imagen según el umbral
    return Image.fromarray(img_bin.astype(np.uint8)) #Devuelve la imagen en PIL e int 8

# ROTACION IMAGEN
def rotar_imagen(img, angulo):
    if isinstance(img, Image.Image): #La convierte a arreglo si es imagen PIL
        img = np.array(img) 

    ang = np.radians(angulo) #Convierte el angulo de grados a radianes
    cos_ang = np.cos(ang) #Calcula coseno y seno del angulo
    sin_ang = np.sin(ang) 
    n, m = img.shape[:2] #Extrae dimensiones de la imagen

    # Calcular nuevas dimensiones para que toda la imagen quepa
    #Estima el nuevo ancho y alto de la imagen rotada 
    new_w = int(abs(m * cos_ang) + abs(n * sin_ang)) #Calcula el nuevo ancho
    new_h = int(abs(n * cos_ang) + abs(m * sin_ang)) #Calcula el nuevo alto

    # Calcular centro
    cx, cy = m // 2, n // 2 #Centro original de la imagen
    new_cx, new_cy = new_w // 2, new_h // 2 #Centro de la nueva imagen

    rotated = np.zeros((new_h, new_w, 3), dtype=np.uint8) #Crea una nueva imagen vacía con las nuevas dimensiones

    for i in range(new_h): #Recorre cada pixel de la nueva imagen
        for j in range(new_w): 
            x = int((j - new_cx) * cos_ang + (i - new_cy) * sin_ang + cx) #Aplica la transformación inversa para encontrar el pixel original
            y = int(-(j - new_cx) * sin_ang + (i - new_cy) * cos_ang + cy)
            if 0 <= y < n and 0 <= x < m: #Verifica que las coordenadas estén dentro de los límites de la imagen original
                rotated[i, j] = img[y, x] #Asigna el valor del pixel original a la nueva imagen

    return Image.fromarray(rotated) #Devuelve la imagen rotada en formato PIL

#ZOOM CENTRAL 
def zoom_central(img, zoom_factor=1.0):
    if zoom_factor == 1.0: #No aplica zoom si el factor es 1
        return img

    if isinstance(img, Image.Image): #Convierte la imagen a arreglo si es PIL
        arr = np.asarray(img) 
    else: #Si ya es arreglo la deja igual y la usa directamente
        arr = img

    h, w = arr.shape[:2] #Extrae las dimensiones de la imagen
    zoom_area_h = int(h / zoom_factor) #Calcula el área de zoom en altura
    zoom_area_w = int(w / zoom_factor) #Calcula el área de zoom en ancho

    start_row = max(0, (h - zoom_area_h) // 2) #Calcula las coordenadas de inicio y fin del recorte
    end_row = start_row + zoom_area_h
    start_col = max(0, (w - zoom_area_w) // 2) #Calcula las coordenadas de inicio y fin del recorte
    end_col = start_col + zoom_area_w

    recorte = arr[start_row:end_row, start_col:end_col] #Recorta la imagen en el área de zoom
    zoomed = np.array(Image.fromarray(recorte).resize((w, h), Image.LANCZOS)) #Redimensiona el recorte a las dimensiones originales usando interpolación Lanczos

    return Image.fromarray(zoomed) #Devuelve la imagen con zoom en formato PIL

#FOTO NEGATIVA 
def foto_negativa(img):
    if isinstance(img, Image.Image): #Verifica si la imagen es PIL y la convierte a arreglo
        arr = np.asarray(img, dtype=np.uint8)
    else: #Si ya es arreglo la deja igual y la usa directamente
        arr = img

    # Inversión manual: 255 - valor
    negativo = 255 - arr #Calcula el negativo restando cada valor de pixel a 255

    return Image.fromarray(negativo.astype(np.uint8)) #Devuelve la imagen negativa en formato PIL
#CONTRASTE LOGARITMICO
def contraste_log(img):
    if isinstance(img, Image.Image): #Verifica si la imagen es PIL y la convierte a arreglo
        arr = np.asarray(img, dtype=np.float32) / 255.0
    else: #Si ya es arreglo la normaliza y pasa a float32
        arr = img.astype(np.float32) / 255.0

    img_log = np.log10(1 + arr) #Aplica la transformación logarítmica
    img_log = img_log / np.max(img_log)  # Normalización
    return Image.fromarray((img_log * 255).astype(np.uint8)) #Convierte la imagen de vuelta a formato PIL
#CONTRASTE EXPONENCIAL
def contraste_exp(img):
    if isinstance(img, Image.Image): #Verifica si la imagen es PIL y la convierte a arreglo
        arr = np.asarray(img, dtype=np.float32) / 255.0
    else: #Si ya es arreglo la normaliza y pasa a float32
        arr = img.astype(np.float32) / 255.0

    img_exp = np.exp(arr) - 1 #Aplica la transformación exponencial
    img_exp = img_exp / np.max(img_exp)  # Normalización
    return Image.fromarray((img_exp * 255).astype(np.uint8)) #Convierte la imagen de vuelta a formato PIL

#HISTOGRAMA 
def mostrar_histograma(img):
    if isinstance(img, Image.Image): #Verifica si la imagen es PIL y la convierte a arreglo
        img = np.array(img) 
    
    # Asegurar que los valores estén en 0-255
    if img.max() <= 1.0:
        img = (img * 255).astype(np.uint8)
    
    # Separar canales
    R = img[:, :, 0]
    G = img[:, :, 1]
    B = img[:, :, 2]
    
    # Crear figura con 3 subplots 
    plt.figure(figsize=(10, 6))
    
    # Histograma canal rojo
    plt.subplot(3, 1, 1)
    plt.hist(R.ravel(), bins=256, color='red', alpha=0.7) #Histograma del canal rojo
    plt.title('Histograma del canal Rojo')
    plt.xlabel('Intensidad')
    plt.ylabel('Frecuencia')
    
    # Histograma canal verde
    plt.subplot(3, 1, 2)
    plt.hist(G.ravel(), bins=256, color='green', alpha=0.7) #Histograma del canal verde
    plt.title('Histograma del canal Verde')
    plt.xlabel('Intensidad')
    plt.ylabel('Frecuencia')
    
    # Histograma canal azul
    plt.subplot(3, 1, 3)
    plt.hist(B.ravel(), bins=256, color='blue', alpha=0.7) #Histograma del canal azul
    plt.title('Histograma del canal Azul')
    plt.xlabel('Intensidad')
    plt.ylabel('Frecuencia')
    
    plt.tight_layout() #Ajusta el diseño para que no se sobrepongan los elementos
    plt.show() #Muestra la figura con los histogramas

#ECUALIZACION HISTOGRAMA
def ecualizar_histograma(img):
    if isinstance(img, Image.Image): #Verifica si la imagen es PIL y la convierte a arreglo
        arr = np.array(img) 
    else:
        arr = img #Si ya es arreglo la deja igual y la usa directamente
    
    # Si es imagen a color, ecualizar cada canal
    if arr.ndim == 3: #Verifica si la imagen tiene 3 dimensiones (color)
        resultado = np.zeros_like(arr) #Crea un arreglo vacío para el resultado
        for i in range(3):
            canal = arr[:, :, i] #Selecciona el canal i (0=R, 1=G, 2=B)
            # Calcular histograma
            hist, bins = np.histogram(canal.flatten(), 256, [0, 256])
            # Calcular CDF (función de distribución acumulada)
            cdf = hist.cumsum()
            cdf_normalizado = cdf * hist.max() / cdf.max()
            # Ecualización
            cdf_m = np.ma.masked_equal(cdf, 0) #Evita dividir por cero
            cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())#Normaliza el CDF
            cdf = np.ma.filled(cdf_m, 0).astype('uint8') #Convierte el CDF a uint8
            resultado[:, :, i] = cdf[canal] #Reempa el canal con los valores ecualizados
    else:
        # Imagen en escala de grises
        hist, bins = np.histogram(arr.flatten(), 256, [0, 256]) #Calcula el histograma
        cdf = hist.cumsum() #Calcula el CDF
        cdf_m = np.ma.masked_equal(cdf, 0) #Evita dividir por cero
        cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min()) #Normaliza el CDF
        cdf = np.ma.filled(cdf_m, 0).astype('uint8') #Convierte el CDF a uint8
        resultado = cdf[arr] #Reempa la imagen con los valores ecualizados
    
    return Image.fromarray(resultado.astype(np.uint8)) #Devuelve la imagen ecualizada en formato PIL

#FUSIONAR IMAGENES ECUALIZADAS
def fusionar_ecualizadas(img1, img2): #Fusiona dos imagenes despues de ecualizarlas
    img1_eq = ecualizar_histograma(img1) #Ecualiza la primera imagen
    img2_eq = ecualizar_histograma(img2) #Ecualiza la segunda imagen
    return fusionar_imagenes(img1_eq, img2_eq) #Fusiona las dos imagenes ecualizadas

#RECORTAR IMAGEN 
def recortar_imagen(img, x1, y1, x2, y2): #Recorta la imagen según las coordenadas dadas
    if isinstance(img, Image.Image): #Verifica si la imagen es PIL y la convierte a arreglo
        arr = np.array(img)
    else:
        arr = img #Si ya es arreglo la deja igual y la usa directamente
    
    # Asegurar que las coordenadas estén dentro de los límites
    h, w = arr.shape[:2] #Obtiene las dimensiones de la imagen 
    x1 = max(0, min(x1, w)) #Asegura que x1 esté dentro de los límites
    x2 = max(0, min(x2, w)) #Asegura que x2 esté dentro de los límites
    y1 = max(0, min(y1, h))#Asegura que y1 esté dentro de los límites
    y2 = max(0, min(y2, h))#Asegura que y2 esté dentro de los límites
    
    # Asegurar que x1 < x2 y y1 < y2
    if x1 > x2: #Intercambia x1 si es mayor que x2
        x1, x2 = x2, x1
    if y1 > y2: #Intercambia y1 si es mayor que y2
        y1, y2 = y2, y1
    
    recorte = arr[y1:y2, x1:x2] #Recorta la imagen según las coordenadas dadas
    return Image.fromarray(recorte) #Devuelve la imagen recortada en formato PIL

#EXTRAER CANAL RGB 
def extraer_canal_rgb(img, canal):
    if isinstance(img, Image.Image): #Verifica si la imagen es PIL y la convierte a arreglo
        arr = np.array(img)
    else: #Si ya es arreglo la deja igual y la usa directamente
        arr = img
    
    resultado = np.zeros_like(arr) #Crea un arreglo vacío para el resultado
    
    if canal.upper() == 'R': #Extrae el canal rojo
        resultado[:, :, 0] = arr[:, :, 0]
    elif canal.upper() == 'G': #Extrae el canal verde
        resultado[:, :, 1] = arr[:, :, 1]
    elif canal.upper() == 'B': #Extrae el canal azul
        resultado[:, :, 2] = arr[:, :, 2]
    
    return Image.fromarray(resultado.astype(np.uint8))#Devuelve la imagen con el canal extraído en formato PIL

#COLOR CYAN 
def color_cyan(img): #
    if isinstance(img, Image.Image): #Verifica si la imagen es PIL y la convierte a arreglo
        arr = np.array(img, dtype=np.float32)
    else: #Si ya es arreglo la deja igual y la usa directamente
        arr = img.astype(np.float32)
    
    brillo = 0.5 #Define el nivel de brillo a aumentar
    imgCanal = np.copy(arr) #Copia el arreglo original
    
    # Aumentar canales Verde (1) y Azul (2)
    imgCanal[:, :, 1] = np.clip(arr[:, :, 1] + brillo * 255, 0, 255) #Aumenta el canal verde
    imgCanal[:, :, 2] = np.clip(arr[:, :, 2] + brillo * 255, 0, 255) #Aumenta el canal azul
    
    return Image.fromarray(imgCanal.astype(np.uint8)) #Devuelve la imagen con efecto cyan en formato PIL
#COLOR MAGENTA
def color_magenta(img):
    if isinstance(img, Image.Image): #Verifica si la imagen es PIL y la convierte a arreglo
        arr = np.array(img, dtype=np.float32)
    else: #Si ya es arreglo la normaliza y pasa a float32
        arr = img.astype(np.float32)
    
    brillo = 0.5 #Define el nivel de brillo a aumentar
    imgCanal = np.copy(arr) #Copia el arreglo original
    
    # Aumentar canales Rojo (0) y Azul (2)
    imgCanal[:, :, 0] = np.clip(arr[:, :, 0] + brillo * 255, 0, 255) #Aumenta el canal rojo
    imgCanal[:, :, 2] = np.clip(arr[:, :, 2] + brillo * 255, 0, 255) #Aumenta el canal azul
    
    return Image.fromarray(imgCanal.astype(np.uint8)) #Devuelve la imagen con efecto magenta en formato PIL

#COLOR AMARILLO
def color_amarillo(img):
    if isinstance(img, Image.Image): #Verifica si la imagen es PIL y la convierte a arreglo
        arr = np.array(img, dtype=np.float32)
    else: #Si ya es arreglo la normaliza y pasa a float32
        arr = img.astype(np.float32)
    
    brillo = 0.5 #Define el nivel de brillo a aumentar
    imgCanal = np.copy(arr) #Copia el arreglo original
    
    # Aumentar canales Rojo (0) y Verde (1)
    imgCanal[:, :, 0] = np.clip(arr[:, :, 0] + brillo * 255, 0, 255) #Aumenta el canal rojo
    imgCanal[:, :, 1] = np.clip(arr[:, :, 1] + brillo * 255, 0, 255) #Aumenta el canal verde
    
    return Image.fromarray(imgCanal.astype(np.uint8)) #Devuelve la imagen con efecto amarillo en formato PIL

#CANAL CMYK 
def extraer_canal_cmyk(img, canal):
    if canal.upper() == 'C': #Si el canal es C (cyan)
        return color_cyan(img)
    elif canal.upper() == 'M': #Si el canal es M (magenta)
        return color_magenta(img)
    elif canal.upper() == 'Y': #Si el canal es Y (amarillo)
        return color_amarillo(img)
    elif canal.upper() == 'K': #Si el canal es K (negro)
        return foto_negativa(img)
    else: 
        return img
    
    