PI = 3.1416

# Cubo
# Volumen = lado^3
# Área superficial = 6 * lado^2 (es la suma de las áreas de todas sus caras.)

def cubo():
    print("\nHas escogido Cubo.")
    print("¿Qué deseas hallar?")
    print("1. Volumen")
    print("2. Área superficial")
    print("3. Volver")

    try:
        opcion = int(input("Selección: "))
    except ValueError:
        print("Valor no válido")
        return

    if opcion == 1:
        try:
            lado = float(input("Ingresa el lado del cubo: "))
        except ValueError:
            print("Valor no válido")
            return
        volumen = lado ** 3
        print("El volumen del cubo es:", volumen)
    
    elif opcion == 2:
        try:
            lado = float(input("Ingresa el lado del cubo: "))
        except ValueError:
            print("Valor no válido")
            return
        area = 6 * (lado ** 2)
        print("El área superficial del cubo es:", area)
    
    elif opcion == 3:
        return
    else:
        print("Selección inválida")


# Pirámide cuadrada (la base es un cuadrado)
# Volumen = (base^2 * altura) / 3
# Área superficial = base^2 + 2*base*altura_apotema


def piramide():
    print("\nHas escogido Pirámide cuadrada.")
    print("¿Qué deseas hallar?")
    print("1. Volumen")
    print("2. Área superficial")
    print("3. Volver")

    try:
        opcion = int(input("Selección: "))
    except ValueError:
        print("Valor no válido")
        return

    if opcion == 1:
        try:
            base = float(input("Ingresa la longitud de la base: "))
            altura = float(input("Ingresa la altura de la pirámide: "))
        except ValueError:
            print("Valor no válido")
            return
        volumen = (base ** 2 * altura) / 3
        print("El volumen de la pirámide es:", volumen)
    
    elif opcion == 2:
        try:
            base = float(input("Ingresa la longitud de la base: "))
            altura_apotema = float(input("Ingresa la altura lateral (apotema): "))
        except ValueError:
            print("Valor no válido")
            return
        area = (base ** 2) + (2 * base * altura_apotema)
        print("El área superficial de la pirámide es:", area)
    
    elif opcion == 3:
        return
    else:
        print("Selección inválida")


# Esfera
# Volumen = (4/3) * PI * radio^3
# Área superficial = 4 * PI * radio^2


def esfera():
    print("\nHas escogido Esfera.")
    print("¿Qué deseas hallar?")
    print("1. Volumen")
    print("2. Área superficial")
    print("3. Volver")

    try:
        opcion = int(input("Selección: "))
    except ValueError:
        print("Valor no válido")
        return

    if opcion == 1:
        try:
            radio = float(input("Ingresa el radio: "))
        except ValueError:
            print("Valor no válido")
            return
        volumen = (4/3) * PI * (radio ** 3)
        print("El volumen de la esfera es:", volumen)
    
    elif opcion == 2:
        try:
            radio = float(input("Ingresa el radio: "))
        except ValueError:
            print("Valor no válido")
            return
        area = 4 * PI * (radio ** 2)
        print("El área superficial de la esfera es:", area)
    
    elif opcion == 3:
        return
    else:
        print("Selección inválida")


# Cono
# Volumen = (1/3) * PI * radio^2 * altura
# Área superficial = PI * radio * (radio + generatriz)
# Generatriz = (radio^2 + altura^2) ** (1/2) -> (es la distancia inclinada desde la base hasta el vértice, es decir, el lado “inclinado” que une el centro de la base con la punta del cono.)


def cono():
    print("\nHas escogido Cono.")
    print("¿Qué deseas hallar?")
    print("1. Volumen")
    print("2. Área superficial")
    print("3. Volver")

    try:
        opcion = int(input("Selección: "))
    except ValueError:
        print("Valor no válido")
        return

    if opcion == 1:
        try:
            radio = float(input("Ingresa el radio: "))
            altura = float(input("Ingresa la altura: "))
        except ValueError:
            print("Valor no válido")
            return
        volumen = (1/3) * PI * (radio ** 2) * altura
        print("El volumen del cono es:", volumen)
    
    elif opcion == 2:
        try:
            radio = float(input("Ingresa el radio: "))
            altura = float(input("Ingresa la altura: "))
        except ValueError:
            print("Valor no válido")
            return
        generatriz = (radio ** 2 + altura ** 2) ** (1/2)
        area = PI * radio * (radio + generatriz)
        print("El área superficial del cono es:", area)
    
    elif opcion == 3:
        return
    else:
        print("Selección inválida")