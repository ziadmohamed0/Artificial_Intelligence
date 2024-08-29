##############################################################
#   @file       :   Hand_Tracking.py                         #
#   @brief      :   Enables camera to recognize hands,       #
#                   interpret gestures, and enable           #
#                   interactions with virtual objects to     #   
#                   write numbers on the screen.             #
#   @auther     :   Ziad Mohammed Fathi Mohammed.            #
#   @date_start :   Aug.15.2024.                             #
#   @date_end   :   Aug.15.2024.                             #
#   @work_hrs   :   2hrs.                                    #
##############################################################



# ---------------- imoprts section Start ---------------- #
import cv2                                                                      # Library Hand Tracking.
import mediapipe as mp                                                          # Library Comuter Vision 2.                                                              
# ---------------- imoprts section End ---------------- #


# ---------------- intialization variables section Start ---------------- #
cap = cv2.VideoCapture(0)                                                       # intialization camera.
mpHands = mp.solutions.hands                                                    # Hand Code.
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
tipIds = [4, 8, 12, 16, 20]                                                     # start point in each finger.
# ---------------- intialization variables section End ---------------- #

# ---------------- Main Program section Start ---------------- #
while True:
   stat, frame = cap.read()                            
   frame = cv2.flip(frame, 1)

   img_RGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)                             # convert from BGR to RGB

   res = hands.process(img_RGB)                                                 # check hand in frame or not 

   lmList = []                                                                  # list to store data of hand

   if res.multi_hand_landmarks:
      
      for handLms in res.multi_hand_landmarks:
         
         for id, lm in enumerate(handLms.landmark):
            _high, _wigdth, _cm = frame.shape                                   # calc High , Wigdth , CM.
            cx, cy = int(lm.x * _wigdth), int(lm.y * _high)                     # X-aix , y-aix. 
            lmList.append([id, cx, cy])                                         # list to store data of hand. 
            mpDraw.draw_landmarks(frame, handLms, mpHands.HAND_CONNECTIONS)     # draw nets on hand
            

            if id == 8:
               cv2.circle(frame, (cx, cy), 20, (0, 255, 0), cv2.FILLED)         # Draw circle on finger 

            if len(lmList) == 21:
               fingers = []

               if lmList[tipIds[0]][1] < lmList[tipIds[0] - 2][1]:
                  fingers.append(1)
               else:
                  fingers.append(0)

               for tip in range(1, 5):
                  if lmList[tipIds[tip]][2] < lmList[tipIds[tip] - 2][2]:
                     fingers.append(1)
                  else:
                     fingers.append(0)

               totalFingers = fingers.count(1)                                  # varibale calc number of hand.
               print(totalFingers)
               cv2.putText(frame, f'{totalFingers}', (40, 80), cv2.FONT_HERSHEY_SIMPLEX,
               3, (0, 0, 255), 6)                                               # print data on frame.
# ---------------- Main Program section end ---------------- #

# ---------------- Show Data Start ---------------- #
   cv2.imshow('Hand Tracker', frame)
   if cv2.waitKey(5) & 0xff == ord("x"):
      break
# ---------------- Show Data end ---------------- #
