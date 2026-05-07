class Funcion:
    def __init__(self, id_f, pelicula, duracion, hora, fecha, sala_id):
        self.id_f = id_f
        self.pelicula = pelicula
        self.duracion = duracion
        self.hora = hora
        self.fecha = fecha
        self.sala_id = sala_id

    def __str__(self):
        return f"{self.id_f}-  {self.pelicula} - {self.hora} - (Sala: {self.sala_id})"