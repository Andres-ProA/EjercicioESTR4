# Sistema de Registro y Login (Python, MySQL y Bootstrap)

Aplicacion web para el registro y autenticacion de usuarios conectada a una base de datos MySQL.

## Estructura del Proyecto

```text
EjercicioFrontBackBD/
├── app.py                 # Servidor Flask, conexion a MySQL y funciones
├── database.sql           # Script SQL para crear la base de datos y la tabla
├── requirements.txt       # Dependencias del proyecto
├── README.md              # Documentacion
└── templates/
    ├── login.html         # Pantalla de inicio de sesion
    ├── registro.html      # Pantalla de registro de usuarios
    └── home.html          # Pantalla principal (bienvenida)
```

## Requisitos Previos

- Python 3 instalado
- Servidor MySQL en ejecucion

## Base de Datos

Antes de iniciar la aplicacion, ejecuta el script `database.sql` en tu cliente de MySQL para crear la base de datos `usuarios_app` y la tabla `usuarios`.

Verifica en `app.py` que las credenciales de conexion coincidan con tu entorno local:
- Host: localhost
- Usuario: root
- Password: tu contrasena (por defecto: 1234)
- Base de datos: usuarios_app

## Instalacion y Ejecucion

1. Instalar las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

2. Iniciar la aplicacion:
   ```bash
   python app.py
   ```

3. Abrir en el navegador:
   http://localhost:5000
