# Challenge: Reading Drone LEDs
We now know that we can process images with OpenCV to remove noise, reduce blur, change the size of an image, and find features within an image. The Tello drones have the ability to attach an LED matrix to their top, and display custom images to it. Is it possible for a Drone's camera to read the LED Matrix? And if so, does this mean we can transfer data between drones? 

# Challenge Requirements 
- Process drone images until they're usable
- Read another drone's LED matrix at some distance
- Use the information on another drone's LED matrix to communicate (use as ArUco marker, Rock/Paper/Scissors indicator, status message, or classification of drone)

See if you can develop a protocol for the communication on information between drones. 
