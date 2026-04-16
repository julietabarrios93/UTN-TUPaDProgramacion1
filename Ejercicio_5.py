# Ejercicio 5  — “Escape Room:"La Arena del 
# Gladiador"  
# 1. Descripción del Escenario  
# Vas a desarrollar un simulador de batalla por turnos en Python. El programa enfrentará a un 
# usuario (Gladiador) contra un oponente controlado por la computadora (Enemigo). El 
# objetivo es reducir los puntos de vida del oponente a cero antes de que él lo haga contigo.  
# Este ejercicio evalúa el uso de variables (int, float, string, boolean), estructuras de 
# control (if/elif/else), ciclos (while y for) y validación de datos estricta.  
# 2. Requerimientos Técnicos  
# A. Tipos de Datos  
# Debes utilizar obligatoriamente los siguientes tipos de datos para las variables del juego:  
# • • String: Para el nombre del jugador.  
# • • Int: Para los Puntos de Vida (HP) y cantidad de pociones.  
# • • Float: Para el cálculo del daño (ej: un golpe crítico multiplica el ataque por 1.5).  
# • • Boolean: Para controlar si el juego sigue activo o quién tiene el turno.  
# B. Reglas de Validación (¡Importante!)  
# • • No está permitido usar bloques try / except.  
# • • Para validar texto, debes usar el método .isalpha() dentro de un ciclo while.  
# • • Para validar números, debes usar el método .isdigit() dentro de un ciclo 
# while.  

print("--- BIENVENIDO A LA ARENA ---")
# 3. Flujo del Programa  
# Paso 1: Configuración del Personaje  
# El programa inicia pidiendo el nombre del Gladiador.  
gladiador = input("Nombre del gladiador: ")

# • • Validación: El nombre solo puede contener letras. Si el usuario ingresa números, 
# símbolos o lo deja vacío, el programa debe decir "Error: Solo se permiten letras" y volver a 
# preguntar hasta que sea válido.

while gladiador == "" or not gladiador.isalpha(): 
    gladiador = input("Error: Solo se permiten letras. Ingrese nombre de gladiador válido: ")

# Paso 2: Inicialización de Estadísticas  
# El programa debe definir las variables iniciales (sin preguntar al usuario):  
# • • Vida del Gladiador: 100 (int)  
# • • Vida del Enemigo: 100 (int)  
# • • Pociones de Vida: 3 (int)  
# • • Daño base "Ataque Pesado": 15 (int)  
# • • Daño base del enemigo: 12 (int)  
# • • Turno Gladiador : True (booleano)  

vida_gladiador = 100
vida_enemigo = 100
pociones_vida = 3
dano_ataque_pesado = 15 #daño
dano_base_enemigo = 12 #daño
turno_gladiador = True

# Paso 3: El Ciclo de Combate  
# El juego entra en un ciclo que se repite mientras ambos combatientes tengan más de 0 
# puntos de vida.  



while vida_gladiador > 0 and vida_enemigo > 0:

    # Turno del Jugador:  
    # Muestra la vida actual de ambos y las pociones restantes. Luego, ofrece un menú con 3 
    # opciones:  
    # 1. Ataque Pesado  
    # 2. Ráfaga Veloz (Requiere uso de for)  
    # 3. Curar  

    opcion = input(f"""Vida del Gladiador: {vida_gladiador} puntos
Vida del Enemigo: {vida_enemigo}
Pociones restantes {pociones_vida}

 Menú:
                
    1. Ataque pesado
    2. Ráfaga Veloz
    3. Curar
    
Ingrese su opción:     
          """)
    
    # • Validación del Menú: El programa debe pedir la opción al usuario. 1. Verificar que lo 
    # ingresado sea un número (.isdigit()).  
    # 2. Verificar que el número sea 1, 2 o 3.  
    # o Si falla alguna validación, mostrar mensaje de error y volver a pedir.  

    while not opcion.isdigit(): 
        opcion = input("Elija una opción válida: ")

    while int(opcion) <= 0 or int(opcion) >3: 
        opcion = input("Opción fuera de rango: ")

    # Lógica de las Acciones:  
    # Acción A: Ataque Pesado (Opción 1)  
    # • • Calcula el daño final. Si la vida del enemigo es menor a 20 puntos, el jugador 
    # realiza un "Golpe Crítico" multiplicando su daño base por 1.5 (resultado float).  
    # • • Resta el daño a la vida del enemigo.  
    # • • Muestra un mensaje: "¡Atacaste al enemigo por X puntos de daño!"  

    if opcion == "1":
        if vida_enemigo < 20:
            dano_final = dano_ataque_pesado * 1.5
            vida_enemigo -= dano_final
        else:
            dano_final = dano_ataque_pesado
            vida_enemigo -= dano_final

        print(f"¡Atacaste al enemigo por {dano_final} puntos de daño!")
    
    
    # Acción B: Ráfaga Veloz (Opción 2)  
    # • • Esta acción realiza una serie de golpes rápidos. Debes implementar un bucle for.  
    # • • El bucle debe repetirse 3 veces (usando range).  
    # • • Dentro del bucle, en cada repetición: 1. Resta 5 puntos de daño a la vida del enemigo.  
    # • 2. Muestra el mensaje: " > Golpe conectado por 5 de daño".  
    # •  
    elif opcion == "2":
        for i in range (3):
            vida_enemigo-=5
            print("> Golpe conectado por 5 de daño")
    
    # Acción C: Curar (Opción 3) 
    elif opcion == "3":
        # • • Si tienes pociones (> 0): Suma 30 puntos a tu vida y resta 1 poción.
        if pociones_vida > 0:
            vida_gladiador += 30
            if vida_gladiador > 100:
                vida_gladiador = 100
            pociones_vida -= 1
        
        # • • Si NO tienes pociones: Muestra "¡No quedan pociones!" y pierdes el turno (el 
        # enemigo ataca igual).  
        else:
            print("¡No quedan pociones! Pierdes el turno.")
            turno_gladiador = False
    
    # Turno del Enemigo:  
    # Turno del Enemigo:  
    # Justo después de tu acción, el enemigo ataca automáticamente.  
    # • • Resta el daño base del enemigo (12) a tu vida. 
    if turno_gladiador == False :
        vida_gladiador-= dano_base_enemigo

        # • • Muestra un mensaje: "¡El enemigo te atacó por 12 puntos de daño!" 
        print("¡El enemigo te atacó por 12 puntos de daño!")   


# Paso 4: Fin del Juego  
# Cuando el ciclo termine (porque la vida de alguno llegó a 0 o menos), debes evaluar:  
# • • Si vida_jugador > 0: Mostrar "¡VICTORIA! [Nombre] ha ganado la batalla."  
# • • Si vida_jugador <= 0: Mostrar "DERROTA. Has caído en combate."  

if vida_gladiador > 0:
    print(f"¡VICTORIA! {gladiador} ha ganado la batalla")
else:
    print("DERROTA. Has caído en combate.")

 

 
