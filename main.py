import tkinter as tk
from vista import Vista
from controlador import Controlador

if __name__ == "__main__":
    root = tk.Tk()
    # Primero se crea la vista
    vista = Vista(root, None)
    # Luego se crea el controlador con la vista ya existente
    controlador = Controlador(vista)
    # Se asigna el controlador a la vista
    vista.controlador = controlador
    root.mainloop()
