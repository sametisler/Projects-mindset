
from flask import Flask, render_template , request
import flask
from tc_kimlik_generator import tc_kimlik_no_uret
result = []
app = Flask(__name__)

__all__ = ["create_app"]


def create_app():
    app = flask.Flask(__name__)
    app.config.from_pyfile('settings.py')


@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/result', methods=['GET', 'POST'])
def tc():
    result.clear() # çıktı için oluşturulan liste elemanlarını siler.
    number = int(request.form.get('number', 0))
    for i in range(number):
        result.append(tc_kimlik_no_uret()) # result listesine üretilen tc kimlik no'larını eleman olarak atar.

    return render_template('result.html', result = result)


