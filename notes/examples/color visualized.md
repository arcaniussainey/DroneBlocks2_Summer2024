This demo will allow you to see the HSV colors. To use it, you only need to change the values in ```col_1``` and ```col_2```. These are Hue, Saturation, Value values. You can use a number from 0 to 255 and it represents the percentage in that category (0 is 0%, 255 is 100%). If you want to calculate the percentage value from a number between 0-255 you can divide the number you choose by 255 and multiply by 100. Once you put in your number, the code will convert them to the BGR color space, and then display both images. 

```Python
import numpy as np
import cv2

# Change these:
col_1 = [0,200,100]
col_2 = [250, 100, 100]

color_one = cv2.cvtColor(np.full((150, 150, 3), np.array(col_1), dtype=np.uint8), cv2.COLOR_HSV2BGR)
color_two = cv2.cvtColor(np.full((150, 150, 3), np.array(col_2), dtype=np.uint8), cv2.COLOR_HSV2BGR)

cv2.imshow("Color 1", color_one)
cv2.imshow("Color 2", color_two)

cv2.waitKey(0)
```
