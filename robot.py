#Ez lesz az a program, ahol a robot önjáró lesz, és a szenzor által mért értékek hatására változtat irányt, valamint ki is írja ezeket a folyadékkristályos kijelzőre


import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

robot1 = 23 #Motor1A, 16-os GPIO láb, IC: pin2, input2, zöld kábel
robot2 = 24 #Motor1B, 18-as GPIO láb, IC: pin7, input1, sárga kábel 
robot3 = 25 #Motor1E, 22-es GPIO láb, IC: pin1, enable, lila kábel
robot4 = 5  #Motor2A, 29-es GPIO láb, IC: pin10, input3, sárga kábel
robot5 = 6  #Motor2B, 31-es GPIO láb, IC: pin15, input4, zöld kábel
robot7 = 13 #Motor2E, 33-as GPIO láb, IC: pin9, enable, lila kábel

robot8 = 20 #Szenzor, TRIG, fehér kábel
robot9 = 21 #Szenzor, ECHO, szürke kábel

robot10 = 4  #LCD, LCD1_E, enable, 
robot11 = 26 #LCD, LCD2_RS, RS
robot12 = 17 #LCD, LCD2_D4, D4
robot13 = 27 #LCD, LCD3_D5, D5
robot14 = 22 #LCD, LCD4_D6, D6
robot15 = 12 #LCD, LCD5_D7, D7

GPIO.setup(robot1,GPIO.OUT)
GPIO.setup(robot2,GPIO.OUT)
GPIO.setup(robot3,GPIO.OUT)
GPIO.setup(robot4,GPIO.OUT)
GPIO.setup(robot5,GPIO.OUT)
GPIO.setup(robot6,GPIO.OUT)
GPIO.setup(robot7,GPIO.OUT)
GPIO.setup(robot8,GPIO.OUT)
GPIO.setup(robot9,GPIO.OUT)
GPIO.setup(robot10,GPIO.OUT)
GPIO.setup(robot11,GPIO.OUT)
GPIO.setup(robo12,GPIO.OUT)
GPIO.setup(robot13,GPIO.OUT)
GPIO.setup(robot14,GPIO.OUT)
GPIO.setup(robot15,GPIO.OUT)

#Előre haladás
GPIO.output(robot1,GPIO.HIGH)
GPIO.output(robot2,GPIO.LOW)
GPIO.output(robot3,GPIO.HIGH)
GPIO.output(robot4,GPIO.HIGH)
GPIO.output(robot5,GPIO.LOW)
GPIO.output(robot6,GPIO.HIGH)

#Hátra haladás
GPIO.output(robot1,GPIO.LOW)
GPIO.output(robot2,GPIO.HIGH)
GPIO.output(robot3,GPIO.HIGH)
GPIO.output(robot4,GPIO.LOW)
GPIO.output(robot5,GPIO.HIGH)
GPIO.output(robot6,GPIO.HIGH)

#Jobbra fordulás
GPIO.output(robot1,GPIO.LOW)
GPIO.output(robot2,GPIO.HIGH)
GPIO.output(robot3,GPIO.HIGH)
GPIO.output(robot4,GPIO.HIGH)
GPIO.output(robot5,GPIO.LOW)
GPIO.output(robot6,GPIO.HIGH)

#Balra fordulás
GPIO.output(robot1,GPIO.HIGH)
GPIO.output(robot2,GPIO.LOW)
GPIO.output(robot3,GPIO.HIGH)
GPIO.output(robot4,GPIO.LOW)
GPIO.output(robot5,GPIO.HIGH)
GPIO.output(robot6,GPIO.HIGH)

#Megállás
GPIO.output(robot3,GPIO.LOW)
GPIO.output(robot6,GPIO.LOW)








GPIO.cleanup()
