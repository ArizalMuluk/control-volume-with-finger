# Volume Control Using Hand Gestures

## Description
This project is a volume control application that uses hand gesture detection to change the audio volume. Using the index finger and thumb, the user can turn down or turn up the volume by simply changing the distance between the two fingers. This application utilizes `OpenCV` and `Mediapipe` for image processing and `alsaaudio` to control the system volume.

## Features
- Hand detection using machine learning models.
- Real-time audio volume control based on the distance between the fingers.
- On-screen FPS (Frame Per Second) display.
- Volume bar graph showing current volume level.

## Prerequisites
Before running the application, make sure you have the following libraries installed:

- Python 3.x
- OpenCV
- Mediapipe
- NumPy
- alsaaudio
- FingerTrackModule (hand detection module)

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/username/repo.git
   cd repo```
2. Install the required libraries:
   ``bash
   pip install opencv-python numpy pyalsaaudio
   ```
3. Make sure you have the FingerTrackModule module. You may need to download or install it separately.

## How to use
1. Run the Python script:
```bash
python3 volume_control.py
```
2. Point your camera at your hand and use your index finger and thumb to control the volume:

- Fingers that are close together (< 25 pixels apart) will set the volume to minimum (0%).
- Fingers that are far apart (distance > 200 pixels) will set the volume to maximum (100%).
- The distance in between will adjust the volume proportionally.

3. Press q to exit the app.

## Contribution
If you would like to contribute, please create a pull request or open an issue for discussion.

# Note: This python program is only supported when run on linux OS!
