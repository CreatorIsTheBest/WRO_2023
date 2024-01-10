In this project we're using two boards, an arduino uno and a raspberry pi 3B. Wich are comunicated throw a data bus using the GPIO in the raspberry pi and some of the input pins in arduino.
The raspberry is used for the processing of the image taken from a OV5647 camera with artificial vision.
Meanwhile the arduino it's going to be used for controlling the motion of the robot and the logic reasoning keeping in mind the inputs of all the sensors including the camera info send by the raspberry pi.

The programming language that we're going to be using in this project is python for the artificial vision in the raspberry pi and C++ in the arduino for the rest of the tasks.
