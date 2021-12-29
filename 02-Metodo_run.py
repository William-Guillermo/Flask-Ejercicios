from logging import debug
from flask import Flask

app = Flask (__name__)
@app.route('/')
def index():
    return ("metodo Run")

@app.route('/Contacto')
def Contacto():
   return (" Segunda Ruta  lamada Contacto")

if __name__ == '__main__':
    app.run(debug=True, port=8000)