from services.servicio_taquilla import obtener_salas, vender_boleto, obtener_datos_cine, listar_cartelera
import time


def app():
    cine = obtener_datos_cine()
    while True:
        print("Bienvenido a CINEX, tu desconex :D")
        print("1. Ver Salas y Disponibilidad")
        print("2. Vender entradas")
        print("3. Contexto del cine")
        print("4 .Ver Caartelera de hoy")
        print("5. Disponibilidad Cajeros en Sede")
        print("6. Salir")

        opcion = input("Elije we: ")

        if opcion == "1":
            for s in obtener_salas():
                print(s)
            

        elif opcion == "2":
          try:
            costo = 5
            print(f"El precio es {costo}")

            print()
            print()
            print()

            time.sleep(4)
            print()
            print()

            time.sleep(3)
            precio = int(input("Coloque el precio ubicado en la entrada: "))
            s_id = int(input("ID SALA:"))
            cant = (int(input("Cantidad;")))

            total = cant * precio

            pago = int(input("ingrese la cantidad a pagar:"))

            print(f"el total es: {total}")

            if pago < total:
                print("Saldo insuficiente")
                break
            else:
                resultado = vender_boleto(s_id, cant)
                print(f"Resultado: {resultado}")
                print()
                print()
                time.sleep(10)
                print("Venta culminada")
                break
          except ValueError:
              print("Error, ingrese números nojoda")


        elif opcion == "3":
            print("Resumen del CINE:")
            if cine: 
                print(f"Sede: {cine.direccion}")
                print(f"Horario: {cine.horario}")
                print(f"Estado: Operativo")
            else:
                print("No hay datos de sede we")

        elif opcion == "4":
            try:
                cartelera = listar_cartelera()   
                for peli in cartelera:
                    print(f" {peli}")
            except:
                print("No carga ni madres")

        elif opcion == "5":
            print("CAJEROS A TRATAR")
            if cine:
                print(f"Taquilla: {cine.direccion}")
                print(f"Horario de atención:{cine.horario}")
                print("Cajeros activos: 3 (Sede Principal)")
            break
            
        
        elif opcion == "6":
            print("Chau we")
            break

      

        else:
            print("Opcion no válida")

        
if __name__ == "__main__":
    app()