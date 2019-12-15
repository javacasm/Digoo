import digoo
import config
import time

d = digoo.Digoo(config.CAMERA_IP)
print('starting camera with IP '+config.CAMERA_IP)

d.play_video()
print('Playing video')

time.sleep(1)
print('moving to the left')
d.move_left()

time.sleep(1)
print('moving to the right')
d.move_right()

time.sleep(1)
print('moving up')
d.move_up()

time.sleep(1)
print('moving down')
d.move_down()

time.sleep(5)

d.take_snapshot('~/image.jpg')

print('Stop video')
d.stop_video()

