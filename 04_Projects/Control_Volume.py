import cv2
import numpy as np
import math
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import mediapipe as mp

# Define the width and height of the video capture
w, h = 620, 480

# Initialize video capture
cap = cv2.VideoCapture(0)
cap.set(3, w)
cap.set(4, h)

# Initialize MediaPipe hand detector
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

# Initialize volume control
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)

# Get volume range
vol_range = volume.GetVolumeRange()
min_vol = vol_range[0]
max_vol = vol_range[1]

# Main loop
while True:
    try:
        # Capture frame-by-frame
        ret, img = cap.read()
        if not ret:
            print("Failed to capture image")
            break
        
        # Convert the image to RGB
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(img_rgb)

        if results.multi_hand_landmarks:
            for landmarks in results.multi_hand_landmarks:
                # Draw landmarks and connections
                mp_drawing.draw_landmarks(img, landmarks, mp_hands.HAND_CONNECTIONS)
                
                # Get positions of the tip of the index (8) and thumb (4) fingers
                x1, y1 = int(landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * w), int(landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * h)
                x0, y0 = int(landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x * w), int(landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y * h)
                cx, cy = (x1 + x0) // 2, (y1 + y0) // 2

                # Draw landmarks and lines
                cv2.circle(img, (x1, y1), 10, (0, 0, 0), cv2.FILLED)
                cv2.circle(img, (x0, y0), 10, (0, 0, 0), cv2.FILLED)
                cv2.line(img, (x1, y1), (x0, y0), (0, 0, 0), 3)
                cv2.circle(img, (cx, cy), 10, (0, 0, 255), cv2.FILLED)

                # Calculate distance and map to volume
                length = math.hypot(x0 - x1, y0 - y1)
                vol = np.interp(length, [10, 150], [min_vol, max_vol])
                volume.SetMasterVolumeLevel(vol, None)

                if length < 50:
                    cv2.circle(img, (cx, cy), 10, (0, 0, 255), cv2.FILLED)

        # Display the resulting frame
        cv2.putText(img, "Volume Control Using Hand Gestures", (int(w / 2) - 160, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
        cv2.imshow("Volume Control Using Hand Gestures", img)

        # Break loop on 'q' key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    except Exception as e:
        print(f"An error occurred: {e}")

# Release resources
cap.release()
cv2.destroyAllWindows()