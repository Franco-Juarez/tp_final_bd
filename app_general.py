import tkinter as tk
from tkinter import ttk
from tkinter.font import Font
import subprocess

##############################################################CHATGP
# Funciones para abrir las aplicaciones independientes
def abrir_app_pacientes():
    subprocess.Popen(["python", "app_pacientes.py"])

def abrir_app_medicos():
    subprocess.Popen(["python", "app_medicos.py"])

def abrir_app_turnos():
    subprocess.Popen(["python", "app_turnos.py"])

# Ventana principal
root = tk.Tk()
root.title("Manejador Principal")
root.geometry("400x300")

# Fuente personalizada para los botones
font = Font(family="Arial", size=12)

style = ttk.Style()
style.configure("Custom.TButton", font=font, padding=10)

# Botones principales
ttk.Button(root, text="Pacientes", command=abrir_app_pacientes, style="Custom.TButton").pack(pady=20, fill="x", padx=50)
ttk.Button(root, text="Médicos", command=abrir_app_medicos, style="Custom.TButton").pack(pady=20, fill="x", padx=50)
ttk.Button(root, text="Turnos", command=abrir_app_turnos, style="Custom.TButton").pack(pady=20, fill="x", padx=50)

root.mainloop()