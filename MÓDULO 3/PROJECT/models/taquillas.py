from models.usuarios import Usuarios
from data.db import get_connection

class Taquilla:
      def __init__(self, id_usuario, direccion, horario, película,  id_funcion = None):
            self.id_usuario = id_usuario
            self.direccion = direccion
            self.horario = horario
            self.pelicula = película
            self.id_funcion = id_funcion

      def __str__(self):
            return f"Sede: {self.direccion}, Horario: {self.horario}"
      
      def resumen_borrador():
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT Count(*) FROM Sala")
            total_salas = cursor.fetchone()[0]
            conn.close()
            return f"Sede activada con {total_salas} disponible coño"
      
     