
# Import funciones de otros archivos
import capture_packets 
import analyze_packets

import reports

#create a menu navigation
def menu():
    print("--------------------------------------------")
    print("        Bienvenido al menú                  ")
    print("--------------------------------------------")
    print("1. Capturar paquetes y analizar paquetes")
    print("2. Reporte de capturas")
    print("3. Reporte de IPs")
    print("4. Reporte de análisis de IPs")
    print("5. Salir")
    
    option = int(input("Por favor, seleccione una opción: "))

    return option

#main function
def main():
    
    try:
      option = menu()
    except ValueError:
      print("Introduce un número")
      option = menu()
      
    while option != 5:
        if option == 1:
            time_limit = int(input("Introduce el tiempo de ejecución en segundos: "))

            print("--------------------------------------------")
            print("   Capturando paquetes           ")
            print("--------------------------------------------")
            capture_packets.capture_packets(time_limit)

            print("--------------------------------------------")
            print("   Analizando paquetes capturados           ")
            print("--------------------------------------------")

            capture_packets.analyze_and_save_packets_db()

        elif option == 2:
            print("--------------------------------------------")
            print("   Reporte de capturas           ")
            print("--------------------------------------------")
            
            reports.show_report_captures()

            
        elif option == 3:
            print("--------------------------------------------")
            print("   Reporte de IPs           ")
            print("--------------------------------------------")
            reports.show_reports_ip();

        elif option == 4:
            print("--------------------------------------------")
            print("   Reporte de análisis de IPs           ")
            print("--------------------------------------------")
            reports.show_reports_analysis()
            
        else:
            print("Invalid option")
        option = menu()

    print("Gracias por usar el programa. Hasta pronto!")


if __name__ == "__main__":
    main()
    
    



