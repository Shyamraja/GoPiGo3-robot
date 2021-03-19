import time
from easygopigo3 import EasyGoPiGo3
gpg = EasyGoPiGo3()

print("Move the robot for 100 cm and stop.")
gpg.drive_cm(100, True)
time.sleep(3)

print("Move in a rectangular path.")
length = 30
for i in range(4)
gpg.drive_cm(length)
gpg.turn_degrees(90)
time.sleep(1)

print("Move the robot Forward for 5 seconds")
gpg.forward()
time.sleep(2)

print("Turn left for 3 seconds and stop")
gpg.left()
time.sleep(1)

print("Stop!")
gpg.stop()
print("Done")


