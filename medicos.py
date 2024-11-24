from conexion import BaseDeDatos

class Medico:
    def __init__(self, db):
        self.db = db

    def registrar_medico(self, nombre, apellido, telefono, especialidad):
        query = "INSERT INTO Medicos (nombre, apellido, telefono, especialidad) VALUES (%s, %s, %s, %s)"
        valores = (nombre, apellido, telefono, especialidad)
        self.db.ejecutar(query, valores)
        return "Médico registrado con éxito."

    def actualizar_medico(self, medico_id, nombre, apellido, telefono, especialidad):
        query = "UPDATE Medicos SET nombre=%s, apellido=%s, telefono=%s, especialidad=%s WHERE medico_id=%s"
        valores = (nombre, apellido, telefono, especialidad, medico_id)
        self.db.ejecutar(query, valores)
        return "Médico actualizado con éxito."

    def ver_medico(self, medico_id):
        query = "SELECT * FROM Medicos WHERE medico_id = %s"
        return self.db.obtener_datos(query, (medico_id,))
        
    def eliminar_medico(self, medico_id):
        query = "DELETE FROM Medicos WHERE medico_id = %s"
        self.db.ejecutar(query, (medico_id,))
        return "Médico eliminado con éxito."

    def ver_medicos(self):
        query = "SELECT * FROM Medicos"
        return self.db.obtener_datos(query)
        
    def buscar_medico_por_nombre(self, nombre, apellido):
        query = "SELECT * FROM Medicos WHERE (nombre LIKE %s) AND (apellido LIKE %s)"
        valores = (f"%{nombre}%", f"%{apellido}%")
        return self.db.obtener_datos(query, valores)
    
    def buscar_medico_por_especialidad(self, nombre, apellido, especialidad):
        query = "SELECT * FROM Medicos WHERE (nombre LIKE %s) AND (apellido LIKE %s) AND (especialidad LIKE %s)"
        valores = (f"%{nombre}%", f"%{apellido}%", f"%{especialidad}%")
        return self.db.obtener_datos(query, valores)