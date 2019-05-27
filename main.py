from flask import Flask, render_template, request, redirect
import shorten_url as su
import requests
import urllib

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<url>', methods=['GET'])
def redirect_origin(url):
    link = su.original_link(url)
    return redirect(link, code=302)


@app.route('/', methods=['POST'])
def getvalue():
    link = request.form['urllink']
    res = su.link_hash(link)
    s = 47*'_'
    res2 = su.original_link(res)
    return render_template('index.html', n = res, m = res2)


if  __name__ == "__main__":
    app.run(debug=True)
