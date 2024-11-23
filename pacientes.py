from conexion import BaseDeDatos

class Paciente:
  def __init__(self, db):
    self.db = db

  def registrar_paciente(self, nombre, apellido, telefono, email, direccion):
    query = "INSERT INTO Pacientes (nombre, apellido, telefono, email, direccion) VALUES (%s, %s, %s, %s, %s)"
    valores = (nombre, apellido, telefono, email, direccion)
    self.db.ejecutar(query, valores)
    return "Paciente registrado con éxito."

  def actualizar_paciente(self, paciente_id, nombre, apellido, telefono, email, direccion):
    query = "UPDATE Pacientes SET nombre=%s, apellido=%s, telefono=%s, email=%s, direccion=%s WHERE paciente_id=%s"
    valores = (nombre, apellido, telefono, email, direccion, paciente_id)
    self.db.ejecutar(query, valores)
    return "Paciente actualizado con éxito."

  def ver_paciente(self, paciente_id):
    query = "SELECT * FROM Pacientes WHERE paciente_id = %s"
    return self.db.obtener_datos(query, (paciente_id,))
      
  def eliminar_paciente(self, paciente_id):
    query = "DELETE FROM Pacientes WHERE paciente_id = %s"
    self.db.ejecutar(query, (paciente_id,))
    return "Paciente eliminado con éxito."

  def ver_pacientes(self):
    query = "SELECT * FROM Pacientes"
    return self.db.obtener_datos(query)
      
  def buscar_paciente_por_nombre(self, nombre, apellido):
    query = "SELECT * FROM Pacientes WHERE (nombre LIKE %s) AND (apellido LIKE %s)"
    valores = (f"%{nombre}%", f"%{apellido}%")
    return self.db.obtener_datos(query, valores)
