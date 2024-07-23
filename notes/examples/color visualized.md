This demo will allow you to see the HSV colors:

```Python
import numpy as np
import cv2

col_1 = [0,200,100]
col_2 = [250, 100, 100]

color_one = cv2.cvtColor(np.full((150, 150, 3), np.array(col_1), dtype=np.uint8), cv2.COLOR_HSV2BGR)
color_two = cv2.cvtColor(np.full((150, 150, 3), np.array(col_2), dtype=np.uint8), cv2.COLOR_HSV2BGR)

cv2.imshow("Color 1", color_one)
cv2.imshow("Color 2", color_two)

cv2.waitKey(0)
```
