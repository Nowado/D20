#Takes declared number of pics and saves them as 1.jpg, 2.jpg...
from picamera import PiCamera
from time import sleep

#type(name)=str, name='abc.jpg'
def take_picture(name,delay=5):
    camera = PiCamera()
    camera.resolution = (1024, 768)
    camera.start_preview()
    for i in range(delay):
        print('Photo in ' + str(delay-i))
        sleep(1)
    camera.capture(name)
    camera.stop_preview()

#type(names)=[]
def capture_set(names,delay):
    for i in names:
            print('Takng photo '+str(i) +' out of set of '+str(len(names)))
            take_picture(str(i),delay)
temp=input('How many photos do you want to take?')
temp=range(int(temp))
names=[]
for i in temp:
    names.append(str(i)+'.jpg')

delay=int(input('How many seconds do you want between photos?'))

capture_set(names,delay)