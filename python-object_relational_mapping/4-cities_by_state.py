#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    """
    Connects to a MySQL database and lists all cities in ascending order by id.
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
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC")
    # Obtener todas las filas resultantes de la consulta
    rows = cursor.fetchall()

    # Imprimir cada fila
    for row in rows:
        print(row)

    # Cerrar el cursor y la conexión a la base de datos
    cursor.close()
    database.close()
