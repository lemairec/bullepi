from flask import Flask, render_template
app = Flask(__name__)
import socket


@app.route("/")
def hello():
    return render_template('home.html')

@app.route("/relay1")
def relay1():
    return "Hello World!"

if __name__ == "__main__":
    print " *** serveur run"
    print " *** ip : " + str(socket.gethostbyname(socket.gethostname()))
    app.run()
