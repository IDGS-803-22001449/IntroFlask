# importa flask
# request es para obtener los datos de un formulario envio y obtencion de parametros
from flask import Flask, render_template, request

## crea el objeto de la aplicación
# app corre ejecuta toda la aplicacion
app=Flask(__name__, template_folder='templates')

# crea una ruta o decorador
@app.route('/')
def index():
    grupo="IDGS803"
    
    lista=["Juan", "Pedro", "mario"]
    # redner_template() reanderiza y obtienen el archivo del html
    return render_template('index.html', grupo = grupo, lista= lista)

@app.route('/operasBas', methods=['POST', 'GET'])
def operaBasicas():
    if request.method == 'POST':
        num1 = request.form.get("n1")
        num2 = request.form.get("n2")
        operacion = request.form.get("opOperacion")
        if operacion == "suma":
            resOp = "La suma de {} y {} es: {}".format(num1, num2, int(num1)+int(num2))
        elif operacion == "resta":
            resOp = "La resta de {} y {} es: {}".format(num1, num2, int(num1)-int(num2))
        elif operacion == "multiplicacion":
            resOp = "La multiplicación de {} y {} es: {}".format(num1, num2, int(num1)*int(num2))
        elif operacion == "division":
            resOp = "La división de {} y {} es: {}".format(num1, num2, int(num1)/int(num2))
        
        return render_template('operasBas.html', resOp=resOp)
    return render_template('operasBas.html', resOp='')



@app.route('/resultado', methods=['GET','POST'])
def resultado():
    if request.method == "POST":
        # obtiene los datos del formulario con el id o nombre en el html
        num1 = request.form.get("n1")
        num2 = request.form.get("n2")
        return "La suma de {} + {} es: {}".format(num1, num2, int(num1)+int(num2))

@app.route('/ejemplo1')
def ejemplo1():
    return render_template('ejemplo1.html')

@app.route('/ejemplo2')
def ejemplo2():
    return render_template('ejemplo2.html')

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


# @app.route("/default")
# @app.route("/default/<string:nom>")
# def func(nom='pedro'):
#     return "El nombre de Nom es "+nom

@app.route("/form1")
def form1():
    return '''
        <form>
            <label>Nombre:</label>
            <input type="text" name="nombre" placeholder="Nombre">
            </br>
            <label>Apellido</label>
            <input type="text" name="nombre" placeholder="Nombre">
            </br>
        </form>
    '''

## ejecuta la aplicacion
if __name__ == '__main__':
    # app.run() corre la aplicacion y debug=True para que se actualice automaticamente solo con recargar la pagina en el navegador
    # port = (numero) indica el cuarpo en el que se vaa ejecutar la aplicacion/servidor
    app.run(debug=True, port=3000)