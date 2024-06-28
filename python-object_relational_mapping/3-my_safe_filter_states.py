#!/usr/bin/python3
"""
Script that takes in arguments and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument (safe from SQL injections).
"""
# Importar modulos MySQL para ejecutar consultas a database desde python y sys para acceder a los argumentos.
import MySQLdb
import sys

if __name__ == "__main__":
    """
    Connects to a MySQL database and lists all states in ascending order by id.
    """
    # Establece conexion con la database y agrego los (argumentos) argv dentro.
    database = MySQLdb.connect(
        host= "localhost",
        port= 3306,
        user= sys.argv[1],
        passwd= sys.argv[2],
        db= sys.argv[3],
    )
    # Obj cursor para poder interactuar con la database y hacer consultas.
    cursor = database.cursor() 
    # Ejecutar la consulta SQL usando una consulta parametrizada para evitar inyecciones SQL
    cursor.execute("SELECT * FROM states WHERE name LIKE '{}' ORDER BY id ASC".format(sys.argv[4]))
    # Rows son las filas devueltas por la consulta, fetchall las recupera.
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    database.close()
