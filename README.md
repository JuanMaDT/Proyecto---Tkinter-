# Proyecto---Tkinter-
Aplicación de escritorio desarrollada en Python con interfaz gráfica Tkinter que permite procesar y transformar imágenes digitales aplicando múltiples operaciones de procesamiento de imágenes.
👥 Integrantes

Juan Manuel Diaz Torres
Lina Maria Calvo Castro 

Librerias requeridas: 
pip install numpy
pip install pillow
pip install matplotlib 

FUNCIONES IMPLEMENTADAS 
1. BRILLO 
Ubicación: Slider "Brillo"
Función: Ajusta el brillo de toda la imagen
Rango: 0.5 (oscuro) a 2.0 (muy brillante)
Uso: Desliza el control para ver cambios en tiempo real

2. BRILLO POR CANAL RGB
  Ubicación: Checkboxes R, G, B en "Canales RGB"
  Función: Activa/desactiva canales de color individualmente
  Uso: Desmarca un checkbox para eliminar ese color de la imagen

3. CONTRASTE LOGARITMICO
  Ubicación: Botón "Contraste Log"
  Función: Mejora el contraste en zonas oscuras
  Uso: Útil para realzar detalles en imágenes subexpuestas

4. CONTRASTE EXPONENCIAL
  Ubicación: Botón "Contraste Exp"
  Función: Mejora el contraste en zonas claras
  Uso: Útil para realzar detalles en imágenes sobreexpuestas

5. RECORTE IMAGEN
  Ubicación: Botón "Recortar"
  Función: Recorta un área rectangular de la imagen
  Uso:

  Clic en "Recortar"
  Ingresa X inicial (coordenada horizontal izquierda)
  Ingresa Y inicial (coordenada vertical superior)
  Ingresa X final (coordenada horizontal derecha)
  Ingresa Y final (coordenada vertical inferior)


  Ejemplo: Para recortar el centro de una imagen de 800x600:

  X inicial: 200, Y inicial: 150
  X final: 600, Y final: 450

6. ZOOM
  Ubicación: Slider "Zoom"
  Función: Amplía o reduce la vista desde el centro
  Rango: 0.5 (alejar) a 3.0 (acercar)
  Uso: Valores > 1 hacen zoom in, valores < 1 hacen zoom out

7. ROTACION
  Ubicación: Slider "Rotación (°)"
  Función: Rota la imagen en sentido antihorario
  Rango: -180° a 180°
  Uso: Desliza para rotar en tiempo real

8. VISUALIZACION HISTOGRAMA
  Ubicación: Botón "Ver Histograma"
  Función: Muestra la distribución de intensidades de cada canal RGB
  Uso: Abre una ventana con 3 gráficos (R, G, B)
  Interpretación:

  Picos a la izquierda = imagen oscura
  Picos a la derecha = imagen clara
  Distribución uniforme = buen contraste
   
9. FUSION DE IMAGENES SIMPLE
  Ubicación: Botón "Fusionar"
  Función: Combina dos imágenes mediante promedio
  Uso:

  Carga una imagen principal
  Clic en "Fusionar"
  Selecciona la segunda imagen
  Se crea una mezcla 50/50

10. FUSION DE IMAGENES ECUALIZADAS
  Ubicación: Botón "Fusionar Ecualizadas"
  Función: Ecualiza ambas imágenes antes de fusionarlas
  Uso: Igual que fusión simple, pero mejora el contraste previo
  Ventaja: Mejor resultado en imágenes con diferente iluminación

11. Ubicación: Botones "Solo R", "Solo G", "Solo B"
  Función: Muestra únicamente un canal de color
  Uso:

  "Solo R" → Muestra solo componente rojo
  "Solo G" → Muestra solo componente verde
  "Solo B" → Muestra solo componente azul

12. EXTRACCION DE CAPAS CMYK
  Ubicación: Botones en "Canales CMYK"
  Función: Aplica efectos de color tipo impresión
  Uso:

  Cyan (C): Resalta azul + verde
  Magenta (M): Resalta rojo + azul
  Amarillo (Y): Resalta rojo + verde

13. FOTO NEGATIVA
  Ubicación: Botón "Negativo"
  Función: Invierte todos los colores de la imagen
  Uso: Efecto película negativa (oscuro → claro, claro → oscuro)

14. CONVERSION A ESCALA DE GRISES
  Ubicación: Botón "Escala de Grises"
  Función: Convierte la imagen a blanco y negro
  Método: Promedio de canales RGB
  Uso: Presiona nuevamente para revertir

15. BINARIZACION CON UMBRAL
  Ubicación: Slider "Umbral (0-255)"
  Función: Convierte la imagen a solo blanco y negro puro
  Uso:

  Valores bajos → más pixeles blancos
  Valores altos → más pixeles negros
  Útil para separar objetos del fondo

    #FunciónUbicaciónDescripción1Brillo GlobalSlider "Brillo"Ajusta el brillo de toda la imagen (rango: 0.5 - 2.0)2Brillo por Canal RGBCheckboxes R, G, BActiva/desactiva canales de color individualmente3Contraste LogarítmicoBotón "Contraste Log"Mejora el contraste en zonas oscuras4Contraste ExponencialBotón "Contraste Exp"Mejora el contraste en zonas claras5Recorte de ImagenBotón "Recortar"Recorta un área rectangular mediante coordenadas (x1, y1, x2, y2)6ZoomSlider "Zoom"Amplía o reduce la vista desde el centro (0.5x - 3.0x)7RotaciónSlider "Rotación (°)"Rota la imagen en sentido antihorario (-180° a 180°)8Visualización de HistogramaBotón "Ver Histograma"Muestra la distribución de intensidades por canal RGB9Fusión de ImágenesBotón "Fusionar"Combina dos imágenes mediante promedio (50/50)10Fusión EcualizadasBotón "Fusionar Ecualizadas"Ecualiza ambas imágenes antes de fusionarlas11Extracción RGBBotones "Solo R/G/B"Extrae y muestra cada canal de color por separado12Extracción CMYKBotones "Cyan/Magenta/Amarillo"Aplica efectos de color tipo impresión (C, M, Y)13Foto NegativaBotón "Negativo"Invierte todos los colores de la imagen14Escala de GrisesBotón "Escala de Grises"Convierte la imagen a blanco y negro (promedio RGB)15BinarizaciónSlider "Umbral (0-255)"Convierte la imagen a solo blanco y negro puro
