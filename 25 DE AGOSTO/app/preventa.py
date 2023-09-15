# Importando módulos necesarios de Flask y la conexión a la base de datos.
from flask import Flask, request, render_template
from confiDB import *  # Importando conexión a la base de datos (importar confiDB)

# Creando una instancia de la aplicación Flask.
app = Flask(__name__)

# Definición de la ruta '/preventa' para la página de inicio de preventa.
@app.route('/preventa')
def inicio():
    return render_template('public/PreVenta.html')  # Renderiza la plantilla 'public/PreVenta.html'

# Definición de la ruta '/form' para el registro de preventas.
@app.route('/form', methods=['GET', 'POST'])
def registrarPreVenta():
    msg = ''  # Variable para almacenar mensajes de respuesta.

    # Verifica si la solicitud es de tipo POST (cuando se envía el formulario).
    if request.method == 'POST':
        # Obtiene los datos del formulario.
        idPrenda = request.form['idPrenda']
        fecha = request.form['fecha']
        fechaEnvio = request.form['fechaEnvio']
        estado = request.form['estado']

        # Establece una conexión a la base de datos.
        conexion_MySQLdb = connectionBD()
        cursor = conexion_MySQLdb.cursor(dictionary=True)

        # Prepara y ejecuta la consulta SQL para insertar datos en la tabla 'PreVenta'.
        sql = ("INSERT INTO PreVenta(idPrenda, fecha, fechaEnvio, estado) VALUES (%s, %s, %s, %s)")
        valores = (idPrenda, fecha, fechaEnvio, estado)
        cursor.execute(sql, valores)
        conexion_MySQLdb.commit()

        cursor.close()  # Cierra el cursor de la conexión SQL.
        conexion_MySQLdb.close()  # Cierra la conexión a la base de datos.

        msg = 'Registro con éxito'  # Mensaje de éxito.

        print(cursor.rowcount, "registro insertado")  # Imprime la cantidad de registros insertados.
        print("1 registro insertado, id", cursor.lastrowid)  # Imprime el ID del último registro insertado.

        return render_template('public/PreVenta.html', msg='Formulario enviado')
    else:
        return render_template('public/PreVenta.html', msg='Método HTTP incorrecto')

# Ejecución de la aplicación Flask si el archivo se ejecuta como un script independiente.
if __name__ == '__main__':
    app.run(debug=True, port=5000)
