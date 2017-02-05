from flask import Flask, render_template
import RPi.GPIO as GPIO
import socket


GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT, initial=GPIO.HIGH)

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('home.html')

@app.route("/relay_on")
def relay_on():
    GPIO.output(4, GPIO.LOW)
    return render_template('home.html')

@app.route("/relay_off")
def relay_off():
    GPIO.output(4, GPIO.HIGH)
    return render_template('home.html')

if __name__ == "__main__":
    print " *** serveur run"
    print " *** ip : " + str(socket.gethostbyname(socket.gethostname()))
    app.run()
