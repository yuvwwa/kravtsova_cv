import cv2

cap = cv2.VideoCapture("pictures.avi")

count = 0
while True:
    _, frame = cap.read()
    if  not _:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.bitwise_not(gray)
    _, thresh = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)

    cnts, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    area = cv2.contourArea(cnts[0])

    if area > 53000 and area < 53100:
        count += 1

    cv2.putText(frame, f"count of my images = {count}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (127, 255, 0))
    #cv2.putText(frame, f"area = {area}", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (127, 255, 0))

    cv2.imshow("Image", frame)
    
    key = cv2.waitKey(1)
    if key == ord('q'):
        break    

print(f"Total number of my images = {count}")
cap.release()
cv2.destroyAllWindows()
