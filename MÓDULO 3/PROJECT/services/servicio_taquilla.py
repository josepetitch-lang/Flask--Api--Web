from data.db import get_connection
from models.salas import Sala
from models.taquillas import Taquilla
from models.funciones import Funcion
import sqlite3


def obtener_salas():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Sala")
    filas = cursor.fetchall()
                   
    print(f"El tipo de filas es {type(filas)}")

    lista_salas = []
    for f in filas:
        nueva_sala = Sala(f[0], f[1], f[2], f[3])
        lista_salas.append(nueva_sala)

    conn.close()
    return lista_salas


def obtener_datos_cine():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Taquilla LIMIT 1")
        f = cursor.fetchone()
        conn.close()

        if f:
           return Taquilla(f[0], f[1], f[2], f[3])
    except sqlite3.Error as e:
        return f"{e}: Srchivo no encontrado"

    
def resumen_salas():
    try:
      conn = get_connection()
      cursor = conn.cursor()
      cursor.execute = ("Select COUNT(*) FROM Sala WHERE Disponibilidad > 0")
      nosequeponer = cursor.fetchone()[0]
      conn.close()

      if nosequeponer > 0:
        return f"OJO, Tienes {nosequeponer} TOTALMENTE LLENOS, ESTÁ MAS LLENO QUE... que... el tanque de mi casa (lol)"
      else:
        return f"Todas tienen disponibilidad xd"
    except sqlite3.Error:
        return None
    

def listar_cartelera():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Funciones")
    filas = cursor.fetchall()
    conn.close

    cartelera = []

    for f in filas:
       cartelera.append(f"Título: {f[1]}, Hora: {f[2]}")
       
    return cartelera
    
def vender_boleto(id_s, niidea):
    try:
        conn = get_connection()
        cursor = conn.cursor()
    
        cursor.execute("SELECT Disponibilidad FROM Sala WHERE ID_SALA = ?", (id_s,))
        fila = cursor.fetchone() # Usamos fetchone() que es más directo que fetchall()
        
        if fila:
            disp_actual = fila[0]
            
            if disp_actual >= niidea:
                
                sql = "UPDATE Sala SET Disponibilidad = Disponibilidad - ? WHERE ID_SALA = ?"
                cursor.execute(sql, (niidea, id_s))
                
                conn.commit()
                conn.close()
                return "Vendido" 
            else:
                conn.close()
                return "No hay suficientes boletos"
        
        conn.close()
        return "Sala no encontrada"
        
    except Exception as e:
        return f"Error en la base de datos: {e}"