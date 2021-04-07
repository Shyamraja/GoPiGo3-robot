import time
from easygopigo3 import EasyGoPiGo3
gpg = EasyGoPiGo3()

try:
    my_linefollower = gpg.init_line_follower()
    time.sleep(0.1)
except:
    print("the line follower is not responding")
    time.sleep(0.2)
    exit()
 my_linefollower.read_position()
 my_linefollower.read_position()

 gpg.forward()
 while True:
     if my_linefollower.read_position() == 'center':
         print("Robot moving forward") 
         gpg.forward()
     if my_linefollower.read_position() == 'left':
         print("Robot moving left") 
         gpg.left()
    if my_linefollower.read_position() == 'right':
         print("Robot moving right") 
         gpg.right()

 gpg.stop()
     
 