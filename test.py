from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('0.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=os.environ['PORT'])


