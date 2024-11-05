import cv2

cap=cv2.VideoCapture(0)

while True:
    res,frame=cap.read()

    # print(frame.shape)
    frame=cv2.flip(frame,1)
    x1,x2,y1,y2=400,600,50,300
    roi=frame[y1:y2,x1:x2]

    cv2.rectangle(frame,(400,50),(600,300),255,10)
    # cv2.imshow('dis',frame)
    cv2.imshow('roi',roi)
    if cv2.waitKey(1)==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()