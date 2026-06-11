from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/instructores')
def instructores():
    return render_template('instructores.html')

@app.route('/crear_instructor')
def crear_instructor():
    return render_template('crear_instructor.html')

@app.route('/actualizar_instructor')
def actualizar_instructor():
    return render_template('actualizar_instructor.html')

@app.route('/eliminar_instructor')
def eliminar_instructor():
    return render_template('eliminar_instructor.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/evaluaciones')
def evaluaciones():
    return render_template('evaluaciones.html')

@app.route('/fichas')
def fichas():
    return render_template('fichas.html')

@app.route('/reportes')
def reportes():
    return render_template('reportes.html')

if __name__ == '__main__':
    app.run(debug=True)