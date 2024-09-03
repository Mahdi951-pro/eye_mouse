# Eye-Controlled Mouse using OpenCV, MediaPipe, and PyAutoGUI

This project implements an eye-controlled mouse using Python, OpenCV, MediaPipe, and PyAutoGUI. The system tracks the user's eye movements through a webcam, allowing the user to move the mouse cursor and perform clicks by blinking.

## Features

- **Real-time Eye Tracking**: Uses the webcam to detect and track eye movements.
- **Cursor Control**: Maps eye movements to screen coordinates to move the mouse cursor.
- **Blink Detection**: Detects blinks to trigger mouse clicks.
- **Interactive Display**: Shows the processed video feed with visual markers for detected facial landmarks.

## Prerequisites

Make sure you have the following Python packages installed:

- `opencv-python`
- `mediapipe`
- `pyautogui`

You can install them using pip:

bash
pip install opencv-python mediapipe pyautogui
Usage
Clone the Repository:

bash
Copy code
git clone https://github.com/yourusername/eye-controlled-mouse.git
cd eye-controlled-mouse
Run the Script:

Execute the Python script:

bash
Copy code
python eye_controlled_mouse.py
This will start the webcam and the real-time eye-tracking system.

Control Your Mouse:

Move your eyes to control the mouse cursor.
Blink to perform a mouse click.
How It Works
Face Mesh Detection: Uses MediaPipe's FaceMesh to detect 468 facial landmarks in real-time.
Eye Region Tracking: Focuses on specific landmarks around the eyes to determine the eye position and movement.
Cursor Movement: Maps the normalized eye coordinates to the screen dimensions and moves the cursor using PyAutoGUI.
Blink Click: Calculates the vertical distance between two eye landmarks to detect blinks and trigger mouse clicks.
Demonstration

Customization
You can modify the threshold for blink detection, the landmarks used for tracking, and other parameters to suit your needs.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
OpenCV
MediaPipe
PyAutoGUI
Contributing
Contributions are welcome! Please fork this repository and submit a pull request with your changes.

Contact
If you have any questions or suggestions, feel free to reach out:

GitHub: Mahdi951-pro


YouTube: https://www.youtube.com/channel/UCFqZmvEYIL7xV637tlrd8qQ
css
Copy code

This `README.md` file provides an overview of the project, instructions for setup and usage, and 
