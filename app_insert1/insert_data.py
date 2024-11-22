import psycopg2
import os
from time import sleep
import random

# Configuración de la base de datos desde las variables de entorno
DATABASE_HOST = os.environ.get('DATABASE_HOST', 'localhost')
DATABASE_NAME = os.environ.get('DATABASE_NAME', 'postgres')
DATABASE_USER = os.environ.get('DATABASE_USER', 'user')
DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD', 'password')

# Datos aleatorios para generar pedidos
nombres = ['Juan', 'María', 'Carlos', 'Ana', 'Luis']
pizzas = ['Pepperoni', 'Hawaiana', 'Margarita', 'Vegetariana', '4 Quesos']
cantidades = [1, 2, 3, 4, 5]

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

def insert_random_order():
    """Generar e insertar un pedido aleatorio en la base de datos."""
    conn = connect_to_db()
    cursor = conn.cursor()
    try:
        # Generar datos aleatorios
        nombre = random.choice(nombres)
        pizza = random.choice(pizzas)
        cantidad = random.choice(cantidades)

        # Insertar datos en la tabla
        cursor.execute("""
            INSERT INTO pizza_orders (customer_name, pizza_type, quantity)
            VALUES (%s, %s, %s)
        """, (nombre, pizza, cantidad))
        conn.commit()
        print(f"Pedido insertado: {nombre} pidió {cantidad} pizza(s) de {pizza}.")
    except Exception as e:
        print(f"Error al insertar el pedido: {e}")
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    # Bucle infinito para insertar datos cada 10 segundos
    while True:
        insert_random_order()
        sleep(10)
