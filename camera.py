from picamera import PiCamera
from time import sleep

camera = PiCamera(resolution=(1000, 800), framerate=40)
camera.iso = 400
camera.start_preview()
for i in range(8):
    sleep(2)
    camera.capture('/home/pi/Pictures/image%s.jpg' % i)
camera.stop_preview()
