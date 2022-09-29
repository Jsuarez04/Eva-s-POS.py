#El menú principal tendrá las siguientes opciones#
#-Menú ARCHIVO#
#-Menú MOVIMIENTOS#
#-Menú AYUDA#
#-SALIR#


print("::: BIENVENIDO A LIBRERIA EVA'S POS :::")
Usuarios={"master":1234, "gerente":5678}
Clientes={"Efectivo":0000000}

# Declaramos las funciones secundarias que utlizara el programa
def Menu_Usuarios(): 

    print("\t :: MENU DE USUARIOS ::")
    print("1. ::: Agregar Nuevo Usuario :::")
    print("2. ::: ELiminar Usuario :::")
    print("3. ::: Ver Usuarios :::")
    print("4. ::: Salir :::")
    opcion_usuario=int(input("Ingrese el número de su opción: "))
        
    if opcion_usuario==1:
        print("\t:: Agregar Nuevo Usuario ::")
        agg_us=(input("INGRESE EL NOMBRE DEL NUEVO USUARIO: ")) 
        agg_passw =(input("INGRESE LA CLAVE DEL NUEVO USUARIO: ")) 
        conf=(input("CONFIRME LA CLAVE DEL NUEVO USUARIO: ")) 
        if agg_passw==conf:
            Usuarios[agg_us] = agg_passw
            print("USUARIO AGREGADO EXITOSAMENTE")
            return Menu_Usuarios()
        else:
            print("Clave invalida ¡Inténtelo de nuevo!")    
            return Menu_Usuarios()
    
    elif opcion_usuario == 2:
        contador = 0
        print("\t:: Eliminacion de Usuarios ::")
        for key in Usuarios:
            contador += 1
            print(f"{contador}. {key}")
        opcion_elim = input("Ingrese el nombre del usuario que desea eliminar: ")
            
        if opcion_elim in Usuarios:
            Usuarios.pop(opcion_elim)
            print("Usuario eliminado!")
            return Menu_Usuarios()
        else:
            print("Ese usuario no esta registrado...")
            return Menu_Usuarios()
    
    elif opcion_usuario == 3:
        print("\t:: Reporte de usuarios ::")
        print("Nombre  -  Contraseña  -  Nivel de seguridad")
        for key, value in Usuarios.items():
            if key == "master" or key == "gerente":
                print(f"{key}  \t{value}  \t Alto")
            else:
                print(f"{key}  \t{value}  \t Bajo")
        Salir= input("Escribe salir para retroceder: ")
        if Salir == "salir":
            return Menu_Usuarios()
    
    elif opcion_usuario == 4:
        return Menu_principal()

def CambiodeUsuario():
    global usuario_, clave_
    contador = 0 
    print("\t :: CAMBIO DE USUARIO ::")
    verificacion = int(input("Confirme su clave: "))
    if verificacion == clave_:
        print(f"\t:: Usted ha iniciado sesion como: {usuario_} ::")
        print("¿A que usuario desea cambiar?")
        for key in Usuarios:
            contador += 1
            print(f"{contador}. {key}")
        
        opcion_cambio = input("Ingrese el nombre del usuario al que desea cambiar sesion: ")

        if opcion_cambio in Usuarios:
            verif_clave = int(input(f"Ingrese la clave de `{opcion_cambio}`: "))
            if verif_clave == Usuarios[opcion_cambio]:
                print(f"`{usuario_}` ha cerrado sesion!")
                usuario_ = opcion_cambio
                clave_ = verif_clave
                print(f"Ahora `{usuario_}` tiene sesion iniciada")
                return Menu_principal()
            else:
                print("Usuario invalido!")
                return Menu_principal    
    else:
        print("Clave errada...")
        return Menu_principal()

def CambiosdeClave():
    global usuario_, clave_, Usuarios
    print("\t :: CAMBIO DE CLAVES :::")
    print("1. ::: Cambios de Clave :::\n2. ::: Cambios de Nombre de usuario :::")
    opcion_cambio = int(input("Ingrese el numero de su opcion: "))
    
    if opcion_cambio == 1:
        print(":: Cambiar Clave ::")
        verificacion = int(input("Confirme su clave: "))
        if verificacion == clave_:
            nueva_clave = int(input("Ingrese su nueva clave numerica: "))
            print("")
            nueva_clave2 = int(input("Confirme su nueva clave numerica: "))
            if nueva_clave == nueva_clave2:
                clave_ = nueva_clave
                Usuarios[usuario_] = nueva_clave
                print("Clave cambiada exitosamente")
                print(Usuarios)
                return Menu_principal(), Usuarios
        else:
            print("Fallo en la confirmacion ¡Intente de nuevo!")
            return Menu_principal()


    elif opcion_cambio == 2:
        contador = 0
        print(":: Cambiar Nombre de Usuario ::")
        verificacion = int(input("Confirme su clave: "))
        if verificacion == clave_:
            new_username = input("Ingrese su nuevo nombre de usuario: ")
            print("")
            Confir_username = input("Confirme su nuevo nombre de usuario: ")
            if new_username == Confir_username:
                Usuarios[Confir_username] = Usuarios[usuario_]
                del Usuarios[usuario_]

                print(f"`{usuario_}` ha cambiado de nombre a `{Confir_username}`")
                usuario_ = Confir_username
                return Usuarios, Menu_principal(), usuario_

def Menu_clientes():

    print("\t :: GESTION DE CLIENTES ::")
    print("1. :: Agregar Clientes ::")
    print("2. :: Eliminar Clientes ::")
    print("3. :: Reporte de clientes ::")
    print("4. :: SALIR ::")
    
    opcion_clientes =int(input("Ingrese el numero de opcion: "))
    if opcion_clientes == 1:
        print("\t:: Agregar Nuevo cliente ::")
        agg_cl=(input("INGRESE EL NOMBRE DEL NUEVO CLIENTE: ")) 
        agg_ci =(input("INGRESE LA CEDULA DEL NUEVO CLIENTE: ")) 
        Clientes[agg_cl]= agg_ci
        print("CLIENTE AGREGADO EXITOSAMENTE")
        return Menu_clientes()
    
    elif opcion_clientes == 2:
        contador = 0
        print("\t:: Eliminacion de clientes ::")
        for key in Clientes:
            contador += 1
            print(f"{contador}. {key}")
        opcion_elim = input("Ingrese el nombre del cliente que desea eliminar: ")
            
        if opcion_elim in Clientes:
            Clientes.pop(opcion_elim)
            print("Cliente eliminado!")
            return Menu_clientes()
        else:
            print("Ese Cliente no esta registrado...")
            return Menu_clientes()
    
    elif opcion_clientes== 3:
        print("\t:: Reporte de Clientes ::")
        print("Nombre - C.I / RIF")
        for key, value in Clientes.items():
                print(f"{key}  \t{value}")
        Salir= input("Escribe salir para retroceder: ")
        if Salir == "salir":
            return Menu_clientes()
    
    elif opcion_clientes == 4:
        return Menu_principal()

def Menu_principal():
    print('\t ::: BIENVENIDO :::')
    print("\t:: MENÚ PRINCIPAL ::")
    print("1. ::: ARCHIVO :::")
    print("2. ::: MOVIMIENTOS :::")
    print("3. ::: AYUDA :::")
    print("4. ::: SALIR :::")
    opcion = int(input("Ingrese el número de su opción: "))
    


    if opcion == 1:
        print("\t :: ARCHIVO ::")
        print("1. ::: Usuarios :::")
        print("2. ::: Clientes :::")
        print("3. ::: Productos :::")
        print("4. ::: Cambio de Usuario :::")
        print("5. ::: Cambio de Clave :::")
        print("6. ::: Salir :::")
        opcion_archivo=int(input("Ingrese el número de su opción: "))
    
        if opcion_archivo== 1:
            return Menu_Usuarios()
        elif opcion_archivo==2:
            return Menu_clientes()
        elif opcion_archivo == 6:
            return Menu_principal()

# Luego completamos con una funcion principal que sea capaz de llamar a las demas
def Menu_principal():
    print(f'\t ::: BIENVENIDO {usuario_} :::')
    print("\t:: MENÚ PRINCIPAL ::")
    print("1. ::: ARCHIVO :::")
    print("2. ::: MOVIMIENTOS :::")
    print("3. ::: AYUDA :::")
    print("4. ::: SALIR :::")
    opcion = int(input("Ingrese el número de su opción: "))
    
    if opcion == 1:
        print("\t :: ARCHIVO ::")
        print("1. ::: Usuarios :::")
        print("2. ::: Clientes :::")
        print("3. ::: Productos :::")
        print("4. ::: Cambio de Usuario :::")
        print("5. ::: Cambio de Clave :::")
        print("6. ::: Salir :::")
        opcion_archivo=int(input("Ingrese el número de su opción: "))
    
        if opcion_archivo== 1:
            return Menu_Usuarios()
        
        elif opcion_archivo == 2:
            return Menu_clientes()

        elif opcion_archivo == 4:
            return CambiodeUsuario()

        elif opcion_archivo == 5:
            return CambiosdeClave()

        elif opcion_archivo == 6:
            return Menu_principal()  

# Se declara un ciclo indefinido hasta que el usuario ingrese un usuario y clave validos
while True:
    usuario_=input("Ingrese su nombre de usuario:")
    clave_=int(input("Ingrese su clave numerica:"))
    if usuario_ in Usuarios and clave_ == Usuarios[usuario_]:
        Menu_principal()
        break
    else:
        print("Usuario y/o contaseña incorrectos ¡Inténtelo de nuevo!...")






        