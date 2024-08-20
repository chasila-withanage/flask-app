from flask import Flask
import socket

app = Flask(__name__)

@app.route('/info')
def welcome():
    hostname = socket.gethostname()
    return f'Welcome from {hostname}!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
