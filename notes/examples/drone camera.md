This is a basic script or interacting with the Tello's Camera. You'll notice that there is a section to resize the image, which is commented out. Why might we want to resize the camera-images? Why might we not want to? WHat are the benefits of a larger and smaller camera view respectively. 

```Python
from droneblocks.DroneBlocksTello import DroneBlocksTello
import cv2

me = DroneBlocksTello()
#cap = cv2.VideoCapture(0)
me.connect(True)
print(me.get_battery())
me.streamon()


while True:
    img = me.get_frame_read().frame
    #img = cv2.resize(img, (360, 240))
    cv2.imshow("results", img)
    cv2.waitKey(1)
```


Also ask yourself, are your images noise-free, or are you able to see noise patterns within your camera view? What does this mean for data collection using the Tello cameras?
