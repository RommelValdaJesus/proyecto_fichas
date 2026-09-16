import sqlite3
class Modelo:
    def __init__(self):
        self.conexion = sqlite3.connect("clinica.db")
        self.cursor = self.conexion.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS pacientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT,
                doctor TEXT,
                area TEXT,
                fecha TEXT
            )
        """)
        self.conexion.commit()

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
