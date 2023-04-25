from flask import Flask, request, render_template, url_for

app = Flask(__name__)
@app.route('/')
def home():
	return render_template("index.html")

@app.route('/login')
def login():
	#return "this is login page"
	return render_template("login.html")


@app.route('/register')
def register():
	#return "this is register page"
	return render_template("register.html")

@app.route('/register2')
def register_2():
	return render_template("register_2.html")


if __name__=='__main__':
	app.run()
