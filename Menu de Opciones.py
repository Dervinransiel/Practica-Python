# Menu de Opciones

opcion = 0 
nombre = input("Escribe alguna opcion:")

while opcion != 2:
    print("1. saludo")
    print("2. Despidase")

    opcion = int(input("Ingrese una opcion:"))
    if opcion == 1:
        print("Hola "+nombre)
print("Adios")