#https://github.com/carolinedunn/timelapse

from picamera import PiCamera
from os import system
import datetime
from time import sleep

minutes = 30 #set this to the number of minutes you wish to run your timelapse camera
secondsInterval = 5 #number of seconds delay between each photo taken
fps = 30 #frames per second timelapse video

numPhotos = int((minutes*60)/secondsInterval) #number of photos to take
print("number of photos to take = ", numPhotos)

dateRaw = datetime.datetime.now()
dateTimeFormat = dateRaw.strftime("%Y-%m-%d_%H:%M")
print("RPi started taking photos for your timelapse at: " + dateTimeFormat)


camera = PiCamera()
camera.resolution = (1920,1080)
camera.rotation = 90
system('rm /home/pi/Pictures/timelapse/*.jpg') #delete all photos in the Pictures folder before timelapse start

for i in range(numPhotos):
    camera.capture('/home/pi/Pictures/timelapse/image_{}.jpg'.format(i))
    sleep(secondsInterval)
    
    
print("Done taking photos.")
print("Please standby as your timelapse video is created.")

#system('ffmpeg -framerate 30 -pattern_type glob -i "/home/pi/Pictures/timelapse/*.jpg" -s:v 1920x1080 -c:v libx264 -crf 25 -pix_fmt yuv422p /home/pi/Videos/timelapse/{}.mp4'.format(dateTimeFormat))
#ffmpeg -r 30 -start_number 0 -pattern_type glob -i "/home/pi/Pictures/timelapse/*.jpg" -s hd1080 -vcodec libx264 -crf 18 -preset medium /home/pi/Videos/timelapse/test.mp4
#system('ffmpeg -r 30 -start_number 0000000 -pattern_type glob -i "/home/pi/Pictures/timelapse/*.jpg" -i image%06d.jpg -s hd1080 -vcodec libx264 -crf 18 -preset medium /home/pi/Videos/timelapse/{}.mp4'.format(dateTimeFormat))

system('ffmpeg -r 25 -start_number 0 -i "/home/pi/Pictures/timelapse/image_%d.jpg" -s hd1080 -vcodec libx264 -crf 18 -preset medium /home/pi/Videos/timelapse/{}.mp4'.format(dateTimeFormat))

print('Timelapse video is complete. Video saved as /home/pi/Videos/timelapse/{}.mp4'.format(dateTimeFormat))