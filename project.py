from picamera import PiCamera
from gpiozero import Buzzer
from gpiozero import LED
import os
from twilio.rest import Client
from time import sleep

camera = PiCamera()
buzzer = Buzzer(23)
white_led = LED(17)
#~ camera.start_preview()
#~ sleep(5)
#~ camera.capture('/home/pi/Desktop/motion')
#~ camera.stop_preview()

import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)         #Read output from PIR motion sensor
GPIO.setup(17, GPIO.OUT)         #LED output pin
while True:
		i=GPIO.input(4)
		if i==0:                 #When output from motion sensor is LOW
			print ("NO_Motion_detected",i)
			GPIO.output(17, 0)  #Turn OFF LED
			sleep(0.5)
		elif i==1:               #When output from motion sensor is HIGH
			print ("Motion_detected",i)
			print ("Image_Capturing",i)
			camera.capture('/home/pi/Desktop/motion/image.jpg')
			buzzer.on()
            GPIO.output(4, 1)  #Turn ON LED
            account_sid = os.environ['AC4230e6c190a67c5fdc2009a5b2a5656c']
            auth_token = os.environ['781490611e67c5ee39f2e6be7f423804']
            client = Client(account_sid, auth_token)

            message = client.api.account.messages.create(
                                body="Animal Detected.",
                                from_='+12052933174',
                                to='+916299225767'
                            )
            sleep(0.5)
            buzzer.off()
            sleep(0.5)