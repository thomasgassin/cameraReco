from picamera import PiCamera
from time import sleep

camera = PiCamera()
#camera.resolution = (300, 200)
camera.preview_fullscreen=False 
camera.preview_window=(620, 320, 640, 520) 
camera.start_preview()
sleep(5)
camera.stop_preview()