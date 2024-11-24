from conexion import BaseDeDatos

class Turno:
    def __init__(self, db):
        self.db = db

    def registrar_turno(self, id_paciente, id_medico, fecha, hora):
        query = "INSERT INTO Turnos (id_paciente, id_medico, fecha, hora) VALUES (%s, %s, %s, %s)"
        valores = (id_paciente, id_medico, fecha, hora)
        self.db.ejecutar(query, valores)
        return "Turno programado con éxito."

    def actualizar_turno(self, id_turno, nueva_fecha, nueva_hora):
        query = "UPDATE Turnos SET fecha = %s, hora = %s WHERE id_turno = %s"
        valores = (nueva_fecha, nueva_hora, id_turno)
        self.db.ejecutar(query, valores)
        return "Turno actualizado con éxito."

    def cancelar_turno(self, id_turno):
        query = "DELETE FROM Turnos WHERE id_turno = %s"
        self.db.ejecutar(query, (id_turno,))
        return "Turno cancelado con éxito."
    
#################################################CHATGPT
    def cancelar_turnos_por_medico_y_fecha(self, id_medico, fecha_inicio, fecha_fin):
        query = "DELETE FROM Turnos WHERE id_medico = %s AND fecha BETWEEN %s AND %s"
        valores = (id_medico, fecha_inicio, fecha_fin)
        self.db.ejecutar(query, valores)
        return f"Turnos cancelados para el médico {id_medico} entre {fecha_inicio} y {fecha_fin}."

    def ver_turno(self, id_turno):
        query = "SELECT * FROM Turnos WHERE id_turno = %s"
        return self.db.obtener_datos(query, (id_turno,))

    def ver_turnos(self):
        query = "SELECT t.id_turno, p.nombre AS paciente, m.nombre AS medico, t.fecha, t.hora FROM Turnos t INNER JOIN Pacientes p ON t.id_paciente = p.paciente_id INNER JOIN Medicos m ON t.id_medico = m.medico_id"
        return self.db.obtener_datos(query)

    def buscar_turnos_por_fecha(self, fecha_inicio, fecha_fin):
        query = "SELECT t.id_turno, p.nombre AS paciente, m.nombre AS medico, t.fecha, t.hora FROM Turnos t INNER JOIN Pacientes p ON t.id_paciente = p.paciente_id INNER JOIN Medicos m ON t.id_medico = m.medico_id WHERE t.fecha BETWEEN %s AND %s ORDER BY t.fecha, t.hora"
        valores = (fecha_inicio, fecha_fin)
        return self.db.obtener_datos(query)

    def reporte_medicos_con_mas_turnos(self):
        query = "SELECT m.nombre, m.apellido, COUNT(t.id_turno) AS total_turnos FROM Turnos t INNER JOIN Medicos m ON t.id_medico = m.medico_id GROUP BY m.medico_id ORDER BY total_turnos DESC LIMIT 3"
        return self.db.obtener_datos(query)    