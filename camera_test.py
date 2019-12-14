import digoo
import config
import time

d = digoo.Digoo(config.CAMERA_IP)
print('starting camera with IP '+config.CAMERA_IP)

print('moving to the left')
d.move_left()

print('moving to the left')
d.move_left()

print('moving up')
d.move_up()

print('moving down')
d.move_down()

d.play_video()
print('Playing video')
time.sleep(10)

d.take_snapshot('image.jpg')

print('Stop video')
d.stop_video()

