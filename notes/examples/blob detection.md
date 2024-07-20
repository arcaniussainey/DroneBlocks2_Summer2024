This example outlines blob detection using parameters supplied to the SimpleBlobDetector from OpenCV. This allows us to detect and mark blobs (masses of color) in an image by looking at connected pixel groups, and evaluating the shape, size, area, and circularity of the shape the group makes. We give an example script whose parameters can be easily changed out, as well as an example image. Ensure to have the image in the workspace, on the space directory level as the script, with the same name. The example should draw red circles around blobs, with the size corresponding to the detected blob. 

Here are the criteria and their meanings (source: OpenCV Docs):
 - Color: Compares the intensity of a binary (Black/White) image
 - Area: Extracted blobs will have an area between minArea (inclusive) and maxArea (exclusive)
 - Circularity: How circular something is. Extracted blobs will be between minArea (inclusive) and maxArea (exclusive) This is calculated by measuring the irregularity of the perimeter.
 - Inertia ratio: This is the ratio of min to max inertia. Inertia is movement, so this measures how oval shaped a blob is (it's moving directionally). Extracted blobs will have a ratio between minIntertiaRatio (inclusive) and maxIntertiaRatio (exclusive)
 - By convexity: This refers to the concaveness of a shape, or having arc-like indents. Pacman is a circle with a convex mouth. Extracted blobs have a circularity between minCircularity (inclusive) and maxIntertia (exclusive):

![BlobTest](https://github.com/user-attachments/assets/c6f3df51-4931-408c-ad59-907462a4056a)


Note that this image is somewhat noisy (faint miscoloration of white pixels/black pixels) due to the compression of the jpeg algorthim. How could we address that? What filter might we use in a condition like this? The SimpleBlobDetector actually performs filtering for us, but it's important to think about how we would go about this. 


```Python
#!/usr/bin/python

# Standard imports
import cv2
import numpy as np;

# Read image
im = cv2.imread("blob.jpeg")

# Setup SimpleBlobDetector parameters.
params = cv2.SimpleBlobDetector_Params()

# Change thresholds
# Threshholds are used to convert a source image into a binary image for further processing
params.minThreshold = 1
params.maxThreshold = 255


# Filter by Area.
params.filterByArea = False
params.minArea = 1500

# Filter by Circularity
params.filterByCircularity = True
params.minCircularity = 0.1

# Filter by Convexity
params.filterByConvexity = False
params.minConvexity = 0.87

# Filter by Inertia
params.filterByInertia = True
params.minInertiaRatio = 0.01

# Create a detector with the parameters
# OLD: detector = cv2.SimpleBlobDetector(params)
detector = cv2.SimpleBlobDetector_create(params)


# Detect blobs.
keypoints = detector.detect(im)

# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures
# the size of the circle corresponds to the size of blob

im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Show blobs
cv2.imshow("Keypoints", im_with_keypoints)
cv2.imshow("No Keypoints", im)
cv2.waitKey(0)
```

Target Images:

![image](https://github.com/user-attachments/assets/c150f20b-0360-43b6-8b05-67c1a395414d)
