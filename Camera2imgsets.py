#Takes declared number of pics and saves them as 1.jpg, 2.jpg...
from picamera import PiCamera
from time import sleep

camera = PiCamera()

def take_pictures(d,sets_delay,photo_delay,photo_per_side):
    camera.resolution = (2048, 2048)
    for side in range(d):
        for j in range(sets_delay):
            print('New set of '+str(side+1) +' side in ' + str(sets_delay - j))
            sleep(1)
        for photo in range(photo_per_side):
            for i in range(photo_delay):
                print('Photo in ' + str(photo_delay-i))
                sleep(1)
            camera.capture(str(side+1)+'_'+str(photo)+'.jpg', use_video_port=True)

#def capture_set(names,delay):
#    for i in names:
#            print('Takng photo '+str(i) +' out of set of '+str(len(names)))
#            take_picture(str(i),delay)


d=int(input('How many sides does your dice have?'))
photo_per_side=int(input('How many photos do you want to take per side?'))

sets_delay=int(input('How many seconds do you want between sets?'))
photo_delay=int(input('How many seconds do you want between photos?'))


take_pictures(d,sets_delay,photo_delay,photo_per_side)