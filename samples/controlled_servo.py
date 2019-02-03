# This code is teaching how to read events from the USB controller

from evdev import InputDevice, categorize, ecodes
import maestro

servo = maestro.Controller("/dev/ttyAMA0")
gamepad = InputDevice('/dev/input/event0')

servo.setAccel(0, 4)
servo.setTarget(0, 6000)  # initial position

for event in gamepad.read_loop():
    currentPosition = servo.getPosition(0)
    print ("Current position: " + str(currentPosition))
    # user_input = raw_input()
    # if input == 'X':
    #     break
    if event.type == 1:
        if event.code == 293 and event.value == 1:
            print ("Top Right Button")
            servo.setTarget(0, currentPosition + 100)
        elif event.code == 292 and event.value == 1:
            print ("Top Left Button")
            servo.setTarget(0, currentPosition - 100)


servo.close
