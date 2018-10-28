from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

robot1A = 23
robot1B = 24
robot1E = 25 

robot2A = 5
robot2B = 6
robot2E = 13

GPIO.setup(robot1A,GPIO.OUT)
GPIO.setup(robot1B,GPIO.OUT)
GPIO.setup(robot1E,GPIO.OUT)
GPIO.setup(robot2A,GPIO.OUT)
GPIO.setup(robot2B,GPIO.OUT)
GPIO.setup(robot2E,GPIO.OUT)

#Előre
GPIO.output(robot1A,GPIO.HIGH)
GPIO.output(robot1B,GPIO.LOW)
GPIO.output(robot1E,GPIO.HIGH)
GPIO.output(robot2A,GPIO.HIGH)
GPIO.output(robot2B,GPIO.LOW)
GPIO.output(robot2E,GPIO.HIGH)

#Hátra
GPIO.output(robot1A,GPIO.LOW)
GPIO.output(robot1B,GPIO.HIGH)
GPIO.output(robot1E,GPIO.HIGH)
GPIO.output(robot2A,GPIO.LOW)
GPIO.output(robot2B,GPIO.HIGH)
GPIO.output(robot2E,GPIO.HIGH)

#Jobbra
GPIO.output(robot1A,GPIO.LOW)
GPIO.output(robot1B,GPIO.HIGH)
GPIO.output(robot1E,GPIO.HIGH)
GPIO.output(robot2A,GPIO.HIGH)
GPIO.output(robot2B,GPIO.LOW)
GPIO.output(robot2E,GPIO.HIGH)

#Balra
GPIO.output(robot1A,GPIO.HIGH)
GPIO.output(robot1B,GPIO.LOW)
GPIO.output(robot1E,GPIO.HIGH)
GPIO.output(robot2A,GPIO.LOW)
GPIO.output(robot2B,GPIO.HIGH)
GPIO.output(robot2E,GPIO.HIGH)

#Megállás
GPIO.output(robot1E,GPIO.LOW)
GPIO.output(robot2E,GPIO.LOW)

GPIO.cleanup()
