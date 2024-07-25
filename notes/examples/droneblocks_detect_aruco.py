from droneblocks.DroneBlocksTello import DroneBlocksTello
import cv2
from cv2 import aruco
import numpy as np
import time
import keyboard
import threading

def get_video(tello):
    tello.streamon()
    # Set up the ArUco detection
    aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_ARUCO_ORIGINAL)
    aruco_params = aruco.DetectorParameters()
    aruco_detector = cv2.aruco.ArucoDetector(aruco_dict, aruco_params)

    while program_running:
        global img
        img = tello.get_frame_read().frame
        img = cv2.resize(img, (360, 240))
        
        # Use ArUco detection
        corners, ids, rejectedImgPoints = aruco_detector.detectMarkers(img)
        aruco.drawDetectedMarkers(img, corners, ids)
      
        cv2.imshow("Image", img) 
        cv2.waitKey(1)

# Start here!
if __name__ == '__main__':
    tello = DroneBlocksTello()
    tello.connect()
    global program_running
    program_running = True
    last_time = time.time()
    current_time = time.time()

    video = threading.Thread(target=get_video, args=(tello,))

    video.start()

    tello.takeoff()

    while True:
        key = keyboard.read_key()

        if key == "w":
            tello.fly_forward(20, "cm")
        elif key == "q":
            tello.rotate_counter_clockwise(15)
        elif key == "s":
            tello.fly_backward(20, "cm")
        elif key == "e":
            tello.rotate_clockwise(15)
        elif key =="l":
            tello.land()
            break
        
    program_running = False
    cv2.destroyAllWindows()

    