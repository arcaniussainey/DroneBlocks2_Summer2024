import sys

sys.path.append("..")

import cv2
from cv2 import aruco
import imutils

if __name__ == '__main__':

    # Set up the ArUco detection
    aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_ARUCO_ORIGINAL)
    aruco_params = aruco.DetectorParameters()
    aruco_detector = cv2.aruco.ArucoDetector(aruco_dict, aruco_params)

    # Read in an image
    # resize so it is easier to view
    image = cv2.imread('test_porch_2.JPG')
    image = imutils.resize(image, width=800)

    # call the detectMarkers function from the OpenCV ArUco package
    corners, ids, rejectedImgPoints = aruco_detector.detectMarkers(image)

    # Print the ids and the corners to the terminal 
    for id in ids:
        print(id)

    print(corners)
    for corner in corners:
        print(corner)

    # Retrieve the actual values to use later
    # notice the awkward mutliple indexing to get values
    ID = ids[0][0]
    Corner1 = corners[0][0][0]
    Corner2 = corners[0][0][1]
    Corner3 = corners[0][0][2]
    Corner4 = corners[0][0][3]

    print("------ ArUco Marker Details -------")
    print(ID)
    print(Corner1)
    print(Corner2)
    print(Corner3)
    print(Corner4)

    # Use OpenCV to draw box around the ArUco marker
    outputImage = image.copy()
    aruco.drawDetectedMarkers(outputImage, corners, ids)
    cv2.imshow('ArUco.detect_markers', outputImage)

    # Wait until any key is pressed to exit
    cv2.waitKey(0)