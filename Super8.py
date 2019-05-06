import RPi.GPIO as GPIO  # to interact with the camera
import time  # for the naming of the file
import os  # to execute linux commands

GPIO.setmode(GPIO.BCM)

GPIO.setup(2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(14, GPIO.OUT)
#video = (time.strftime("%y_%b_%d_%H_%M"))  # use date and time as filename, so we can store mutliple files
try:
    while True:
        GPIO.wait_for_edge(2, GPIO.FALLING)  # when you connect pin2 to ground it triggers the event
        GPIO.output(4, GPIO.HIGH)  # activate Super8 cam
        GPIO.output(14, GPIO.HIGH)
        video = (time.strftime("%y_%b_%d_%H_%M"))
        os.system("raspivid -w 1920 -h 1080 -fps 25 -o " + str(video) + ".h264 -t 30000")
        # record 30 sec video (30fps america / 25fps Europe)
        GPIO.output(14, GPIO.LOW) # deactivate Super8 cam
        os.system("MP4Box -add " + str(video) + ".h264 " + "/home/pi/Super8/" + str(video) + ".mp4")
        os.system("rm " + str(video) + ".h264")  # delete the original .h264 file
        GPIO.output(4, GPIO.LOW)
        # GPIO.output(14, GPIO.LOW) # deactivate Super8 cam
        print("finished converting")





except:
    GPIO.cleanup()
# if not make sure all the pullups are in a known state
