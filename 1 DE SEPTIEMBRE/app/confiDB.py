# Importando la librería mysql.connector para conectar Python con MySQL
import mysql.connector

# Función para establecer una conexión a la base de datos.
def connectionBD():
    # Configuración de los parámetros de conexión.
    mydb = mysql.connector.connect(
        host="localhost",   # Dirección del servidor de la base de datos.
        user="root",        # Nombre de usuario de la base de datos.
        passwd="",          # Contraseña de la base de datos (dejar en blanco si no hay contraseña).
        database="santyfashion"  # Nombre de la base de datos a la que se desea conectar.
    )

    # Verifica si la conexión se estableció con éxito.
    if mydb:
        print("Conexión exitosa")  # Mensaje de éxito en la conexión.
    else:
        print("Error en la conexión a BD")  # Mensaje de error en caso de fallo en la conexión.

    return mydb  # Retorna la conexión establecida o None en caso de fallo.
