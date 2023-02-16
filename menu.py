
# Import funciones de otros archivos
import capture_packets 
import analyze_packets





#create a menu navigation
def menu():
    print("--------------------------------------------")
    print("Welcome to the menu")
    print("1. Capturar paquetes y analizar paquetes")
    print("2. Analizar paquetes")
    print("3. Resultados")
    print("4. Salir")
    
    print("Por favor, seleccione una opción: ")
    option = int(input())
    return option

#main function
def main():
    
    try:
      option = menu()
    except ValueError:
      print("Introduce un número")
      option = menu()
      
    while option != 11:
        if option == 1:
            print("You have selected option 1")
            time_limit = int(input("Introduce el tiempo de ejecución en segundos: "))
            capture_packets.capture_packets(time_limit)
            analyze_packets.analyze()

        elif option == 2:
            print("You have selected option 2")
            analyze_packets.analyze()
        elif option == 3:
            print("You have selected option 3")
        elif option == 4:
            print("You have selected option 4")
        else:
            print("Invalid option")
        option = menu()

    print("Thank you for using the menu")


if __name__ == "__main__":
    main()
    
    



