# Ejercicio 4  — “Escape Room: La Bóveda”
# Sos un agente que intenta abrir una bóveda con 3 cerraduras. Tenés energía y tiempo 
# limitados. 
# Si abrís las 3 cerraduras antes de quedarte sin energía o sin tiempo, ganás.

energia = 100 
tiempo = 12 
cerraduras_abiertas = 0 
alarma = False 
codigo_parcial = ""
forzar_cerraduras = 0

# • Pedir nombre del agente y validar con .isalpha() en un while. 
# • Validar opciones del menú y cualquier número pedido con .isdigit() en un 
# while. 
# • El juego debe funcionar con estructuras secuenciales, condicionales y 
# repetitivas (puede usar funciones propias del lenguaje como .lower(), len(), 
# formateo, etc.). 

agente = input("Ingrese nombre del agente: ")

while agente == "" or not agente.isalpha(): 
    agente = input("Error, agente inválido ingrese sólo letras: ")

# En cada turno mostrar el estado y el siguiente menú:
opcion =  input(f"""
                
Estado:
                
    Energía: {energia}
    Tiempo: {tiempo}
    Cerraduras abiertas: {cerraduras_abiertas}
    Alarma: {alarma}
                
 Menú:
                
    1. Forzar cerradura
    2. Hackear Panel
    3. Descansar

    
Ingrese su opción: """)

while not opcion.isdigit(): 
    opcion = input("Elija una opción válida: ")

while int(opcion) <= 0 or int(opcion) >3: 
    opcion = input("Opción fuera de rango: ")

# El juego continúa mientras: 
# • energia > 0, tiempo > 0, cerraduras_abiertas < 3 
# • y no esté bloqueado por alarma. 
# Regla anti-spam (muy importante) 
# Para evitar que el jugador gane eligiendo “Forzar cerradura” 3 veces seguidas al 
# iniciar: 
# ✅ Si el jugador elige Forzar cerradura (opción 1) 3 veces seguidas, entonces: 
# • se cobra el costo normal (-20 energía, -2 tiempo)

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and forzar_cerraduras <3 :

    # 1. Forzar cerradura (costo: -20 energía, -2 tiempo)
    if opcion == "1":
        energia -=20
        tiempo -= 2
        forzar_cerraduras += 1


        # Regla anti-spam: si es la 3ra vez seguida forzando, se activa alarma y 
        # no abre. 

        if forzar_cerraduras == 3:
            alarma = True
            break

        # Si la energía está por debajo de 40, hay “riesgo de alarma”: 
        # ▪ pedir un número 1-3 (validado). Si elige 3 → alarma=True. 
        # Si no hay alarma, abre 1 cerradura. 

        elif energia<40:
            riesgo_alarma = input("Riesgo de alarma: Elija un numero del 1 al 3: ")
            while not riesgo_alarma.isdigit(): 
                riesgo_alarma = input("Elija una opción válida: ")

            while int(riesgo_alarma) <= 0 or int(riesgo_alarma) >3: 
                riesgo_alarma = input("Opción fuera de rango: ")
            if riesgo_alarma == "3":
                alarma = True
            else:
                cerraduras_abiertas +=1
        else:
            cerraduras_abiertas +=1


    # 2. Hackear panel (costo: -10 energía, -3 tiempo) 
    elif opcion == "2":
        energia -=10
        tiempo -= 3

        # Si el jugador elige opción 2 o 3, se corta la racha de “forzar seguidas”. 
        forzar_cerraduras = 0

        # o Debe usar un for de 4 pasos mostrando progreso. 
        # o En cada paso sumar una letra al codigo_parcial (por ejemplo “A”). 

        for i in range(4):
            codigo_parcial+= "A"

        # o Si len(codigo_parcial) >= 8, se abre automáticamente 1 cerradura si 
        # todavía faltan.
        if len(codigo_parcial)>=8:
            cerraduras_abiertas +=1
        



    # 3. Descansar (costo: +15 energía (máx 100), -1 tiempo; 
 
    elif opcion == "3":
        
        energia +=15
                
        # (máx 100)
        if energia > 100:
            energia = 100

        tiempo -= 1

        # Si el jugador elige opción 2 o 3, se corta la racha de “forzar seguidas”. 
        forzar_cerraduras = 0

        # si alarma ON: -10 energía extra) 
        if alarma == True:
            energia -=10
 



    # Menú de acciones (se repite mientras el juego siga) 

    opcion =  input(f"""
                
Estado:
                
    Energía: {energia}
    Tiempo: {tiempo}
    Cerraduras abiertas: {cerraduras_abiertas}
    Alarma: {alarma}
                
 Menú:
                
    1. Forzar cerradura
    2. Hackear Panel
    3. Descansar

    
Ingrese su opción: """)

    while not opcion.isdigit(): 
        opcion = input("Elija una opción válida: ")

    while int(opcion) <= 0 or int(opcion) >3: 
        opcion = input("Opción fuera de rango: ")

        
# Condiciones de fin 



# • Si se bloquea por alarma → DERROTA (bloqueo)
# • Si alarma == True y tiempo <= 3 y todavía no se abrió la bóveda, el sistema 
# se bloquea y se pierde.
if alarma == True and forzar_cerraduras == 3 or alarma == True and tiempo <= 3:
    print("DERROTA (bloqueo))")

# • Si cerraduras_abiertas == 3 → VICTORIA 

elif cerraduras_abiertas == 3:
    print ("¡VICTORIA!")

# • Si energia <= 0 o tiempo <= 0 → DERROTA 
elif energia <= 0 or tiempo <= 0:
    print("DERROTA")









