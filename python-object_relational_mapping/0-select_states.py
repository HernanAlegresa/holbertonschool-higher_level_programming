#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa
"""
# Importar modulos MySQL para ejecutar consultas a database desde python y sys para acceder a los argumentos.
import MySQLdb
import sys

if __name__ == "__main__":
    """
    Connects to a MySQL database and lists all states in ascending order by id.
    """
    database = MySQLdb.connect(  # Establece conexion con la database y agrego los (argumentos) argv dentro.
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = database.cursor() # Obj cursor para poder interactuar con la database.
    cursor.execute("SELECT * FROM states ORDER BY id ASC") # Ejecucion de consulta SQL.
    rows = cursor.fetchall() # Rows son las filas devueltas por la consulta, fetchall las recupera.

    for row in rows:
        print(row)

    cursor.close()
    database.close()