from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

# Verifica si el número es par/impar:
@app.route("/parimpar/<int:numero>")
def show_parimpar(numero):
    if numero % 2 == 0:
        return f"El número {numero} es par."
    else:
        return f"El número {numero} es impar."

# Say hello
@app.route("/hello")
@app.route("/hello/<name>")
def ola(name=None):
    return render_template("hello.html",name=name)

# Nombre y edad
@app.route("/edad/<name>/<int:edad>")
def edades(name,edad):
    resta = 100 - edad
    cien = 2024 + resta
    return render_template("100.html",name=name,cien=cien)
