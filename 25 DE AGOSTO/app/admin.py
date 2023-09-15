# Importando los módulos necesarios de Flask y la conexión a la base de datos.
from flask import Flask, request, render_template
from confiDB import *

# Creando una instancia de la aplicación Flask.
app = Flask(__name__)

# Definición de la ruta '/admin' para la página de inicio.
@app.route('/admin')
def inicio():
    # Renderiza la plantilla 'public/Admin.html' al acceder a '/admin'.
    return render_template('public/Admin.html')

# Definición de la ruta '/form' para el registro de administradores.
@app.route('/form', methods=['GET', 'POST'])
def registrarAdmin():
    msg = ''  # Variable para almacenar mensajes de respuesta.

    # Verifica si la solicitud es de tipo POST.
    if request.method == 'POST':
        # Obtiene los datos del formulario.
        Nom = request.form['Nom']
        Apl = request.form['Apl']
        User = request.form['User']
        Pass = request.form['Pass']
        confirmm = request.form['confirmm']

        # Establece una conexión a la base de datos.
        conexion_MySQLdb = connectionBD()
        cursor = conexion_MySQLdb.cursor(dictionary=True)

        # Prepara y ejecuta la consulta SQL para insertar datos en la tabla 'Administrador'.
        sql = ("INSERT INTO Administrador(Nom, Apl, User, Pass, confirmm) VALUES (%s, %s, %s, %s, %s)")
        valores = (Nom, Apl, User, Pass, confirmm)
        cursor.execute(sql, valores)
        conexion_MySQLdb.commit()

        cursor.close()  # Cierra el cursor de la conexión SQL.
        conexion_MySQLdb.close()  # Cierra la conexión a la base de datos.

        msg = 'Registro con éxito'  # Mensaje de éxito.

        print(cursor.rowcount, "registro insertado")  # Imprime la cantidad de registros insertados.
        print("1 registro insertado, id", cursor.lastrowid)  # Imprime el ID del último registro insertado.

        return render_template('public/Admin.html', msg='Formulario enviado')
    else:
        return render_template('public/Admin.html', msg='Método HTTP incorrecto')

# Ejecución de la aplicación Flask si el archivo se ejecuta como un script independiente.
if __name__ == '__main__':
    app.run(debug=True, port=5500)
