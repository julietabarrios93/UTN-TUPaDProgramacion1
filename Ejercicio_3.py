# ✅ Ejercicio 3 (Alta) — “Agenda de Turnos con Nombres (sin listas)” 
# Contexto 
# Hay 2 días de atención: Lunes y Martes. 
# Cada día tiene cupos fijos: 
# • Lunes: 4 turnos 
# • Martes: 3 turnos 

# Restricciones 
# • ❌ No listas, no diccionarios, no sets, no tuplas. 
# • ✅ Se permite usar "" como “vacío”. 
# • ✅ Validaciones con .isalpha() y .isdigit() (sin try/except).    


# Reglas 
# 1. Pedir nombre del operador (solo letras). 

operador = input("Ingrese nombre del operador: ")

while operador == "" or not operador.isalpha(): 
    operador = input("Error, operador inválido ingrese sólo letras: ")

lunes1="(libre)"
lunes2="(libre)"
lunes3="(libre)"
lunes4="(libre)"
martes1="(libre)"
martes2="(libre)"
martes3="(libre)"

cant_turnos_lunes=0
cant_turnos_martes=0

# 2. Menú repetitivo hasta salir: 


opcion =  input("""Menú:
                
    1. Reservar turno
    2. Cancelar turno
    3. Ver agenda del día
    4. Ver resumen general
    5. Salir
    
Ingrese su opción: """)

while not opcion.isdigit(): 
    opcion = input("Elija una opción válida: ")

while int(opcion) <= 0 or int(opcion) >5: 
    opcion = input("Opción fuera de rango: ")

while opcion != "5":


    if opcion == "1":
    # 1. Reservar turno 
        # Elegir día (1=Lunes, 2=Martes).

        dia = input("Elija día: 1= Lunes o 2= Martes: ")

        while not dia.isdigit(): 
            dia = input("Elija una opción válida: ")

        while int(dia) <= 0 or int(dia) >2: 
            dia = input("Opción fuera de rango: ")

        # Pedir nombre del paciente (solo letras). 

        paciente = input("Ingrese nombre del paciente: ")

        while paciente == "" or not paciente.isalpha(): 
            paciente = input("Error, paciente inválido ingrese sólo letras: ")            

        #Si elige lunes
    
        if dia == "1":

        # Verificar que no esté repetido en ese día (comparando con las variables ya cargadas). 

            if paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4:
                print("Ese paciente ya tiene turno en Lunes.")
            
            # Guardar en el primer espacio libre (ej. lunes1, lunes2…). 
            
            else:
                if lunes1 == "(libre)":
                    lunes1 = paciente
                    print("Turno reservado en Lunes - Turno 1.")

                elif lunes2 == "(libre)":
                    lunes2 = paciente
                    print("Turno reservado en Lunes - Turno 2.")

                elif lunes3 == "(libre)":
                    lunes3 = paciente
                    print("Turno reservado en Lunes - Turno 3.")
                
                elif lunes4 == "(libre)":
                    lunes4= paciente
                    print("Turno reservado en Lunes - Turno 4.")
                
                else:
                    print("Agendia día Lunes llena")

        #Si elige martes

        else: 
            if paciente == martes1 or paciente == martes2 or paciente == martes3:
                print("Ese paciente ya tiene turno en Martes.")
            else:
                if martes1 == "(libre)":
                    martes1 = paciente
                    print("Turno reservado en Martes - Turno 1.")

                elif martes2 == "(libre)":
                    martes2 = paciente
                    print("Turno reservado en Martes - Turno 2.")

                elif martes3 == "(libre)":
                    martes3 = paciente
                    print("Turno reservado en Martes - Turno 3.")
                
                else:
                    print("Agendia día Martes llena")
                





    # 2. Cancelar turno

    elif opcion == "2":
        
        # Elegir día (1=Lunes, 2=Martes).

        dia = input("Elija día: 1= Lunes o 2= Martes: ")

        while not dia.isdigit(): 
            dia = input("Elija una opción válida: ")

        while int(dia) <= 0 or int(dia) >2: 
            dia = input("Opción fuera de rango: ")

        # Pedir nombre del paciente (solo letras). 

        paciente = input("Ingrese nombre del paciente: ")

        while paciente == "" or not paciente.isalpha(): 
            paciente = input("Error, paciente inválido ingrese sólo letras: ")            

        #Si elige lunes
    
        if dia == "1": 

        # Si existe, cancelar y dejar el espacio vacío. 

            if paciente == lunes1:
                lunes1= "(libre)"
                print("Su turno se ha cancelado.")
            
            elif paciente == lunes2:
                lunes2= "(libre)"
                print("Su turno se ha cancelado.")

            elif paciente == lunes3:
                lunes3= "(libre)"
                print("Su turno se ha cancelado.")
            
            elif paciente == lunes4:
                lunes4= "(libre)"
                print("Su turno se ha cancelado.")
            
            else:
                print("Usted no tiene turno asignado para el día Lunes")

        #Si elige martes
        
        else: 

            if paciente == martes1:
                martes1= "(libre)"
                print("Su turno se ha cancelado.")
            
            elif paciente == martes2:
                martes2= "(libre)"
                print("Su turno se ha cancelado.")

            elif paciente == martes3:
                martes3= "(libre)"
                print("Su turno se ha cancelado.")
            
            else:
                print("Usted no tiene turno asignado para el día Lunes")








    # 3. Ver agenda del día
    # Mostrar los turnos del día en orden (Turno 1..N), indicando “(libre)” si está vacío.     

    elif opcion == "3":
        # Elegir día (1=Lunes, 2=Martes).

        dia = input("Elija día: 1= Lunes o 2= Martes: ")

        while not dia.isdigit(): 
            dia = input("Elija una opción válida: ")

        while int(dia) <= 0 or int(dia) >2: 
            dia = input("Opción fuera de rango: ")


        #Si elige lunes
    
        if dia == "1": 

        # Si existe, cancelar y dejar el espacio vacío. 

            print(f""" Agenda día Lunes:
                  
                Lunes 1 - {lunes1}
                Lunes 2 - {lunes2}
                Lunes 3 - {lunes3}
                Lunes 4 - {lunes4}

                  """)

        #Si elige martes
        
        else: 
            print(f""" Agenda día Martes:
                  
                Martes 1 - {martes1}
                Martes 2 - {martes2}
                Martes 3 - {martes3}

                  """)




    # Resumen general: 

    elif opcion == "4":

        # Turnos ocupados y disponibles por día.

        print(f""" Agenda día Lunes:
                  
                Lunes 1 - {lunes1}
                Lunes 2 - {lunes2}
                Lunes 3 - {lunes3}
                Lunes 4 - {lunes4}

                  """)
        print(f""" Agenda día Martes:
                  
                Martes 1 - {martes1}
                Martes 2 - {martes2}
                Martes 3 - {martes3}

                  """)
        
        # Día con más turnos (o empate).

        if lunes1 != "(libre)":
            cant_turnos_lunes += 1
        elif lunes2 != "(libre)":
            cant_turnos_lunes += 1
        elif lunes3 != "(libre)":
            cant_turnos_lunes += 1
        elif lunes3 != "(libre)":
            cant_turnos_lunes += 1
        elif lunes4 != "(libre)":
            cant_turnos_lunes += 1
        elif martes1 != "(libre)":
            cant_turnos_martes += 1
        elif martes2 != "(libre)":
            cant_turnos_martes += 1
        elif martes3 != "(libre)":
            cant_turnos_martes += 1

        if cant_turnos_lunes > cant_turnos_martes:
            print("El día con mas turnos es el Lunes")
        elif cant_turnos_lunes < cant_turnos_martes:
            print("El día con mas turnos es el Martes")
        else:
            print("Empate - Ambos dias tienen la misma cantidad de turnos.")

    

    # Menú repetitivo hasta salir
    opcion =  input("""Menú:
                
    1. Reservar turno
    2. Cancelar turno
    3. Ver agenda del día
    4. Ver resumen general
    5. Salir
    
Ingrese su opción: """)
    
# 5. Salir 

print("Hasta Luego")
