
from flask import Flask, render_template, request, abort

app = Flask(__name__)


# MENU PRINCIPAL
@app.route("/")
def inicio():
    return render_template("index.html")


# EJERCICIO 1: NOTAS Y ASISTENCIA
@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():

    if request.method == "POST":
        try:
            nota1 = float(request.form["nota1"])
            nota2 = float(request.form["nota2"])
            nota3 = float(request.form["nota3"])
            asistencia = float(request.form["asistencia"])

            if not all(10 <= n <= 70 for n in [nota1, nota2, nota3]):
                abort(400, description="Las notas deben estar entre 10 y 70.")

            if not 0 <= asistencia <= 100:
                abort(400, description="La asistencia debe estar entre 0 y 100.")

            promedio = round((nota1 + nota2 + nota3) / 3, 2)

            if promedio >= 40 and asistencia >= 75:
                estado = "Aprobado"
            else:
                estado = "Reprobado"

            return render_template(
                "resultado1.html",
                promedio=promedio,
                asistencia=asistencia,
                estado=estado
            )

        except (ValueError, KeyError):
            abort(400, description="Ingresa datos numéricos válidos.")

    return render_template("ejercicio1.html")


# EJERCICIO 2: COMPARAR NOMBRES
@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():

    if request.method == "POST":

        nombre1 = request.form.get("nombre1", "").strip()
        nombre2 = request.form.get("nombre2", "").strip()
        nombre3 = request.form.get("nombre3", "").strip()

        nombres = [nombre1, nombre2, nombre3]

        if any(not nombre for nombre in nombres):
            abort(400, description="Debes completar los tres nombres.")

        nombre_mayor = max(nombres, key=len)
        cantidad = len(nombre_mayor)

        return render_template(
            "resultado2.html",
            nombre=nombre_mayor,
            cantidad=cantidad
        )

    return render_template("ejercicio2.html")


# MANEJO DE ERRORES
@app.errorhandler(400)
def error_400(error):
    return f"Error: {error.description} <a href='/'>Volver al inicio</a>", 400


# EJECUTAR APLICACION
if __name__ == "__main__":
    app.run(debug=True)
