# importa flask
# request es para obtener los datos de un formulario envio y obtencion de parametros
from flask import Flask, render_template, request
# importa g para poder utilizar las variables globales
from flask import g
# importa flash para poder mostrar mensajes en la aplicacion
from flask import flash
#proteje contra ataques tipo csrf
from flask_wtf.csrf import CSRFProtect
# importa forms para poder utilisar los formularios del otro archivo
import forms

## crea el objeto de la aplicación
# app corre ejecuta toda la aplicacion
app=Flask(__name__, template_folder='templates')
app.secret_key="Esta es la llave secreta"
csrf = CSRFProtect()

# esta funcion se ejecuta cuando se produce un error 404 que no encuentra el recurso o la pagina
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


# esta fucnion o decorador se ejecuta antes de que se ejecute la aplicacion
@app.before_request
def before_request():
    g.nombre="mario"
    print("before request 1")
    
    
# esta funcion o decorador se ejecuta antes de que se ejecute la aplicacion
@app.after_request
def after_request(response):
    print("After request 3")  
    return response



# crea una ruta o decorador
@app.route('/')
def index():
    grupo="IDGS803"

    lista=["Juan", "Pedro", "mario"]
    print("Index 2")
    print("Hola {}".format(g.nombre))
    # redner_template() reanderiza y obtienen el archivo del html
    return render_template('index.html', grupo = grupo, lista= lista)



@app.route('/Alumnos', methods=["GET","POST"])
def alumnos():
    mat=""
    nom=""
    edad=""
    correo=""
    ape=""
    # crea una instancia/objeto de la clase UserForm, y obtien elos valores
    alumno_clase=forms.UserForm(request.form)
    # revisa si todas las validaciones son correctas o validad del formulario
    if request.method == "POST" and alumno_clase.validate():
        # obtiene los datos del formulario con las variables de la clase
        mat=alumno_clase.matricula.data
        nom=alumno_clase.nombre.data
        ape=alumno_clase.apellidos.data
        edad=alumno_clase.edad.data
        correo=alumno_clase.correo.data
        # crea un mensaje con el nombre del alumno
        mensaje='Bienvenido {}'.format(nom)
        # muestra el mensaje en la aplicacion
        flash(mensaje)
    return render_template("Alumnos.html", form=alumno_clase, mat=mat, nom=nom, ape=ape, edad=edad, correo=correo)
    
    


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
    # pasa los parametros que definimos de la clave secreta
    csrf.init_app(app)
    # app.run() corre la aplicacion y debug=True para que se actualice automaticamente solo con recargar la pagina en el navegador
    # port = (numero) indica el cuarpo en el que se vaa ejecutar la aplicacion/servidor
    app.run(debug=True, port=3000)