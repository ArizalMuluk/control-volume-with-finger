import time

import cv2
import mediapipe as mp


class handsDetect:
    def __init__(self, mode=False, maxHands=2, detectCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectCon = detectCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(
            static_image_mode=self.mode,
            max_num_hands=self.maxHands,
            min_detection_confidence=self.detectCon,
            min_tracking_confidence=self.trackCon,
        )
        self.mpDraws = mp.solutions.drawing_utils

    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.result = self.hands.process(imgRGB)

        if self.result.multi_hand_landmarks:
            for handLms in self.result.multi_hand_landmarks:
                if draw:
                    self.mpDraws.draw_landmarks(
                        img,
                        handLms,
                        self.mpHands.HAND_CONNECTIONS,
                        self.mpDraws.DrawingSpec(color=(0, 0, 255), thickness=2),
                        self.mpDraws.DrawingSpec(color=(0, 255, 0), thickness=2),
                    )
        return img

    def findPotitions(self, img, handNo=0, draw=True):

        lmList = []

        if self.result.multi_hand_landmarks:
            myHand = self.result.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                # print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])
                # print(id, cx, cy)
                if draw:
                    cv2.circle(
                        img,
                        center=(cx, cy),
                        radius=10,
                        color=(255, 0, 255),
                        thickness=cv2.FILLED,
                    )

        return lmList


def main():
    cTime = 0
    pTime = 0
    cap = cv2.VideoCapture(0)
    detector = handsDetect()

    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPotitions(img)
        if len(lmList) != 0:
            print(lmList[4])

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(
            img,
            text=str(int(fps)),
            org=(10, 70),
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=3,
            color=(255, 0, 255),
            thickness=3,
        )

        cv2.imshow("Image", img)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break


if __name__ == "__main__":
    main()
