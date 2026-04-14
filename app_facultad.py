from flask import Flask, request, jsonify
import mysql.connector
from bd_facultad import conectar_db

app = Flask(__name__)

@app.route('/alumnos/<int:padron>', methods = ['GET'] )
def buscar_alumno(padron):
    if padron <= 0:
        return jsonify({'error':'No se ingreso un padron valido'}), 400

    try:
        conn = conectar_db()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM alumnos WHERE padron = %s"

        cursor.execute(query, (padron, ))
        alumno_buscado = cursor.fetchone()
        cursor.close()
        conn.close()

        if not alumno_buscado:
            return jsonify({'error':'No existe un alumno con ese padron'}), 404

        return jsonify(alumno_buscado), 200

    except mysql.connector.Error:
        return jsonify({'error':'no se pudo conectar a la base de datos'}), 500

@app.route('/alumnos/<int:padron>/notas', methods=['GET'])
def buscar_notas_alumno(padron):
    if padron <= 0:
        return jsonify({'error':'No se ingreso un padron valido'}), 400

    try:
        conn = conectar_db()
        cursor = conn.cursor(dictionary = True)
        query = """
                 SELECT materias.codigo_materia, materias.nombre, notas.nota, notas.fecha 
                 FROM notas 
                 INNER JOIN alumnos ON notas.padron = alumnos.padron 
                 INNER JOIN materias ON notas.codigo_materia = materias.codigo_materia
                 WHERE notas.padron = %s
        """

        cursor.execute(query, (padron, ))
        notas_alumno = cursor.fetchall()
        cursor.close()
        conn.close()

        if not notas_alumno:
            return jsonify({'error':'No existen notas asociadas a el padron ingresado'}), 404

        return jsonify(notas_alumno), 200

    except mysql.connector.Error:
        return jsonify({'error':'no se pudo conectar a la base de datos'}), 500

@app.route('/alumnos/<int:padron>/notas', methods=['POST'])
def ingresar_nota(padron):
    if padron <= 0:
        return jsonify({'error':'No se ingreso un padron valido'}), 400

    datos_ingresados = request.get_json()
    codigo_materia = datos_ingresados.get('codigo_materia')
    nota = datos_ingresados.get('nota')
    fecha = datos_ingresados.get('fecha')

    try:
        conn = conectar_db()
        cursor = conn.cursor()

        query = "INSERT INTO notas (codigo_materia, nota, fecha, padron) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (codigo_materia, nota, fecha, padron))
        conn.commit()

        cursor.close()
        conn.close()
        return jsonify({
            'mensaje': 'Se creo la nota con exito'
        }), 201

    except mysql.connector.Error:
        return jsonify({'error': 'no se pudo conectar a la base de datos'}), 500

@app.route('/materias/<int:codigo_materia>/alumnos', methods=['GET'])
def consultar_clase(codigo_materia):
    if codigo_materia <= 0:
        return jsonify({'error': 'codigo  de la materia es invalido'}), 400

    try:
        conn = conectar_db()
        cursor = conn.cursor(dictionary=True)
        query = """
                SELECT DISTINCT materias.codigo_materia, alumnos.padron, alumnos.nombre, alumnos.apellido
                FROM notas
                INNER JOIN materias ON notas.codigo_materia = materias.codigo_materia
                WHERE notas.codigo_materia = %s     
        """

        cursor.execute(query, (codigo_materia, ))
        alumnos_materia = cursor.fetchall()
        cursor.close()
        conn.close()

        return jsonify(alumnos_materia), 200

    except mysql.connector.Error:
        return jsonify({'error': 'no se pudo conectar a la base de datos'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=8000)