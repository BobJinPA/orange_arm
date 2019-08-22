# This code is teaching how to read events from the USB controller

from evdev import InputDevice, categorize, ecodes
import maestro

servo = maestro.Controller("/dev/ttyAMA0")
gamepad = InputDevice('/dev/input/event0')
INCREMENT = 100
ACCELERATION = 20
SPEED = 2
MIN = 4000
CENTER = 6000
MAX = 8000

servo.setRange(0, MIN, MAX)
servo.setAccel(0, ACCELERATION)
servo.setSpeed(0, SPEED)
currentPosition = servo.getPosition(0)
print ("Current position: " + str(currentPosition))
servo.setTarget(0, CENTER)  # initial position
currentPosition = servo.getPosition(0)
print ("Current position: " + str(currentPosition))
print ("get min: ", servo.getMin(0))
print ("get max: ",  servo.getMax(0))

for event in gamepad.read_loop():
    currentPosition = servo.getPosition(0)
    print ("Current position: " + str(currentPosition))
    if not servo.isMoving(0):
        if event.type == 1:
            if event.code == 293 and event.value == 1:
                print ("Top Right Button: ", currentPosition + INCREMENT)
                if (currentPosition + INCREMENT) <= MAX:
                    servo.setTarget(0, currentPosition + INCREMENT)
            elif event.code == 292 and event.value == 1:
                print ("Top Left Button: ", currentPosition - INCREMENT)
                if (currentPosition - INCREMENT) >= MIN:
                    servo.setTarget(0, currentPosition - INCREMENT)
        print ("Current position: " + str(currentPosition))


servo.close
