Modules needed:
```bash
pip install tensorflow
pip install keras
```


This will let us see and capture images from the drone by pressing the "c" key:

```Python
from droneblocks.DroneBlocksTello import DroneBlocksTello
import cv2
import time
import os

me = DroneBlocksTello()
#cap = cv2.VideoCapture(0)
me.connect(True)
print(me.get_battery())
me.streamon()


def ai_subframe(image, imgX, imgY):
    subframe = img[imgY:imgY+224, imgX:imgY+224].copy()
    image = cv2.rectangle(image,(imgX,imgY),(imgX+224,imgY+224),(255,0,140),2)

    return image, subframe

start_time = str(time.time()).split(".")[0]
count = 0
path = os.getcwd()

while True:
    img = me.get_frame_read().frame
    #img = cv2.resize(img, (360, 240))
    img, ai_image = ai_subframe(img, 80, 80)
    cv2.imshow("results", img)
    cv2.imshow("Ai Segment", ai_image)
    if cv2.waitKey(33) == ord('c'):
        # Save the images
        print("Saved File(s)! {0} and {1}".format("{0} Sub Image N-{1}.png".format(start_time, count), "{0} Whole Image N-{1}.png".format(start_time, count)))
        cv2.imwrite(os.path.join(path, "{0} Sub Image N-{1}.png".format(start_time, count)), ai_image)
        cv2.imwrite(os.path.join(path, "{0} Whole Image N-{1}.png".format(start_time, count)), img)

        count += 1 # increase count
```


After this, we need to use these images to create a Machine learning model that camn recognize different things. 

Once we're done with that, we can detect them using something like this:

```Python
from droneblocks.DroneBlocksTello import DroneBlocksTello
import cv2
import time
from tensorflow import keras
from keras._tf_keras.keras.models import load_model  # TensorFlow is required for Keras to work
import numpy as np

me = DroneBlocksTello()
#cap = cv2.VideoCapture(0)
me.connect(True)
print(me.get_battery())
me.streamon()



# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = load_model("keras_Model.h5", compile=False)
# Load the labels
class_names = open("labels.txt", "r").readlines()


def ai_subframe(image, imgX, imgY):
    subframe = img[imgY:imgY+224, imgX:imgY+224].copy()
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
    
    # Show the image in a window
    cv2.imshow("Webcam Image", ai_image)

    # Make the image a numpy array and reshape it to the models input shape.
    ai_image = np.asarray(ai_image, dtype=np.float32).reshape(1, 224, 224, 3)

    # Normalize the image array
    ai_image = (ai_image / 127.5) - 1

    # Predicts the model
    prediction = model.predict(ai_image)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    # Print prediction and confidence score
    print("Class:", class_name[2:], end="")
    print("Confidence Score:", str(np.round(confidence_score * 100))[:-2], "%")

    # Listen to the keyboard for presses.
    keyboard_input = cv2.waitKey(1)

    # 27 is the ASCII for the esc key on your keyboard.
    if keyboard_input == 27:
        break
```
