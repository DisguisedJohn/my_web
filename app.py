from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():

	title = "Boom!"
	return render_template("index.html", kokos = title) #Predavani parametru kokos

@app.route('/about')
def about():
	names = ["Jan", "Pep", "Sep"]
	return render_template("about.html", list = names)
