import time
from easygopigo3 import EasyGoPiGo3
gpg = EasyGoPiGo3()

my_distance_sensor = gpg.init_distance_sensor()

while True:
    print("Distance sensor readings are: {} mm ".format(my_distance_sensor.read_mm()))