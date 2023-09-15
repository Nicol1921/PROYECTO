# Importando Flask y render_template desde Flask
from flask import Flask, render_template

# Creando una instancia de la aplicación Flask
app = Flask(__name__)

# Definición de la ruta '/index' para la página de inicio
@app.route('/index')
def inicio():
    return render_template('public/index.html')  # Renderiza la plantilla 'public/index.html'

# Definición de la ruta '/catalogo' para la página de catálogo
@app.route('/catalogo')
def catalogo():
    return render_template('public/catalogo.html')  # Renderiza la plantilla 'public/catalogo.html'

# Definición de la ruta '/blusas' para la página de blusas
@app.route('/blusas')
def blusas():
    return render_template('public/blusas.html')  # Renderiza la plantilla 'public/blusas.html'

# Definición de la ruta '/vestidos' para la página de vestidos
@app.route('/vestidos')
def vestidos():
    return render_template('public/vestidos.html')  # Renderiza la plantilla 'public/vestidos.html'

# Definición de la ruta '/contacto' para la página de contacto
@app.route('/contacto')
def contacto():
    return render_template('public/contacto.html')  # Renderiza la plantilla 'public/contacto.html'

# Definición de la ruta '/login' para la página de inicio de sesión
@app.route('/login')
def login():
    return render_template('public/login.html')  # Renderiza la plantilla 'public/login.html'

@app.route('/home')
def home():
    return render_template('public/home.html')  # Renderiza la plantilla 'public/login.html'

# Ejecución de la aplicación Flask si el archivo se ejecuta como un script independiente.
if __name__ == '__main__':
    app.run(debug=True, port=5500)
