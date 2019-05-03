#Takes declared number of pics and saves them as 1.jpg, 2.jpg...
from picamera import PiCamera
from time import sleep

camera = PiCamera()

def timer_pictures(d,sets_delay,photo_delay,photo_per_side):
    camera.resolution = (1024, 1024)
    for side in range(d):
        for j in range(sets_delay):
            print('New set of '+str(side+1) +' side in ' + str(sets_delay - j))
            #a=input()
            sleep(1)
        for photo in range(photo_per_side):
            for i in range(photo_delay):
                print('Photo in ' + str(photo_delay-i))
                sleep(1)
                #a=input()
            camera.capture(str(side+1)+'_'+str(photo)+'.jpg', use_video_port=True)

def manual_pictures(d,photo_per_side):
	camera.resolution = (1024, 1024)
	for side in range(d):
		print('New set of '+str(side+1))
        a=input()
        for photo in range(photo_per_side):
            a=input()
            camera.capture(str(side+1)+'_'+str(photo)+'.jpg', use_video_port=True)

#def capture_set(names,delay):
#    for i in names:
#            print('Takng photo '+str(i) +' out of set of '+str(len(names)))
#            take_picture(str(i),delay)

mode = input('[t]imer or [m]anual?')
if mode == 't':
	d=int(input('How many sides does your dice have?'))
	photo_per_side=int(input('How many photos do you want to take per side?'))

	sets_delay=int(input('How many seconds do you want between sets?'))
	photo_delay=int(input('How many seconds do you want between photos?'))


	timer_pictures(d,sets_delay,photo_delay,photo_per_side)

if mode == 'm':
	d=int(input('How many sides does your dice have?'))
	photo_per_side=int(input('How many photos do you want to take per side?'))
	manual_pictures(d,photo_per_side)
	