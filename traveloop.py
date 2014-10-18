from flask import Flask, request
app = Flask(__name__, static_url_path='')

@app.route('/')
def root():
    return app.send_static_file('static/html/index.html')

import os
@app.route('/js/<path:path>')
def static_proxy(path):
    # send_static_file will guess the correct MIME type
    return app.send_static_file(os.path.join('js', path))

if __name__ == '__main__':
    app.run(host='0.0.0.0')
