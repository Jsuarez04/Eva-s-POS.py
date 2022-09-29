#El menú principal tendrá las siguientes opciones#
#-Menú ARCHIVO#
#-Menú MOVIMIENTOS#
#-Menú AYUDA#
#-SALIR#


print("::: BIENVENIDO A LIBRERIA EVA'S POS :::")
Usuarios={'master':1234, "gerente":5678}
Clientes={"Efectivo":0000000}
inventario={"Libretas": "ESCO01"}
iva=16/100
contador= 0
# Declaramos las funciones secundarias que utlizara el programa
#Sub-menu productos#
def reporte_ventas():
    print('ns')

def nuevas_facturas():
    print("\t :: FACTURA ::")
    print("1. REALIZAR NUEVA FACTURA")
    print("2. SALIR")
    opcion_fac=int(input("INGRESE EL NUMERO DE SU OPCION: "))
    if opcion_fac == 1:
        print("\t::FACTURA::")
        cliente=(input("Cliente: "))
        if cliente in Clientes:
            while cliente in Clientes:
                producto=(input("-: "))
                if producto in inventario:
                    cantidad=float(input("Cantidad: "))
                    if cantidad<=0:
                        print("ERROR")
                        return nuevas_facturas()
                    else:
                        precio=float(input("Precio: "))
                        if precio<=0:   
                            print("ERROR")
                            return nuevas_facturas()
                
                        else:
                            print("culo")
                            return nuevas_facturas()
                else:   
                    print("Producto no registrado")
                    return nuevas_facturas()
        else:
            print("Cliente no registrado")
            return nuevas_facturas()



def Menu_productos():
    print("\t :: PRODUCTOS ::")
    print("1. ::: Agregar producto :::")
    print("2. ::: Eliminar de producto :::")
    print("3. ::: Inventario :::")
    print("4. ::: SALIR :::")
    opcion_productos=int(input("Ingrese el número de su opción: "))
    if opcion_productos==1:
        print("\t::AGREGAR PRODUCTO::")
        agg_prod=input("Ingrese el nombre del producto: ")
        agg_codigo=input("Ingrese el código del producto: ")
        inventario[agg_prod]= agg_codigo 
        print("PRODUCTO AGREGADO EXITOSAMENTE")
        return Menu_productos()

    elif opcion_productos==2:
        contador=0
        print("\t::ELIMINAR PRODUCTO::")
        for key in inventario:
            contador+=1
            print(f"{contador}. {key}")
            opcion_elim_prod = input("Ingrese el nombre o el codigo del producto a eliminar")
        
        if opcion_elim_prod in inventario:
            inventario.pop(opcion_elim_prod)
            print("\tPRODUCTO ELIMINADO")
            return Menu_productos
        else:
            print("\tPRODUCTO NO REGISTRADO")
            return Menu_productos
    elif opcion_productos == 3:
        print("\t===INVENTARIO===") 
        print("PRODUCTO  -   CODIGO  ")
        for key, value in inventario.items():
                print(f"{key}  \t{value}")
        
        Salir= input("Escribe salir para retroceder: ")
        if Salir == "salir":
            return Menu_productos()
    elif opcion_productos == 4:
        return Menu_principal()
#Sub-menu usuarios#
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
#Opcion cambios de usuario#
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
#Opcion cambios de clave#
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
#Sub-menu clientes#
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

        elif opcion_archivo == 3:
            return Menu_productos()

        elif opcion_archivo == 4:
            return CambiodeUsuario()

        elif opcion_archivo == 5:
            return CambiosdeClave()

        elif opcion_archivo == 6:
            return Menu_principal()  
    if opcion == 2:  
        print("\t :: MOVIMIENTOS ::")
        print("1. ::: Nueva factura :::")
        print("2. ::: Reporte de ventas :::")
        print("3. ::: SALIR :::")    
        opcion_movimientos=int(input("Ingrese el número de su opción: "))
        if opcion_movimientos == 1:
            return nuevas_facturas()
        elif opcion_movimientos == 2:
            return reporte_ventas()
            

# Se declara un ciclo indefinido hasta que el usuario ingrese un usuario y clave validos
while True:
    usuario_=input("Ingrese su nombre de usuario:")
    clave_=int(input("Ingrese su clave numerica:"))
    if usuario_ in Usuarios and clave_ == Usuarios[usuario_]:
        Menu_principal()
        break
    else:
        print("Usuario y/o contaseña incorrectos ¡Inténtelo de nuevo!...")






        