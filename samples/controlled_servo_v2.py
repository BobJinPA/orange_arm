# This code is teaching how to read events from the USB controller

from evdev import InputDevice, categorize, ecodes
import maestro

servo = maestro.Controller("/dev/ttyAMA0")
gamepad = InputDevice('/dev/input/event0')
INCREMENT = 20

servo.setAccel(0, 4)
servo.setSpeed(0, 10)
servo.setTarget(0, 6000)  # initial position
print ("Current position: " + str(currentPosition))
print ("get min: " + servo.getMin())
print ("get max: " + servo.getMax())

for event in gamepad.read_loop():
    currentPosition = servo.getPosition(0)
    print ("Current position: " + str(currentPosition))
    # user_input = raw_input()
    # if input == 'X':
    #     break
    if event.type == 1:
        if event.code == 293 and event.value == 1:
            print ("Top Right Button: "+ currentPosition + INCREMENT)
            servo.setTarget(0, currentPosition + INCREMENT)
        elif event.code == 292 and event.value == 1:
            print ("Top Left Button: " + currentPosition - INCREMENT)
            servo.setTarget(0, currentPosition - INCREMENT)
    print ("Current position: " + str(currentPosition))


servo.close
