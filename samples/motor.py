import maestro

servo = maestro.Controller("/dev/ttyAMA0")
servo.setAccel(0, 4)
servo.setAccel(1, 4)
servo.setAccel(2, 4)
servo.setAccel(3, 4)
while True:
    input = raw_input("Enter servo 0-3 + , + signal 0 - 9000 OR  X to quit:  ")
    if input == 'X':
        break
    inputArray = input.split(",")
    servoNo = int(inputArray[0])
    servoPosition = int(inputArray[1])
    servo.setTarget(servoNo, servoPosition)  # set servo to move to center position
servo.close
