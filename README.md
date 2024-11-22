🚀 Proyecto Dockerizado: ETL con PostgreSQL y Python 🐳🐍
¡Bienvenidos a mi proyecto más reciente! 🌟 Aquí les presento un sistema ETL (Extract, Transform, Load) completamente dockerizado 🛠️, que combina PostgreSQL, Python y Docker para mostrar cómo gestionar datos en un entorno distribuido con replicación de bases de datos y consultas web dinámicas.

🌟 ¿Qué hace este proyecto?
Este proyecto demuestra cómo integrar tecnologías modernas en un entorno ETL utilizando contenedores Docker. Incluye:

🗄️ Bases de Datos:

Una base de datos principal (PostgreSQL) con soporte para replicación.
Una réplica en tiempo real para garantizar alta disponibilidad.
🧾 Inserción Automática de Datos:

Pedidos de Pizza 🍕: Se registran pedidos de manera automática en la tabla pizza_orders.
Vehículos 🚗: Se insertan datos aleatorios de vehículos (marca, color, placa) en la tabla vehiculos.
🌐 Visualización Web Dinámica:

Pedidos de Pizza: http://localhost:5000/pizza-orders
Muestra los pedidos en una tabla bonita y estilizada.
Vehículos: http://localhost:5000/vehiculos
Visualiza los datos de vehículos en un diseño atractivo.
🐳 Infraestructura Dockerizada:

Configuración de Docker Compose para orquestar servicios y aplicaciones.
Todo el proyecto encapsulado en contenedores para garantizar su portabilidad y facilidad de uso.
🧩 Características Principales
Base de datos PostgreSQL con réplica para asegurar disponibilidad y escalabilidad.
Inserción automatizada de datos en tiempo real cada 10 segundos.
Interfaz web amigable para consultar los datos almacenados en las tablas.
Totalmente modular y fácil de extender para proyectos más grandes.
🔧 Tecnologías Utilizadas
🐳 Docker y Docker Compose: Para gestionar y desplegar los contenedores.
🗄️ PostgreSQL: Base de datos principal y réplica.
🐍 Python:
Librería Flask para construir las aplicaciones web.
Librería psycopg2 para interactuar con la base de datos.
🎨 HTML y CSS: Para diseñar tablas estilizadas y bonitas.
🏃 ¿Cómo ejecutarlo?
Clona el repositorio:

bash
Copiar código
git clone https://github.com/FrankDesarrollo/proyecto-Dockerizado-Postgres-python.git
cd proyecto-Dockerizado-Postgres-python
Construye y ejecuta los contenedores:

bash
Copiar código
docker-compose up --build
Abre tu navegador y explora:

Pedidos de Pizza: http://localhost:5000/pizza-orders
Vehículos: http://localhost:5000/vehiculos
🎯 ¿Por qué es interesante este proyecto?
💻 Ideal para aprender sobre arquitectura distribuida.
🛠️ Perfecto para practicar integración con Docker y PostgreSQL.
🌍 Portabilidad total: Todo está encapsulado en contenedores.
📊 Listo para expandirse: Este proyecto puede ser la base de sistemas más complejos.
🌟 Demo Visual
🎥 Pedidos de Pizza:

🎥 Vehículos:

(Reemplaza los enlaces con tus propias imágenes o gifs del proyecto).

💡 Próximos pasos
🚀 Implementar nuevas tablas y relaciones para expandir las funcionalidades.
🌐 Mejorar la interfaz con frameworks modernos como React o Vue.js.
📈 Agregar análisis en tiempo real de los datos generados.
🤝 Conéctate conmigo
Si este proyecto te pareció interesante o tienes sugerencias, ¡no dudes en escribirme! 💬

📧 Correo: frank.palma@gmail.com
💼 LinkedIn: Frank Palma

¡Espero que este proyecto inspire a otros desarrolladores a explorar la magia de Docker y PostgreSQL! 🌟✨
