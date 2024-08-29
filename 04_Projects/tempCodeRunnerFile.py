while True:
   stat, frame = cap.read()                            
   frame = cv2.flip(frame, 1)

   img_RGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)                             # convert from BGR to RGB

   res = hands.process(img_RGB)                                                 # check hand in frame or not 
