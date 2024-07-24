import sys

sys.path.append("..")

import cv2
from cv2 import aruco
import imutils

window_name = "MouseFollow"
original_frame = None

# Make a function that finds the center of the ArUco marker and the mouse pointer
def mouse_move(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        frame = original_frame.copy()

        # call the detectMarkers function from the OpenCV ArUco package
        corners, ids, rejectedImgPoints = aruco_detector.detectMarkers(frame)

        # Find the center of the ArUco marker
        # Start by getting the corners of the marker
        Corner1 = corners[0][0][0]
        Corner3 = corners[0][0][2]

        # Find the average of two opposite corners to find the center
        marker_center_x = (Corner1[0] + Corner3[0]) / 2
        marker_center_y = (Corner1[1] + Corner3[1]) / 2

        # Make a circle at the center of the ArUco marker
        cv2.circle(frame, center=(int(marker_center_x), int(marker_center_y)), radius=8, color=(0, 255, 0), thickness=-1)
        
        # Find the distance between the ArUco marker and the mouse
        # This will be helpful for future activities
        dx = marker_center_x - x
        dy = marker_center_y - y

        # Make a circle where the mouse is
        cv2.circle(frame, center=(x, y), radius=8, color=(255, 255, 0), thickness=-1)

        # Use OpenCV to get information about the ArUco markers
        aruco.drawDetectedMarkers(frame, corners, ids)
        cv2.imshow(window_name, frame)


if __name__ == '__main__':

    # Set up the ArUco detection
    aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_ARUCO_ORIGINAL)
    aruco_params = aruco.DetectorParameters()
    aruco_detector = cv2.aruco.ArucoDetector(aruco_dict, aruco_params)

    # Read in an image
    # resize so it is easier to view
    original_frame = cv2.imread('test_porch_2.JPG')
    original_frame = imutils.resize(original_frame, width=800)
    frame = original_frame.copy()

    # Display the resulting frame
    cv2.imshow(window_name, frame)

    # register a callback function with OpenCV
    # when there is any mouse activity
    cv2.setMouseCallback(window_name, mouse_move)

    # The program will close when any key is pressed
    cv2.waitKey(0)