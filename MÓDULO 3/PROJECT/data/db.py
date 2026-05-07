import sqlite3

dbbase = ("cinex.db")

def get_connection():
   try:
       conexion = sqlite3.connect(dbbase)
       return conexion
   except sqlite3.Error as problem:
       return f"Error: {problem} : ARCHIVO NO ENCONTRADO"
   