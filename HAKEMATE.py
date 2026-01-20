import tkinter as tk
from tkinter import simpledialog, messagebox

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saluda(self):
        return f"Soy {self.nombre} y tengo {self.edad} años."

# Crear ventana oculta para diálogos
root = tk.Tk()
root.withdraw()  # Ocultar ventana principal

# Pedir nombre y edad en ventanas emergentes
nombre = simpledialog.askstring("Entrada", "¿Cuál es tu nombre?")
if nombre is None:
    root.destroy()
    exit()

edad = simpledialog.askstring("Entrada", "¿Cuál es tu edad?")
if edad is None:
    root.destroy()
    exit()

# Crear objeto y mostrar mensaje en ventana
persona = Persona(nombre, edad)
messagebox.showinfo("Resultado", persona.saluda())

root.destroy()
    