from flask import Flask, request

app = Flask(__name__)

# --- DATOS DE PRUEBA ---
lista_alumnos = [
    {'nombre': 'Joel', 'nota': 10, 'carrera': 'Ing. en Computación'},
    {'nombre': 'Emily', 'nota': 8, 'carrera': 'Ing. Informática'},
    {'nombre': 'Mateo', 'nota': 2, 'carrera': 'Ing. Industrial'}
]

# Estilos comunes para reutilizar (Colores oficiales de iOS)
ESTILO_BODY = "font-family: -apple-system, sans-serif; background-color: #f2f2f7; color: #1c1c1e; margin: 0; padding: 20px;"
ESTILO_BOTON = "background-color: #007aff; color: white; padding: 12px 20px; text-decoration: none; border-radius: 12px; font-weight: 600; display: inline-block; margin: 5px 0;"
ESTILO_CARD = "background-color: white; border-radius: 20px; padding: 25px; box-shadow: 0 4px 12px rgba(0,0,0,0.05); border: 1px solid #e5e5ea; max-width: 500px; margin: 0 auto;"

@app.route('/')
def home():
    return f"""
    <body style="{ESTILO_BODY}">
        <div style="{ESTILO_CARD} text-align: center;">
            <h1 style="font-size: 28px; font-weight: 800;">🎓 Portal FIUBA</h1>
            <p style="color: #8e8e93;">Bienvenido, <b>Joel</b></p>
            <hr style="border: 0; border-top: 1px solid #e5e5ea; margin: 20px 0;">
            <div style="display: flex; flex-direction: column; gap: 10px;">
                <a href="/estudiante" style="{ESTILO_BOTON}">Ver Mi Ficha</a>
                <a href="/lista" style="{ESTILO_BOTON}">Lista de Alumnos</a>
                <a href="/sumar?n1=10&n2=5" style="{ESTILO_BOTON}">➕ Calculadora</a>
            </div>
        </div>
    </body>
    """

@app.route('/estudiante')
def detalle():
    return f"""
    <body style="{ESTILO_BODY}">
        <div style="{ESTILO_CARD} text-align: center;">
            <h2 style="margin-top: 0;">Ficha del Alumno</h2>
            <img src="/static/IMG_5291.JPG" alt="Foto de Joel" width="180" style="border-radius: 50%; border: 4px solid #f2f2f7;">
            <h3 style="margin: 15px 0 5px 0;">Joel Galindo</h3>
            <p style="color: #8e8e93; margin: 0;">19 años | FIUBA</p>
            
            <div style="text-align: left; background: #f8f8fa; border-radius: 15px; padding: 15px; margin: 20px 0;">
                <h4 style="margin: 0 0 10px 0; color: #007aff;">Materias Actuales</h4>
                <ul style="margin: 0; padding-left: 20px; line-height: 1.6;">
                    <li>Análisis Matemático II</li>
                    <li>Algoritmos y Programación</li>
                    <li>Intro. al Desarrollo de Software</li>
                </ul>
            </div>
            <a href="/" style="color: #007aff; text-decoration: none; font-weight: 600;">⬅️ Volver al Inicio</a>
        </div>
    </body>
    """

@app.route('/lista')
def ver_lista():
    filas_tabla = ""
    for alumno in lista_alumnos:
        color_nota = "#34c759" if alumno['nota'] >= 7 else "#9C3631"
        filas_tabla += f"""
            <tr style="border-bottom: 1px solid #e5e5ea;">
                <td style="padding: 12px; font-weight: 500;">{alumno['nombre']}</td>
                <td style="padding: 12px; color: {color_nota}; font-weight: bold;">{alumno['nota']}</td>
                <td style="padding: 12px; font-size: 13px;">{alumno['carrera']}</td>
            </tr>
        """

    return f"""
    <body style="{ESTILO_BODY}">
        <div style="{ESTILO_CARD}">
            <h2 style="text-align: center; margin-top: 0;">Listado de Alumnos</h2>
            <table style="width: 100%; border-collapse: collapse; text-align: left;">
                <thead>
                    <tr style="color: #8e8e93; font-size: 12px; text-transform: uppercase;">
                        <th style="padding: 10px;">Nombre</th>
                        <th style="padding: 10px;">Nota</th>
                        <th style="padding: 10px;">Carrera</th>
                    </tr>
                </thead>
                <tbody>
                    {filas_tabla}
                </tbody>
            </table>
            <br>
            <div style="text-align: center;">
                <a href="/" style="color: #007aff; text-decoration: none; font-weight: 600;">⬅️ Volver al Inicio</a>
            </div>
        </div>
    </body>
    """

@app.route('/sumar')
def sumar():
    n1 = request.args.get('n1', default=0, type=int)
    n2 = request.args.get('n2', default=0, type=int)
    resultado = n1 + n2
    
    return f"""
    <body style="{ESTILO_BODY}">
        <div style="{ESTILO_CARD} text-align: center;">
            <div style="font-size: 50px;">🧮</div>
            <h2 style="margin: 10px 0;">Resultado</h2>
            <div style="background: #f2f2f7; border-radius: 15px; padding: 20px; margin: 15px 0;">
                <p style="margin: 0; color: #8e8e93;">La suma de {n1} + {n2} es</p>
                <h1 style="margin: 5px 0; color: #007aff; font-size: 40px;">{resultado}</h1>
            </div>
            <a href="/" style="color: #007aff; text-decoration: none; font-weight: 600;">⬅️ Volver al Inicio</a>
        </div>
    </body>
    """

if __name__ == '__main__':
    app.run(debug=True, port=7000)