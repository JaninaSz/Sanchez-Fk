from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/cuentas')
def cuentas():
   persona_titular = lista_de_datos['dni']
   return render_template('home-banking.html',
                           saludo=persona_titular.saludo(),
                           movements=persona_titular.obtener_todos_los_movimientos())
@app.route('/proceso')
def proceso():
    persona_titular = lista_de_datos['dni']
    return render_template('proceso.html',saludo=persona_titular.saludo())

@app.route('/nuevo')
def nuevo():
    nuevo_cliente=lista_de_datos['dni']
    return render_template('nuevo.html',crear_cuenta=nuevo_cliente.crear_cuenta())

if __name__ == '__main__':
   import proceso_cuentas
   lista_de_datos = proceso_cuentas.crear_cuentas()
   app.run(debug=True)