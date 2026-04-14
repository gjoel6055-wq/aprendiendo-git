import mysql.connector
from bd_facultad import conectar_db

def inicializar_base_de_datos():
    try:
        conn = conectar_db()
        cursor = conn.cursor()

        with open('facu_db.sql', 'r') as f:
            sql_script = f.read()

        for result in cursor.execute(sql_script, multi=True):
            pass

        conn.commit()
        print("¡Base de datos inicializada con éxito!")

        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error al inicializar: {e}")


if __name__ == "__main__":
    inicializar_base_de_datos()