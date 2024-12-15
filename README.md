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
2. Instal library yang dibutuhkan:
   ```bash
   pip install opencv-python numpy pyalsaaudio
   ```
3. Pastikan Anda memiliki modul FingerTrackModule. Anda mungkin perlu mengunduh atau menginstalnya secara terpisah.

## Cara Menggunakan
1. Jalankan skrip Python:
```bash
python3 volume_control.py
```
2. Arahkan kamera Anda ke tangan dan gunakan jari telunjuk dan ibu jari untuk mengontrol volume:

-Jari yang berdekatan (jarak < 25 piksel) akan mengatur volume ke minimum (0%).
-Jari yang berjauhan (jarak > 200 piksel) akan mengatur volume ke maksimum (100%).
-Jarak di antara keduanya akan mengatur volume secara proporsional.

3. Tekan q untuk keluar dari aplikasi.


