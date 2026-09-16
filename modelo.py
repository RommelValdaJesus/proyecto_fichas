class Modelo:


    def agregar_paciente(self, nombre, doctor, area, fecha):
        self.cursor.execute("INSERT INTO pacientes (nombre, doctor, area, fecha) VALUES (?, ?, ?, ?)",
                            (nombre, doctor, area, fecha))
        self.conexion.commit()

    def obtener_pacientes(self):
        self.cursor.execute("SELECT * FROM pacientes")
        return self.cursor.fetchall()

    def eliminar_paciente(self, id_paciente):
        self.cursor.execute("DELETE FROM pacientes WHERE id=?", (id_paciente,))
        self.conexion.commit()
