from flask import Flask, render_template, request, redirect
import shorten_url as su

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def getvalue():
    expression = request.form['urllink']
    hash = su.link_hash(expression)
    res = f"http://angelinalogvina.pythonanywhere.com/{hash}"
    s = '_______________________________________________'
    return render_template('index.html', n = res)


if  __name__ == "__main__":
    app.run(debug=True)
