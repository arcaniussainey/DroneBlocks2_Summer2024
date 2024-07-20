

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
    img = cv2.resize(img, (360, 240))
    cv2.imshow("results", img)
    cv2.waitKey(1)
```
