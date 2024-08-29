import cv2
import mediapipe as mp
import time 
import numpy as np
import math

from pycaw.pycaw import AudioUtilities, IAudioClient
from comtypes import CLSCTX_ALL
from ctypes import cast, POINTER

cap = cv2.VideoCapture(0)                                                       # intialization camera.
mpHands = mp.solutions.hands                                                    # Hand Code.
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

while True:
   stat, frame = cap.read()                            
   frame = cv2.flip(frame, 1)
   img_RGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)                             # convert from BGR to RGB
   res = hands.process(img_RGB)                                                 # check hand in frame or not 
   lm_List = []


   if res.multi_hand_landmarks:
      for handLms in res.multi_hand_landmarks: 
         for id, lm in enumerate(handLms.landmark):
            _high, _wigdth, _cm = frame.shape                                   # calc High , Wigdth , CM.
            cx, cy = int(lm.x * _wigdth), int(lm.y * _high)                     # X-aix , y-aix. 
            lm_List.append([id, cx, cy])                                         # list to store data of hand. 
            mpDraw.draw_landmarks(frame, handLms, mpHands.HAND_CONNECTIONS)     # draw nets on hand
            
            if len(lm_List) == 21:
               x1,y1 = lm_List[4][1], lm_List[4][2]
               x2,y2 = lm_List[8][1], lm_List[8][2]

               cx, cy = ((x1 + x2) // 2), ((y1 + y2) // 2)   

               cv2.circle(frame, (x1,y1), 8 , (255,0,255), cv2.FILLED)
               cv2.circle(frame, (x2,y2), 8 , (255,0,255), cv2.FILLED)
               cv2.line(frame, (x1, y1), (x2, y2), (0, 0, 0), 3)
               cv2.circle(frame, (cx, cy), 5, (255, 0, 255), cv2.FILLED)
               length = math.hypot(x2 - x1, y2 - y1)
               
# ---------------- Show Data Start ---------------- #
   cv2.imshow('Hand Tracker', frame)
   if cv2.waitKey(5) & 0xff == ord("x"):
      break
# ---------------- Show Data end ---------------- #            