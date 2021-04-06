import cv2
from imutils.video.pivideostream import PiVideoStream
import imutils
import time

class VideoCamera(object):
    #Construct 
    def __init__(self):
        self.video = PiVideoStream().start()
        time.sleep(2.0)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        camframe = self.video.read()
        ret, jpeg = cv2.imencode('.jpg', camframe)
        return jpeg.tobytes()