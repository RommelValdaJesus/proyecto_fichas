import tkinter as tk
from tkinter import ttk

class Vista:
    def __init__(self, root, controlador):
        self.root = root
        self.controlador = controlador
        self.root.title("Sistema de Fichas Clínicas")
        self.root.geometry("700x400")

        # Campos
        tk.Label(root, text="Paciente:").grid(row=0, column=0)
        self.nombre = tk.Entry(root)
        self.nombre.grid(row=0, column=1)

        tk.Label(root, text="Doctor:").grid(row=1, column=0)
        self.doctor = tk.Entry(root)
        self.doctor.grid(row=1, column=1)

        tk.Label(root, text="Área:").grid(row=2, column=0)
        self.area = ttk.Combobox(root, values=["Pediatría", "Cardiología", "Emergencias"])
        self.area.grid(row=2, column=1)

        tk.Label(root, text="Fecha:").grid(row=3, column=0)
        self.fecha = tk.Entry(root)
        self.fecha.grid(row=3, column=1)

        self.boton_asignar = tk.Button(root, text="Asignar Ficha")
        self.boton_asignar.grid(row=4, column=1)

       

        # Tabla
        self.tabla = ttk.Treeview(root, columns=("ID", "Nombre", "Doctor", "Área", "Fecha"), show="headings")
        for col in ("ID", "Nombre", "Doctor", "Área", "Fecha"):
            self.tabla.heading(col, text=col)
        self.tabla.grid(row=5, column=0, columnspan=4)
