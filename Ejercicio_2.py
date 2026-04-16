# Ejercicio 2  — “Acceso al Campus y Menú Seguro” 
# Objetivo: Login con intentos + menú de acciones con validación estricta. 
# Requisitos 
# 1. Definir credenciales fijas en el código: 
# o usuario correcto: "alumno" 
# o clave correcta: "python123" 

usuario_correcto = "alumno"
clave_correcta = "python123"

# 2. Permitir máximo 3 intentos para ingresar usuario y clave. 

intentos=0
acceso="ok"
for i in range (1,4):
    usuario = input(f"Intento {i}/3 - Usuario: ")
    clave = input("Clave: ")
    if usuario != usuario_correcto  or clave != clave_correcta:
        print("Error: Credenciales Invalidas")
    else:
        break
    intentos+=1

    # 3. Si falla 3 veces: mostrar “Cuenta bloqueada” y terminar. 
    if intentos == 3:
        print("Cuenta bloqueada")
        acceso= "bloqueado"

if acceso =="ok":
# 4. Si ingresa bien: mostrar un menú repetitivo (usar while) hasta elegir salir: 

    opcion =  input("""Menú:
                    
        1. Ver estado de inscripción
        2. Cambiar clave
        3. Mostrar mensaje motivacional
        4. Salir
        
    Ingrese su opción: """)

    while not opcion.isdigit(): 
        opcion = input("Elija una opción válida: ")

    while int(opcion) <= 0 or int(opcion) >4: 
        opcion = input("Opción fuera de rango: ")

    while opcion != "4":

        # 1. Ver estado de inscripción (mostrar “Inscripto”) 
        if opcion == "1":
            print("Inscripto")
        
        # 2. Cambiar clave (pedir nueva clave y confirmación; deben coincidir) 
        # La nueva clave debe tener mínimo 6 caracteres (validar con len()), si no, rechazar. 

        elif opcion == "2":
            nueva_clave=input("Nueva clave: ")
            while len(nueva_clave)<6:
                nueva_clave= input("Error: mínimo 6 caracteres. Nueva clave:")
            confirmacion = input("Confirmación: ")
            while nueva_clave != confirmacion:
                confirmacion=input("Error: las contraseñas no coinciden. Ingrese confiramción nuevamente:")
            print("Su clave ha sido modificada con éxito")

        # 3. Mostrar mensaje motivacional (1 frase):

        elif opcion == "3":
            print ("El esfuerzo que pones hoy será tu orgullo mañana.")
        
        opcion =  input("""Menú:
                    
        1. Ver estado de inscripción
        2. Cambiar clave
        3. Mostrar mensaje motivacional
        4. Salir

        
    Ingrese su opción: """)
        
        # 5. Validación del menú: 
        # Debe ser número (.isdigit()) 
        # Debe estar entre 1 y 4 
        while not opcion.isdigit() or opcion not in "1234": 
            opcion = input("Elija una opción válida: ")

    # 4. Salir 

    print("Hasta Luego")

