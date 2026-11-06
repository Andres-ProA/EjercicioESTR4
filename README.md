# Ejercicio: Registro y Login con Python, MySQL y Bootstrap

## Archivos del Proyecto

EjercicioFrontBackBD/
│
├── app.py                 # Conexión MySQL, funciones (guardar, validar) y rutas
├── database.sql           # Script SQL para crear la base de datos y la tabla en MySQL
├── requirements.txt       # Librerías necesarias (Flask y mysql-connector-python)
├── README.md              # Documentación
│
└── templates/
    ├── login.html         # Pantalla 1: Iniciar Sesión (con validación de credenciales)
    ├── registro.html      # Pantalla 2: Crear Cuenta (guarda en MySQL)
    └── home.html          # Pantalla 3: Saludo de bienvenida

## Cómo Ejecutar

1. **Instalar los requerimientos**:
   Abre una terminal en esta carpeta y ejecuta:
   ```bash
   pip install -r requirements.txt
   ```

2. **Iniciar la aplicación**:
   ```bash
   python app.py
   ```

3. **Abrir en tu navegador**:
   Entra a:
   http://localhost:5000
