import flask 
app = flask.Flask(__name__)
@app.route('/')
def home():
    return "¡Bienvenido a mi primera aplicación Flask!"

if __name__ == '__main__':app.run(debug=True)
