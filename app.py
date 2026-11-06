from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

# Función para conectar a MySQL
def conectar():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='1234',
        database='usuarios_app'
    )

# 1. FUNCIÓN PARA GUARDAR (REGISTRO)
def guardar(usuario, password):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute(
        "INSERT INTO usuarios (usuario, password) VALUES (%s, %s)",
        (usuario, password)
    )
    conexion.commit()
    cursor.close()
    conexion.close()

# 2. FUNCIÓN PARA VALIDAR CREDENCIALES (LOGIN)
def validar(usuario, password):
    conexion = conectar()
    cursor = conexion.cursor(buffered=True)
    cursor.execute(
        "SELECT * FROM usuarios WHERE usuario = %s AND password = %s",
        (usuario, password)
    )
    usuario_encontrado = cursor.fetchone()
    cursor.close()
    conexion.close()
    return usuario_encontrado


# --- RUTAS DE NAVEGACIÓN ---

# PANTALLA 1: INICIAR SESIÓN (LOGIN)
@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST']) 
def login():
    if request.method == 'POST':
        user = request.form['usuario']
        clave = request.form['password']

        # Validamos si existe en MySQL
        if validar(user, clave):
            return render_template('home.html', usuario=user)
        else:
            return render_template('login.html', error='Usuario o contraseña incorrectos.')

    return render_template('login.html')


# PANTALLA 2: REGISTRO
@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        user = request.form['usuario']
        clave = request.form['password']

        # Guardar en MySQL
        guardar(user, clave)
        return render_template('login.html', mensaje='¡Cuenta creada con éxito! Ahora inicia sesión.')

    return render_template('registro.html')


if __name__ == '__main__':
    app.run()
