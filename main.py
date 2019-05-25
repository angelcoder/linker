from flask import Flask, render_template, request, redirect
import shorten_url as su
import urllib

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<url>', methods=['GET'])
def redirect_origin(url):
    link = su.original_link(url)
    return redirect(link, code=302)


@app.route('/make-request')
def make_request():
    link = request.args.get('urllink')
    if link:
        urllib.request.urlopen(link)

    return redirect('https://stackoverflow.com/questions/45040365/flask-redirect-to-page-then-come-back')

@app.route('/', methods=['POST'])
def getvalue():
    link = request.form['urllink']
    res = su.link_hash(link)
    s = 47*'_'
    res2 = su.original_link(res)
    return render_template('index.html', n = res, m = res2)


if  __name__ == "__main__":
    app.run(debug=True)
