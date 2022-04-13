from flask import Flask 
from flask import render_template
import  os
app = Flask(__name__)

RUTA = os.getcwd() + "/static/img"

@app.route('/')
def index():
	return render_template("index.html")


@app.route("/animes")
def animes():
	ruta = RUTA + "/Posted Animes"
	contenido = os.listdir(ruta)
	return render_template("plantilla.html", contenido = contenido, bloque = "Posted Animes")


@app.route("/series")
def series():
	ruta = RUTA + "/Posted Series"
	contenido = os.listdir(ruta)
	return render_template("plantilla.html", contenido = contenido, bloque = "Posted Series")

@app.route("/peliculas")
def peliculas():
	ruta = RUTA + "/Posted Peliculas"
	contenido = os.listdir(ruta)
	return render_template("plantilla.html", contenido = contenido, bloque = "Posted Peliculas")

if __name__=='__main__':
	app.run(debug=True)