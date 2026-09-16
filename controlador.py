from modelo import Modelo

class Controlador:
    def __init__(self, vista):
        self.vista = vista
        self.modelo = Modelo()
        self.actualizar_tabla()

    def asignar_ficha(self):
        nombre = self.vista.nombre.get()
        doctor = self.vista.doctor.get()
        area = self.vista.area.get()
        fecha = self.vista.fecha.get()
        self.modelo.agregar_paciente(nombre, doctor, area, fecha)
        self.actualizar_tabla()

    def actualizar_tabla(self):
        for row in self.vista.tabla.get_children():
            self.vista.tabla.delete(row)
        for paciente in self.modelo.obtener_pacientes():
            self.vista.tabla.insert("", "end", values=paciente)
