from flask import Flask, render_template, request, url_for, redirect

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=os.environ['PORT'])


