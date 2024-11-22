# Imagen base de Python
FROM python:3.10-slim

# Establecer directorio de trabajo
WORKDIR /app

# Copiar los archivos de la aplicación
COPY app_query.py /app
COPY templates /app/templates

# Instalar dependencias necesarias
RUN pip install flask psycopg2-binary

# Comando para ejecutar la aplicación
CMD ["python", "app_query.py"]
