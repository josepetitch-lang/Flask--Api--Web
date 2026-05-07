from models.taquillas import Taquilla

class Sala:
    def __init__(self, id_sala, filas, número, disponibilidad):
        self.id_sala = id_sala
        self.filas = filas
        self.número = número
        self.disponibilidad = disponibilidad

    def __str__(self):
        return f"Sala : {self.número}, Disp: {self.disponibilidad}, Filas: {self.filas}"
       

    def tiene_capacidad(self,cantidad):
        return self.disponibilidad > cantidad
    
    def actualizar_asientos(self, cantidad):
        if self.tiene_capacidad:
            self.disponibilidad -= cantidad
            return True
        else:
            return False
        
    def disponibles(self):
            if self.disponibilidad == 0:
                return f"Sala {self.número}, AGOTADA"
            else:
                return f"Sala {self.número}, Asientos Disponibles: {self.disponibilidad}"
        
        
    

