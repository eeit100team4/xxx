from flask import Flask, render_template, request, url_for, redirect
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('靜態首頁1016.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=int(os.environ['PORT']))


