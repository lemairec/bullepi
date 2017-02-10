from flask import Flask, render_template
import piplates.RELAYplate as RELAY
import piplates.MOTORplate as MOTOR
import socket


RELAY.getID(0)
MOTOR.dcCONFIG(2,1,'ccw',0,2.5)

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('home.html')

@app.route("/relay_on/<int:relay_number>")
def relay_on(relay_number):
    RELAY.relayON(0,relay_number)
    return render_template('home.html')

@app.route("/motor/<int:motor_number>/<int:value>")
def motor(motor_number,value):
    print str(value)
    MOTOR.dcSPEED(2,motor_number,value)
    if(value > 20):
        MOTOR.dcSTART(2,motor_number)
    else:
        MOTOR.dcSTOP(2,motor_number)
    return render_template('home.html')

@app.route("/relay_off/<int:relay_number>")
def relay_off(relay_number):
    RELAY.relayOFF(0,relay_number)
    return render_template('home.html')

if __name__ == "__main__":
    print " *** serveur run"
    print " *** ip : " + str(socket.gethostbyname(socket.gethostname()))
    app.run(host='0.0.0.0', port=8000)
