# importa flask
from flask import Flask

## crea el objeto de la aplicación
# app corre ejecuta toda la aplicacion
app=Flask(__name__)

# crea una ruta o decorador
@app.route('/')
def index():
    return "Hola Mundo!!! Nuevo 1.0"

# crea una ruta o decorador
@app.route("/hola")
def hola():
    return "Hola!!!!"

# crea una ruta o decorador que resive un parametro de tipo string 
@app.route("/user/<string:user>")
def user(user):
    return f"Hola {user}!!!"

# crea una ruta o decorador que resive un parametro de tipo int
@app.route("/numero/<int:n>")
def numero(n):
    return f"Numero {n}"

# crea una ruta o decorador que resive un parametro de diferentes tipos juntos
@app.route("/user/<string:user>/<int:id>")
def username(user, id):
    return f"Nombre; {user} ID: {id}!!!"

## crea una ruta o decorador que resive un parametro de tipo float
@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1,n2):
    return "La suma es: {}!!".format(n1+n2)


@app.route("/default")
@app.route("/default/<string:nom>")
def func(nom='pedro'):
    return "El nombre de Nom es "+nom

## ejecuta la aplicacion
if __name__ == '__main__':
    # app.run() corre la aplicacion y debug=True para que se actualice automaticamente solo con recargar la pagina en el navegador
    # port = (numero) indica el cuarpo en el que se vaa ejecutar la aplicacion/servidor
    app.run(debug=True, port=3000)