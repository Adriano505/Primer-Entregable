BD = {}

def registrar_usuario():
    while True:
        user = input("Ingrese el nombre de usuario: ")
        if user in BD:
            print("El nombre de usuario ya está en uso. Por favor, ingrese otro.")
        else:
            contraseña = input("Ingrese la contraseña: ")
            BD[user] = {"contraseña": contraseña, "intentos_fallidos": 0}
            print("Usuario registrado exitosamente.")
            break

def iniciar_sesion():
    user = input("Ingrese el nombre de usuario: ")
    if user not in BD:
        print("Nombre de usuario incorrecto.")
        return
    if BD[user]["intentos_fallidos"] >= 3:
        print("La cuenta ha sido bloqueada. Por favor, contacte al administrador.")
        return
    contraseña = input("Ingrese la contraseña: ")
    if BD[user]["contraseña"] == contraseña:
        print("Inicio de sesión exitoso.")
        BD[user]["intentos_fallidos"] = 0
    else:
        print("Contraseña incorrecta.")
        BD[user]["intentos_fallidos"] += 1
        if BD[user]["intentos_fallidos"] >= 3:
            print("La cuenta ha sido bloqueada. Por favor, contacte al administrador.")


while True:
    print("1) Registrar usuario")
    print("2) Iniciar sesión")
    print("3) Ver base de datos")
    print("4) Salir")
    
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_usuario()
    elif opcion == "2":
        iniciar_sesion()
    elif opcion == "3":
        print(BD)
    elif opcion == "4":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")