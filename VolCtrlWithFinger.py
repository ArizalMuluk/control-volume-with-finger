import math
import time

import alsaaudio as ad
import cv2
import numpy as np

import FingerTrackModule as ftm

wCam, hCam = 720, 560

cTime = 0
pTime = 0

cap = cv2.VideoCapture(0)
cap.set(propId=3, value=wCam)
cap.set(propId=4, value=hCam)


detector = ftm.handsDetect(detectCon=0.9)


mixer = ad.Mixer()
current_volume = mixer.getvolume()[0]
min_distance = 25
max_distance = 200

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPotitions(img, draw=False)

    if len(lmList) != 0:
        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

        cv2.circle(
            img, center=(x1, y1), radius=15, color=(255, 0, 255), thickness=cv2.FILLED
        )
        cv2.circle(
            img, center=(x2, y2), radius=15, color=(255, 0, 255), thickness=cv2.FILLED
        )
        cv2.line(img, pt1=(x1, y1), pt2=(x2, y2), color=(255, 0, 255), thickness=2)
        cv2.circle(
            img, center=(cx, cy), radius=15, color=(255, 0, 255), thickness=cv2.FILLED
        )

        length = math.hypot(x2 - x1, y2 - y1)
        # print(f"Distance: {length}")

        if length < min_distance:
            new_volume = 0
        elif length > max_distance:
            new_volume = 100
        else:
            new_volume = int(
                (length - min_distance) / (max_distance - min_distance) * 100
            )
            new_volume = max(0, min(new_volume, 100))

        if new_volume != current_volume:
            mixer.setvolume(new_volume)
            current_volume = new_volume
            print(f"Volume set to: {current_volume}%")

        if length < 25:
            cv2.circle(
                img, center=(cx, cy), radius=15, color=(0, 255, 0), thickness=cv2.FILLED
            )

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(
        img,
        text=f"FPS: {int(fps)}",
        org=(10, 30),
        fontFace=cv2.FONT_HERSHEY_DUPLEX,
        fontScale=1,
        color=(0, 255, 255),
        thickness=2,
    )

    volume_bar_width = 400
    volume_bar_height = 30
    volume_bar_x = 10
    volume_bar_y = 70

    cv2.rectangle(
        img,
        (volume_bar_x, volume_bar_y),
        (volume_bar_x + volume_bar_width, volume_bar_y + volume_bar_height),
        (200, 200, 200),
        thickness=cv2.FILLED,
    )

    current_volume_width = int((current_volume / 100) * volume_bar_width)
    cv2.rectangle(
        img,
        (volume_bar_x, volume_bar_y),
        (volume_bar_x + current_volume_width, volume_bar_y + volume_bar_height),
        (0, 255, 0),
        thickness=cv2.FILLED,
    )

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
