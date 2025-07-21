from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods = ['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        precio_pintura = 9000
        total_origen = 0
        total_descuento = 0
        total_final = 0

        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad_tarros = int(request.form['cantidad_tarros'])

        total_origen = cantidad_tarros * precio_pintura

        if edad >= 18 and edad <= 30:
            total_descuento = total_origen * 0.15
        elif edad > 30:
            total_descuento = total_origen * 0.25

        total_final = total_origen - total_descuento

        return render_template('ejercicio1.html', nombre=nombre, total_origen=total_origen, total_descuento=total_descuento, total_final=total_final)
    return render_template('ejercicio1.html')

@app.route('/ejercicio2', methods = ['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        aUsuariosPermitidos = [
            {'nombre':'juan', 'contrasena':'admin', 'rol':'administrador'},
            {'nombre':'pepe', 'contrasena':'user', 'rol':'usuario'}
        ]
        paso = 2
        valido = False
        nombre = request.form['nombre']
        contrasena = request.form['contrasena']
        rol = ''

        for usuario in aUsuariosPermitidos:
            if usuario['nombre'] == nombre and usuario['contrasena'] == contrasena:
                rol = usuario['rol']
                valido = True

        return render_template('ejercicio2.html', nombre=nombre, contrasena=contrasena, rol=rol, valido=valido, paso=paso)
    return render_template('ejercicio2.html')




if __name__ == '__main__':
    app.run(debug=True)
