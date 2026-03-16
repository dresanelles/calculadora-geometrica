PI = 3.1416


# Triangulo 
# Formula Área = (BASE x ALTURA) / 2
# Formula Perímetro = (Lado 1 + Lado 2 + Lado 3)


def triangulo():
    print("\nHas escogido triangulo.")
    print("¿Qué deseas hallar?")
    print("1. Área")
    print("2. Perímetro")
    print("3. Volver")

    try:
        opcion = int(input("Selección: "))
    except ValueError:
        print("Valor no válido")
        return

    if opcion == 1:
        try:
            base = float(input("Ingresa la base: "))
            altura = float(input("Ingresa la altura: "))
        except ValueError:
            print("Valor no valido")
            return

        area = (base * altura) / 2
        print("El área es:", area)
    
    elif opcion == 2:
        try:
            lado1 = float(input("Ingresa el lado 1: "))
            lado2 = float(input("Ingresa el lado 2: "))
            lado3 = float(input("Ingresa el lado 3: "))
        except ValueError:
            print("Valor no valido")
            return
        
        perimetro = lado1 + lado2 + lado3
        print("El perímetro del triángulo es:", perimetro)
    
    elif opcion == 3:
        return

    else:
        print("Selección inválida")

#("------------------------------------------------")


# Rectángulo 

# Formula Área = BASE x ALTURA
# Formula Perímetro = 2 * (BASE + ALTURA)


def rectangulo():
    print("\nHas escogido rectangulo.")
    print("¿Qué deseas hallar?")
    print("1. Área")
    print("2. Perímetro")
    print("3. Volver")

    try:
        opcion = int(input("Selección: "))
    except ValueError:
        print("Valor no válido")
        return
    


    if opcion == 1:
        try:
            base = float(input("Ingresa la base: "))
            altura = float(input("Ingresa la altura: "))
        except ValueError:
            print("Valor no valido")
            return

        area = (base * altura)
        print("El área es:", area)
    
    elif opcion == 2:
        try:
            base = float(input("Ingresa la base: "))
            altura = float(input("Ingresa la altura: "))
        except ValueError:
            print("Valor no valido")
            return
        
        perimetro = (2 * base) + (2*altura)
        print("El perímetro del rectángulo es:", perimetro)
    
    elif opcion == 3: 
        return

    else:
        print("Selección inválida")


#("------------------------------------------------")


# Circulo

# Formula Área = PI * Radio^2
# Formula Perímetro = 2 × PI × Radio


def circulo():
    print("\nHas escogido Circulo.")
    print("¿Qué deseas hallar?")
    print("1. Área")
    print("2. Perímetro")
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
        if radio <= 0:
            print("Error, el número debe ser mayor que 0")
            return
            

        area = PI * (radio**2) 
        print("El área es:", area)
    
    elif opcion == 2:
        try:
            radio = float(input("Ingresa el radio: "))
        except ValueError:
            print("Valor no válido")
            return


        perimetro = 2 * PI * radio
        print("El perímetro del circulo es:", perimetro)
    
    elif opcion == 3: 
        return

    else:
        print("Selección inválida")


#("------------------------------------------------")


# Pentagono ( 5 lados iguales )

# Formula Área = (perimetro x apotema) / 2
# Formula Perímetro = 5 x lado

# Apotema: linea que va desde el centro del poligono hasta la mitad de uno de sus lados y es perpendicular al lado

#         /\ 
#        /  \
#       /    \
#      /      \
#     /   |    \
#    /    |a    \
#   /_____|_____ \


def pentagono():
    print("\nHas escogido Pentagono.")
    print("¿Qué deseas hallar?")
    print("1. Área")
    print("2. Perímetro")
    print("3. Volver")

    try:
        opcion = int(input("Selección: "))
    except ValueError:
        print("Valor no válido")
        return

    if opcion == 1:
        try:
            lado = float(input("Ingresa el lado: "))
            apotema = float(input("Ingresa el apotema: "))
        except ValueError:
            print("Valor no valido")
            return
        
        perimetro = 5 * lado
        area = (perimetro * apotema) / 2
        print("El área es:", area)
    
    elif opcion == 2:
        try:
            lado = float(input("Ingresa el lado: "))   
            perimetro = 5 * lado
        except ValueError:
            print("Valor no valido")
            return
        
        print("El perímetro del pentagono es:", perimetro)
    
    elif opcion == 3:
        return

    else:
        print("Selección inválida")


#("------------------------------------------------")


# Triangulo Rectángulo
# Formula Área = (cateto a * cateto b) / 2
# Formula Perimetro = cateto a + cateto b + hipotenusa
# Formula Hipotenusa = (cateto a**2 + cateto b**2) ** (1/2)

# Cateto: lados que forman el angulo de 90°
# Hipotenusa: Lado más largo del triangulo

def triangulo_rectangulo():
    print("\nHas escogido Triángulo Rectángulo.")
    print("¿Qué deseas hallar?")
    print("1. Área")
    print("2. Perímetro")
    print("3. Ángulos")
    print("4. Volver")

    try:
        opcion = int(input("Selección: "))
    except ValueError:
        print("Valor no válido")
        return

    if opcion == 1:
        try:
            cateto1 = float(input("Ingresa el cateto 1: "))
            cateto2 = float(input("Ingresa el cateto 2: "))
        except ValueError:
            print("Valor no valido")
            return

        area = (cateto1 * cateto2) / 2
        print("El área es:", area)

    elif opcion == 2:

        print("¿Conoces la hipotenusa?")
        print("1. Sí")
        print("2. No")

        try:
            conoce = int(input("Selección: "))
        except ValueError:
            print("Valor no valido")
            return

        if conoce == 1:
            try:
                cateto1 = float(input("Ingresa el cateto 1: "))
                cateto2 = float(input("Ingresa el cateto 2: "))
                hipotenusa = float(input("Ingresa la hipotenusa: "))
            except ValueError:
                print("Valor no valido")
                return
            
        elif conoce == 2:
            try:
                cateto1 = float(input("Ingresa el cateto 1: "))
                cateto2 = float(input("Ingresa el cateto 2: "))
            except ValueError:
                print("Valor no valido")
                return

            hipotenusa = (cateto1**2 + cateto2**2) ** (1/2)
            print("La hipotenusa calculada es:", hipotenusa)

        perimetro = cateto1 + cateto2 + hipotenusa
        print("El perímetro es:", perimetro)
    
    elif opcion == 3:

        angulo = float(input("Ingresa un ángulo agudo (<90°): "))

        if angulo <= 0 or angulo >= 90:
            print("Ángulo invalido")
        else:
            otro_angulo = 90 -  angulo

            print("Angulo recto: ", str(90),"°")
            print("Angulo ingresado: ", angulo,"°")
            print("Angulo faltante: ", otro_angulo,"°")
            
    
    elif opcion == 4:
        return

    else:
        print("Selección inválida")

    



    






