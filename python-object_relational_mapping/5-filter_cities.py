#!/usr/bin/python3
"""
script that takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    """
    Connects to a MySQL database and lists all cities of a given state in ascending order by id.
    """
    # Conectar a la base de datos usando argumentos
    database = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Crear un cursor para ejecutar consultas SQL
    cursor = database.cursor()
    # Ejecutar la consulta SQL para obtener todas las ciudades junto con sus estados
    cursor.execute("SELECT cities.name FROM cities JOIN states ON cities.state_id = states.id WHERE states.name = %s ORDER BY cities.id ASC", (sys.argv[4],))
    # Obtener todas las filas resultantes de la consulta
    rows = cursor.fetchall()
    # almacenar los nombres de las ciudades en una lista
    city_names = [row[0] for row in rows]
    # Imprimir los nombres de las ciudades separados por comas
    print(", ".join(city_names))
    # Cerrar el cursor y la conexión a la base de datos
    cursor.close()
    database.close()
