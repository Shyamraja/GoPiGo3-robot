from flask import Flask, render_template, Response, request
from camera import VideoCamera
import time
import threading
import os

python_camera = VideoCamera()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') 
    
def generate(video_camera):
    while True:
        gpg.forward()
        camera_frame = video_camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + camera_frame + b'\r\n\r\n')

@app.route('/show_video_feed')
def show_video_feed():
    return Response(generate(python_camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':

    app.run(host='0.0.0.0', debug=False)
    


