
This will let us see and capture images from the drone by pressing the "c" key:

```Python
from droneblocks.DroneBlocksTello import DroneBlocksTello
import cv2
import time

me = DroneBlocksTello()
#cap = cv2.VideoCapture(0)
me.connect(True)
print(me.get_battery())
me.streamon()


def ai_subframe(image, imgX, imgY):
    subframe = crop_img = img[imgY:imgY+224, imgX:imgY+224]
    image = cv2.rectangle(image,(imgX,imgY),(imgX+224,imgY+224),(255,0,140),2)

    return image, subframe

start_time = str(time.time()).split(".")[0]
count = 0

while True:
    img = me.get_frame_read().frame
    #img = cv2.resize(img, (360, 240))
    img, ai_image = ai_subframe(img, 80, 80)
    cv2.imshow("results", img)
    cv2.imshow("Ai Segment", ai_image)
    if cv2.waitKey(3) == ord('c'):
        # Save the images
        cv2.imwrite("{0} Sub Image N-{1}.png".format(start_time, count), ai_image)
        cv2.imwrite("{0} Whole Image N-{1}.png".format(start_time, count), img)

        count += 1 # increase count
```
