from evdev import InputDevice, categorize, ecodes
gamepad = InputDevice('/dev/input/event0')
print (gamepad)
for event in gamepad.read_loop():
    print (event)
	print (event.at)
	print (event.code)
	print (event.type)
	print ("-------")

	if event.type == 3:
		if event.code == 0 and event.value == 255:
			whatHappened = "Right Direction"
		elif event.code == 0 and event.value == 0:
			whatHappened = "Left Direction"
		elif event.code == 1 and event.value == 255:
			whatHappened = "Down Direction"
		elif event.code == 1 and event.value == 0:
			whatHappened = "Up Direction"

	elif event.type == 1:
		if event.code == 293 and event.value == 1:
			whatHappened = "Top Right Button"
		elif event.code == 292 and event.value == 1:
			whatHappened = "Top Left Button"

		elif event.code == 289 and event.value == 1:
			whatHappened = "A Button"
		elif event.code == 290 and event.value == 1:
			whatHappened = "B Button"
		elif event.code == 288 and event.value == 1:
			whatHappened = "X Button"
		elif event.code == 291 and event.value == 1:
			whatHappened = "Y Button"

	print (whatHappened)

