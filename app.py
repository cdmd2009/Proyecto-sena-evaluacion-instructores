from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/instructores")
def instructores():
    return render_template("instructores/index.html")

@app.route("/evaluaciones")
def evaluaciones():
    return render_template("evaluaciones/index.html")

@app.route("/reportes")
def reportes():
    return render_template("reportes/index.html")

@app.route("/fichas")
def fichas():
    return render_template("fichas/index.html")

@app.route("/usuarios")
def usuarios():
    return render_template("usuarios/index.html")

@app.route("/contacto")
def contacto():
    return render_template("contacto/index.html")

@app.route("/configuracion")
def configuracion():
    return render_template("configuracion/index.html")

@app.route("/logout")
def logout():
    return render_template("instructores/index.html")

if __name__ == "__main__":
    app.run(debug=True)