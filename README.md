# Proyecto---Tkinter-
Aplicación de escritorio desarrollada en Python con interfaz gráfica Tkinter que permite procesar y transformar imágenes digitales aplicando múltiples operaciones de procesamiento de imágenes.
👥 Integrantes

Juan Manuel Diaz Torres
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

# 11. Ubicación: Botones "Solo R", "Solo G", "Solo B"
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

   
