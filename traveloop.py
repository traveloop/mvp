from flask import Flask, request, url_for, redirect
app = Flask(__name__)


@app.route('/')
def root():
    return redirect(url_for('static', filename='html/index.html'))


if __name__ == '__main__':
    app.run()
