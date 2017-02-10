import RPi.GPIO as GPIO
import time
import piplates.RELAYplate as RELAY
import piplates.MOTORplate as MOTOR

MOTOR.dcCONFIG(2,1,'ccw',0.0,2.5)
MOTOR.dcSTART(2,1)
time.sleep(5)
MOTOR.dcSPEED(2,1,80.0)
MOTOR.dcSTART(2,1)

RELAY.getID(0)
print "on"
RELAY.relayON(0,3)
time.sleep(3)
print "off"
RELAY.relayOFF(0,3)
MOTOR.dcSTOP(2,1)
