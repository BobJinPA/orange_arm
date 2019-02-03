# This code is teaching how to read events from the USB controller

from evdev import InputDevice, categorize, ecodes

gamepad = InputDevice('/dev/input/event0')
print (gamepad)

for event in gamepad.read_loop():
    # print ("TIMESTAMP: " + str(event.timestamp()))
    # print ("CODE: " + str(event.code))
    # print ("TYPE: " + str(event.type))
    # print ("VALUE: " + str(event.value))
    # print ("-------")
    whatHappened = "I don't know"
    if event.type == 3:
        if event.code == 0 and event.value == 255:
            print ("Right Direction")
        elif event.code == 0 and event.value == 0:
            print ("Left Direction")
        elif event.code == 1 and event.value == 255:
            print ("Down Direction")
        elif event.code == 1 and event.value == 0:
            print ("Up Direction")

    elif event.type == 1:
        if event.code == 293 and event.value == 1:
            print ("Top Right Button")
        elif event.code == 292 and event.value == 1:
            print ("Top Left Button")

        elif event.code == 289 and event.value == 1:
            print ("A Button")
        elif event.code == 290 and event.value == 1:
            print ("B Button")
        elif event.code == 288 and event.value == 1:
            print ("X Button")
        elif event.code == 291 and event.value == 1:
            print ("Y Button")
