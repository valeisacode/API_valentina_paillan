import hashlib
import requests

usuarios = {}

def crearusuario():
    nombre = input("Ingrese nombre de usuario: ")
    if nombre in usuarios:
        print("Usuario ya existe.")
        return
    clave = input("Ingrese contraseña: ")
    clave_encriptada = hashlib.sha256(clave.encode()).hexdigest()
    usuarios[nombre] = clave_encriptada
    print(f"Usuario {nombre} creado correctamente.")

def login():
    nombre = input("Ingrese usuario: ")
    clave = input("Ingrese contraseña: ")
    clave_encriptada = hashlib.sha256(clave.encode()).hexdigest()
    if usuarios.get(nombre) == clave_encriptada:
        print("Login exitoso.")
    else:
        print("Credenciales incorrectas.")

def obtenerdatausuarios():
    url = "https://jsonplaceholder.typicode.com/users"
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        usuarios = respuesta.json()
        for u in usuarios:
            print(f"{u['id']} - {u['name']} ({u['email']})")
    else:
        print("Error en la solicitud GET.")

def enviardatapost():
    url = "https://jsonplaceholder.typicode.com/posts"
    titulo = input("Título del post: ")
    cuerpo = input("Cuerpo del post: ")
    data = {"title": titulo, "body": cuerpo, "userId": 1}
    respuesta = requests.post(url, json=data)
    if respuesta.status_code == 201:
        print("Post enviado correctamente. ID:", respuesta.json()['id'])
    else:
        print("Error al enviar POST.")

def actualizarpostput():
    url = "https://jsonplaceholder.typicode.com/posts"
    id_post = input("ID del post a actualizar: ")
    titulo = input("Nuevo titulo: ")
    cuerpo = input("Nuevo cuerpo: ")
    data = {"id": int(id_post), "title": titulo, "body": cuerpo, "userId": 1}
    respuesta = requests.put(f"{url}/{id_post}", json=data)
    if respuesta.status_code == 200:
        print("Post actualizado correctamente.")
    else:
        print("Error al actualizar.")

def eliminarpost():
    url = "https://jsonplaceholder.typicode.com/posts"
    id_post = input("ID del post a eliminar: ")
    respuesta = requests.delete(f"{url}/{id_post}")
    if respuesta.status_code == 200:
        print("Post eliminado correctamente.")
    else:
        print("Error al eliminar.")

while True:
    print("\nMenú Principal")
    print("1. Registro de Usuarios")
    print("2. Login")
    print("3. Obtener datos desde API (GET)")
    print("4. Enviar datos a API (POST)")
    print("5. Actualizar datos en API (PUT)")
    print("6. Eliminar datos en API (DELETE)")
    print("7. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        crearusuario()
    elif opcion == "2":
        login()
    elif opcion == "3":
        obtenerdatausuarios()
    elif opcion == "4":
        enviardatapost()
    elif opcion == "5":
        actualizarpostput()
    elif opcion == "6":
        eliminarpost()
    elif opcion == "7":
        print("Saliendo...")
        break
    else:
        print("Opción no válida.")
