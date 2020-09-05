from flask import Flask , render_template


# routes
app = Flask(__name__)

@app.route('/perfil')
def perfil():
    return render_template('perfil.html')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/ubicacion')
def ubicacion():
    return render_template('ubicacion.html')

@app.route('/contacto')
def contacto():
    return render_template('redes_sociales.html')

@app.route('/informacion')
def informacion():
    return render_template('informacion.html')

@app.route('/mensaje')
def mensaje():
    return render_template('mensaje-de-envio.html')


# middlewares

if __name__ == '__main__':
     app.run(debug=True)   

# settings