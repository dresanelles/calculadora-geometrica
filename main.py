
from figuras2d import triangulo, rectangulo, circulo, pentagono, triangulo_rectangulo
from figuras3d import cubo, piramide, esfera, cono

# ----------------------------
# Función menú 2D
# ----------------------------
def menu_2d():
    eleccion2d = 0
    while eleccion2d != 6:
        print("\n------ FIGURAS 2D ------")
        print("1. Triángulo")
        print("2. Rectángulo")
        print("3. Círculo")
        print("4. Pentágono")
        print("5. Triángulo Rectángulo")
        print("6. Volver")

        try:
            eleccion2d = int(input("Selecciona una figura 2D: "))
        except ValueError:
            print("Valor no válido")
            continue

        if eleccion2d == 1:
            triangulo()
        elif eleccion2d == 2:
            rectangulo()
        elif eleccion2d == 3:
            circulo()
        elif eleccion2d == 4:
            pentagono()
        elif eleccion2d == 5:
            triangulo_rectangulo()
        elif eleccion2d == 6:
            return
        else:
            print("Selección inválida")

# ----------------------------
# Función menú 3D
# ----------------------------
def menu_3d():
    eleccion3d = 0
    while eleccion3d != 5:
        print("\n------ FIGURAS 3D ------")
        print("1. Cubo")
        print("2. Pirámide")
        print("3. Esfera")
        print("4. Cono")
        print("5. Volver")

        try:
            eleccion3d = int(input("Selecciona una figura 3D: "))
        except ValueError:
            print("Valor no válido")
            continue

        if eleccion3d == 1:
            cubo()
        elif eleccion3d == 2:
            piramide()
        elif eleccion3d == 3:
            esfera()
        elif eleccion3d == 4:
            cono()
        elif eleccion3d == 5:
            return
        else:
            print("Selección inválida")

# ----------------------------
# Bucle principal
# ----------------------------
opcion = 0
while opcion != 3:
    print("\n------🧮 CALCULADORA GEOMÉTRICA 🧮------\n")

    print("Qué tipo de figura quieres hallar?\n")

    print("1. Figuras 2D")
    print("2. Figuras 3D")
    print("3. Salir")

    try:
        opcion = int(input("Selecciona una opción: "))
    except ValueError:
        print("Valor no válido")
        continue

    if opcion == 1:
        menu_2d()
    elif opcion == 2:
        menu_3d()
    elif opcion == 3:
        print("Saliendo de la calculadora...")
    else:
        print("Selección inválida")