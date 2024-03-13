
Robot with Arduino, Raspberry Pi and Computer Vision using TensorFlow and OpenCV
This project details the creation of a robot controlled by Arduino and Raspberry Pi, equipped with 4 sensors, 2 DC motors, an L298N board, and programmed with TensorFlow and OpenCV on Raspberry Pi OS (previously Raspbian). The robot is powered by two 3.7V 18650 batteries connected to a battery holder.

Components Used
Arduino Uno
Raspberry Pi (supported models)
4 Sensors (e.g. ultrasonic sensors)
2 DC Motors
L298N motor controller board
Battery holder for 2 18650 batteries
Raspberry Pi compatible camera (e.g. Pi Camera)
Physical Connections
Arduino Uno and Raspberry Pi:

Connect the Raspberry Pi and the Arduino Uno using a USB cable.
Sensors:

Connect the sensors to the digital or analog pins of the Arduino Uno.
DC Motors:

Connect the DC motors to the output ports of the L298N board.
L298N:

Connect the L298N board to the Arduino Uno:
IN1 to Pin 2
IN2 to Pin 3
IN3 to Pin 4
IN4 to Pin 5
Connect the ENA and ENB pins to the PWM pins of the Arduino Uno.
Camera:

Connect the Raspberry Pi compatible camera to the camera port of the Raspberry Pi.
Feeding:

Connect the two 18650 batteries into the battery holder and connect the output to the power input of the L298N board.
Software installation
Raspberry Pi (Raspberry Pi OS):

Install TensorFlow and OpenCV on Raspberry Pi following the official instructions.
Make sure you have the necessary libraries to control the sensors and DC motors.
Arduino Uno:

Load the code necessary to read the sensor data and control the DC motors.
Project execution
Connect all physical parts according to the connections described above.
Turn on the Raspberry Pi and make sure it is connected to the network.
Run the Python script containing the TensorFlow model to process camera images and make vision-based decisions.
Observe how the robot moves and reacts according to the images captured by the camera and processed by TensorFlow and OpenCV.
Adjust the code as necessary to improve the performance and functionality of the robot.
Additional notes
Make sure you have the necessary libraries installed on the Raspberry Pi to work with TensorFlow, OpenCV, and to control the sensors and DC motors.
You can adjust and customize the code to implement different behaviors based on the robot's vision.
Remember to keep safety considerations in mind when working with motors and electrical components.
This is a basic project to demonstrate the integration of various components. More sensors, actuators, and functions can be added to expand the robot's capabilities.
This README provides an overview of the robot project with Arduino, Raspberry Pi, TensorFlow and OpenCV. For specific code and configuration details, please refer to the corresponding files and documentation in the project repository.





