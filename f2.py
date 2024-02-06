from flask import Flask
from flask import render_template
from flask import request

from flask import Flask, redirect, url_for, request
app = Flask(__name__)

diccionario = {
    'Adrian': 'pedrosanchez@asix2.com',
    'Emma': 'pacosanz@gmail.com',
    'Dabit': 'argentino@gmail.com',
    'Brunito': 'elcigala@gmail.com'
}

def mail(name):
    if name in diccionario:
        email = diccionario[name]
        return email
    return ("No encontrado")

@app.route('/addmail',methods = ['POST', 'GET'])
def addmail():
   if request.method == 'POST':
      nombre = request.form['name']
      email = request.form['mail']
      diccionario[nombre] = email
      return render_template('formulario.html')
   else:
      return render_template('añadirmail.html')

@app.route('/getmail',methods = ['POST', 'GET'])
def getmail():
   if request.method == 'POST':
      user = request.form['name']
      email=mail(user)
      return render_template('resultado.html',mail = email, nombre = user)
   else:
      return render_template('formulario.html')

if __name__ == '__main__':
   app.run(debug = True)