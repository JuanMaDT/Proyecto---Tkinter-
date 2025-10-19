# Proyecto---Tkinter-
Aplicación de escritorio desarrollada en Python con interfaz gráfica Tkinter que permite procesar y transformar imágenes digitales aplicando múltiples operaciones de procesamiento de imágenes.<br>

# Descripcion <br>
## 🚀 Cómo Usar el Programa

Para iniciar el editor, ejecuta el archivo `Proyecto.py` con Python. Una vez abierta la ventana, haz clic en **"Cargar Imagen"** para seleccionar una foto desde tu computador. La imagen aparecerá en el centro de la pantalla lista para ser editada. Utiliza los botones superiores para aplicar efectos instantáneos (negativo, escala de grises, contraste), o ajusta los sliders en tiempo real para controlar brillo, rotación, zoom y binarización. Los checkboxes RGB te permiten activar/desactivar canales de color, mientras que los botones de extracción muestran cada canal por separado. Para fusionar dos imágenes, carga la primera y luego usa el botón **"Fusionar"** o **"Fusionar Ecualizadas"** para seleccionar la segunda. Puedes ver el histograma de distribución de colores con **"Ver Histograma"** y en cualquier momento usar **"Restaurar"** para volver a la imagen original. Cuando estés satisfecho con el resultado, guarda tu trabajo con el botón **"Guardar Imagen"** seleccionando el formato deseado (PNG, JPEG, BMP o TIFF). <br>

# Integrantes<br>

Juan Manuel Diaz Torres<br>
Lina Maria Calvo Castro 

# Librerias requeridas: 
pip install numpy <br> 
pip install pillow <br>
pip install matplotlib 

# FUNCIONES IMPLEMENTADAS 
# 1. BRILLO 
Ubicación: Slider "Brillo"<br>
Función: Ajusta el brillo de toda la imagen<br>
Rango: 0.5 (oscuro) a 2.0 (muy brillante)<br>
Uso: Desliza el control para ver cambios en tiempo real

# 2. BRILLO POR CANAL RGB
  Ubicación: Checkboxes R, G, B en "Canales RGB"<br>
  Función: Activa/desactiva canales de color individualmente<br>
  Uso: Desmarca un checkbox para eliminar ese color de la imagen

# 3. CONTRASTE LOGARITMICO
  Ubicación: Botón "Contraste Log"<br>
  Función: Mejora el contraste en zonas oscuras<br>
  Uso: Útil para realzar detalles en imágenes subexpuestas

# 4. CONTRASTE EXPONENCIAL
  Ubicación: Botón "Contraste Exp"<br>
  Función: Mejora el contraste en zonas claras<br>
  Uso: Útil para realzar detalles en imágenes sobreexpuestas

# 5. RECORTE IMAGEN
  Ubicación: Botón "Recortar"<br>
  Función: Recorta un área rectangular de la imagen<br>
  Uso:<br>
  Clic en "Recortar"<br>
  Ingresa X inicial (coordenada horizontal izquierda)<br>
  Ingresa Y inicial (coordenada vertical superior)<br>
  Ingresa X final (coordenada horizontal derecha)<br>
  Ingresa Y final (coordenada vertical inferior)<br>
  Ejemplo: Para recortar el centro de una imagen de 800x600:<br>
  X inicial: 200, Y inicial: 150<br>
  X final: 600, Y final: 450

# 6. ZOOM
  Ubicación: Slider "Zoom"<br>
  Función: Amplía o reduce la vista desde el centro<br>
  Rango: 0.5 (alejar) a 3.0 (acercar)<br>
  Uso: Valores > 1 hacen zoom in, valores < 1 hacen zoom out<br>

# 7. ROTACION
  Ubicación: Slider "Rotación (°)"<br>
  Función: Rota la imagen en sentido antihorario<br>
  Rango: -180° a 180°<br>
  Uso: Desliza para rotar en tiempo real

# 8. VISUALIZACION HISTOGRAMA
  Ubicación: Botón "Ver Histograma"<br>
  Función: Muestra la distribución de intensidades de cada canal RGB<br>
  Uso: Abre una ventana con 3 gráficos (R, G, B)<br>
  Interpretación:<br>

  Picos a la izquierda = imagen oscura<br>
  Picos a la derecha = imagen clara<br>
  Distribución uniforme = buen contraste
   
# 9. FUSION DE IMAGENES SIMPLE
  Ubicación: Botón "Fusionar"<br>
  Función: Combina dos imágenes mediante promedio<br>
  Uso:<br>
  Carga una imagen principal<br>
  Clic en "Fusionar"<br>
  Selecciona la segunda imagen<br>
  Se crea una mezcla 50/50

# 10. FUSION DE IMAGENES ECUALIZADAS
  Ubicación: Botón "Fusionar Ecualizadas"<br>
  Función: Ecualiza ambas imágenes antes de fusionarlas<br>
  Uso: Igual que fusión simple, pero mejora el contraste previo<br>
  Ventaja: Mejor resultado en imágenes con diferente iluminación

# 11. Extracción de Capas RGB
  Ubicación: Botones "Solo R", "Solo G", "Solo B"<br>
  Función: Muestra únicamente un canal de color<br>
  Uso:<br>
  "Solo R" → Muestra solo componente rojo<br>
  "Solo G" → Muestra solo componente verde<br>
  "Solo B" → Muestra solo componente azul

# 12. EXTRACCION DE CAPAS CMYK
  Ubicación: Botones en "Canales CMYK"<br>
  Función: Aplica efectos de color tipo impresión<br>
  Uso:<br>
  Cyan (C): Resalta azul + verde<br>
  Magenta (M): Resalta rojo + azul<br>
  Amarillo (Y): Resalta rojo + verde

# 13. FOTO NEGATIVA
  Ubicación: Botón "Negativo"<br>
  Función: Invierte todos los colores de la imagen<br>
  Uso: Efecto película negativa (oscuro → claro, claro → oscuro)

# 14. CONVERSION A ESCALA DE GRISES
  Ubicación: Botón "Escala de Grises"<br>
  Función: Convierte la imagen a blanco y negro<br>
  Método: Promedio de canales RGB<br>
  Uso: Presiona nuevamente para revertir

# 15. BINARIZACION CON UMBRAL
  Ubicación: Slider "Umbral (0-255)"<br>
  Función: Convierte la imagen a solo blanco y negro puro<br>
  Uso:<br>
  Valores bajos → más pixeles blancos<br>
  Valores altos → más pixeles negros<br>
  Útil para separar objetos del fondo

# EJEMPLOS DE USO <br>
# 1. Fusion de imagenes. <br>
# PASOS <br>
  1. Abrir la primera imagen
  2. Presionar el boton "Fusionar imagenes"
  3. Seleccionar la segunda imagen 
<img width="500" height="400" alt="image" src="https://github.com/user-attachments/assets/88017a9d-b6f1-40b3-8e53-2d357c8f00d5" />
  
# 2. Escala de grises. <br>
# PASOS <br>
  1. Abrir la imagen
  2. Presionar el boton "Escala de grises"
<img width="500" height="400" alt="image" src="https://github.com/user-attachments/assets/5afe396c-c581-4fc2-b9a3-c67e1abe2205" />

# 3. Imagen negativa s. <br>
# PASOS <br>
  1. Abrir la imagen
  2. Presionar el boton "Negativo"
<img width="500" height="400" alt="image" src="https://github.com/user-attachments/assets/ac053397-a6d4-4473-9861-eb8b43507324" />

# 4. Rotacion de imagen. <br>
# PASOS <br>
  1. Abrir la imagen
  2. Ajustar el Slider "Rotacion"
<img width="500" height="400" alt="image" src="https://github.com/user-attachments/assets/aea83817-c749-443d-bc7e-2e7cb25263f7" />

# 5. Extraccion de canales. <br>
# PASOS <br>
  1. Abrir la imagen
  2. En la seccion Extraer Canal presionar el boton de acuerdo al color
     Ejemplo: Solo R
<img width="500" height="400" alt="image" src="https://github.com/user-attachments/assets/4e0fbce1-4192-412b-9733-2dc9fe2122e5" />
