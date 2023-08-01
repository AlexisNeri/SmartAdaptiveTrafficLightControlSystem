# Traffic Management System using Car Detection and Decision-Making

## Overview
This project implements a Traffic Management System using computer vision techniques to detect vehicles and make intelligent decisions to control traffic lights at an intersection. The system consists of four main modules:

1. `main.py`: This module is the entry point of the Traffic Management System. It captures video streams from two different street cameras and processes them to count the number of vehicles approaching the intersection. The vehicle counts and inference times are logged to an Excel file. The module also provides options to display the processed video frames and save them to disk.

2. `car_counter.py`: This module handles vehicle detection using YOLO (You Only Look Once) object detection. It takes a frame from a video stream as input and detects vehicles in it. The module counts the number of vehicles and returns the count along with the annotated frame.

3. `decision_maker.py`: This module makes intelligent decisions based on the vehicle counts from both street cameras and the elapsed time since the last traffic light change. It uses GPIO pins to control the traffic lights, switching the lights at appropriate intervals to optimize traffic flow at the intersection.

4. `utils.py`: This module provides utility functions for the Traffic Management System. It includes functions to convert videos to frames, keep selected nth files in a directory, and relabel data to match label classes in third-party datasets.

## Requirements
- Python 3.10+
- OpenCV (cv2)
- imutils
- xlsxwriter
- cvlib (YOLO-based object detection)
- gpiozero (for controlling the traffic lights)

## Installation
1. Clone this repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.

## Usage
1. Connect two street cameras to the computer running the Traffic Management System.
2. Update the video sources in `main.py` to point to the streams from the cameras.
3. Run the Traffic Management System using the command: `python main.py`.

## Customization
- You can adjust the time intervals and decision logic in `decision_maker.py` to suit your specific traffic management requirements.
- Modify the YOLO weights, configurations, and class names in `car_counter.py` to improve vehicle detection accuracy for your camera setup.
- Use the utility functions provided in `utils.py` to preprocess video frames, keep selected files, and relabel data if needed.

## Notes
- Ensure that the GPIO pins are correctly connected to the traffic lights and have appropriate permissions for the user running the program.
- This project was executed in a Raspberry Pi 4 Model B.
- If needed, both the frames and the labels used for training are available under `dataset` folder.

Feel free to contribute to this project by submitting pull requests with enhancements or bug fixes.

**Disclaimer**: This project is meant for educational and experimental purposes. Use it responsibly and ensure compliance with traffic laws and safety regulations.
