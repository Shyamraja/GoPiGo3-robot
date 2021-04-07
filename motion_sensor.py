import time
from easygopigo3 import EasyGoPiGo3
gpg = EasyGoPiGo3()

motion_sensor = gpg3_obj.init_motion_sensor(“AD1”)
while True:
   if motion_sensor. motion_detected ():
   print(“Something is moving”)
else:
print(“Nothing”)
