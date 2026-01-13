import cv2
import numpy as np

class Cuadrado:
    """Clase que controla un cuadrado que se mueve arriba y abajo"""
    def __init__(self, x, y, tamaño, velocidad):
        self.x = x
        self.y = y
        self.tamaño = tamaño
        self.velocidad = velocidad
        self.direccion = 1  # 1 para abajo, -1 para arriba
    
    def actualizar(self, alto_ventana):
        """Actualiza la posición del cuadrado"""
        self.y += self.velocidad * self.direccion
        
        # Rebota en los bordes
        if self.y + self.tamaño >= alto_ventana:
            self.y = alto_ventana - self.tamaño
            self.direccion = -1
        elif self.y <= 0:
            self.y = 0
            self.direccion = 1
    
    def dibujar(self, frame):
        """Dibuja el cuadrado en el frame"""
        cv2.rectangle(frame, 
                     (self.x, self.y),
                     (self.x + self.tamaño, self.y + self.tamaño),
                     (0, 255, 0), -1)  # Verde relleno

# Crear ventana
ventana = np.ones((400, 600, 3), dtype=np.uint8) * 255  # Ventana blanca
cuadrado = Cuadrado(x=250, y=100, tamaño=50, velocidad=5)

# Bucle principal
print("Presiona 'q' para salir")
while True:
    ventana[:] = 255  # Limpiar ventana (ponerla blanca)
    cuadrado.actualizar(ventana.shape[0])
    cuadrado.dibujar(ventana)
    
    cv2.imshow("Cuadrado Movible", ventana)
    
    # Presionar 'q' para salir
    if cv2.waitKey(50) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows() 