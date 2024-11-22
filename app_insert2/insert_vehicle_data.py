import psycopg2
import os
from time import sleep
import random

# Configuración de la base de datos desde las variables de entorno
DATABASE_HOST = os.environ.get('DATABASE_HOST', 'localhost')
DATABASE_NAME = os.environ.get('DATABASE_NAME', 'postgres')
DATABASE_USER = os.environ.get('DATABASE_USER', 'user')
DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD', 'password')

# Datos aleatorios para generar vehículos
carros = ['Toyota', 'Chevrolet', 'Ford', 'Hyundai', 'Kia', 'Nissan']
colores = ['Rojo', 'Azul', 'Blanco', 'Negro', 'Gris', 'Verde']

def generar_placa():
    """Generar una placa vehicular aleatoria."""
    letras = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=3))
    numeros = ''.join(random.choices('0123456789', k=3))
    return f"{letras}-{numeros}"

def connect_to_db():
    """Establecer conexión con la base de datos."""
    connection = None
    while connection is None:
        try:
            connection = psycopg2.connect(
                host=DATABASE_HOST,
                dbname=DATABASE_NAME,
                user=DATABASE_USER,
                password=DATABASE_PASSWORD
            )
            print("Conexión exitosa a la base de datos.")
        except Exception as e:
            print(f"Error al conectar a la base de datos: {e}")
            sleep(5)
    return connection

def insert_random_vehicle():
    """Generar e insertar un vehículo aleatorio en la base de datos."""
    conn = connect_to_db()
    cursor = conn.cursor()
    try:
        # Generar datos aleatorios
        carro = random.choice(carros)
        color = random.choice(colores)
        placa = generar_placa()

        # Insertar datos en la tabla
        cursor.execute("""
            INSERT INTO vehiculos (carro, color, placa)
            VALUES (%s, %s, %s)
        """, (carro, color, placa))
        conn.commit()
        print(f"Vehículo insertado: {carro}, {color}, {placa}.")
    except Exception as e:
        print(f"Error al insertar el vehículo: {e}")
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    # Bucle infinito para insertar datos cada 10 segundos
    while True:
        insert_random_vehicle()
        sleep(10)
