from flask import Flask, render_template
import psycopg2
import os

app = Flask(__name__)

# Configuración de la base de datos desde las variables de entorno
DATABASE_HOST = os.environ.get('DATABASE_HOST', 'localhost')
DATABASE_NAME = os.environ.get('DATABASE_NAME', 'replicator')
DATABASE_USER = os.environ.get('DATABASE_USER', 'replicator_password')
DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD', 'password')

def connect_to_db():
    """Establecer conexión con la base de datos."""
    return psycopg2.connect(
        host=DATABASE_HOST,
        dbname=DATABASE_NAME,
        user=DATABASE_USER,
        password=DATABASE_PASSWORD
    )

@app.route('/pizza-orders', methods=['GET'])
def get_pizza_orders():
    """Obtener todos los pedidos de pizza y mostrarlos en una tabla bonita."""
    conn = connect_to_db()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM pizza_orders;")
        rows = cursor.fetchall()
        # Enviar datos a la plantilla HTML
        return render_template('pizza_orders.html', rows=rows)
    except Exception as e:
        return f"Error: {str(e)}", 500
    finally:
        cursor.close()
        conn.close()

@app.route('/vehiculos', methods=['GET'])
def get_vehiculos():
    """Obtener todos los vehículos y mostrarlos en una tabla bonita."""
    conn = connect_to_db()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM vehiculos;")
        rows = cursor.fetchall()
        # Enviar datos a la plantilla HTML
        return render_template('vehiculos.html', rows=rows)
    except Exception as e:
        return f"Error: {str(e)}", 500
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
