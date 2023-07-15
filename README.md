# Face and Eye Detection

## Purpose

The purpose of the Face and Eye Detection project is to demonstrate the capability of OpenCV in detecting faces and eyes in images or video frames. It utilizes pre-trained Haar Cascade classifiers to accurately identify and locate faces and eyes within an image or video stream.

## Intended Audience

This project is intended for individuals interested in computer vision, image processing, and facial recognition. It can be used as a learning resource for understanding the fundamentals of face and eye detection algorithms and how to implement them using OpenCV.

## Requirements

To run the Face and Eye Detection project, the following requirements must be met:

1. Python: The project is implemented in Python, so a Python interpreter is required. Python 3.x is recommended.

2. NumPy: NumPy is a fundamental package for scientific computing with Python. It is used in this project for array manipulation and mathematical operations. Install NumPy using the command `pip install numpy`.

3. OpenCV: OpenCV is a popular computer vision library that provides various functions and algorithms for image and video processing. Install OpenCV using the command `pip install opencv-python`.

## Usage

To use the Face and Eye Detection project, follow these steps:

1. Clone or download the project repository.

2. Ensure that Python, NumPy, and OpenCV are installed.

3. Run the Python script `face_eye_detection.py` using a Python interpreter.

4. The script will access your webcam and start detecting faces and eyes in real-time.

5. The script will process the file and display the output, highlighting detected faces and eyes.

6. Press any key to exit the program.

## Additional Notes

- The project utilizes pre-trained Haar Cascade classifiers for face and eye detection. These classifiers are included in the OpenCV library under the `cv.data.haarcascades` module.

- The project demonstrates how to draw rectangles around detected faces and eyes using the `cv.rectangle()` function.

- The project can handle both images and video files as input. For video files, it processes each frame individually.

- The project showcases the usage of OpenCV functions such as `cv.imread()`, `cv.imshow()`, `cv.CascadeClassifier()`, and `cv.waitKey()`.

- Feel free to experiment with different images or video files to observe the accuracy and performance of the face and eye detection algorithm.

- For more information on the underlying concepts and techniques, refer to the OpenCV documentation and relevant resources on computer vision and image processing.