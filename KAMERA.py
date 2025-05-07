import cv2
import serial
import time

arduino = serial.Serial('COM3', 9600) 
time.sleep(2) 

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (35, 35), 0)

    _, thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY_INV)

    contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) > 0:
        largest_contour = max(contours, key=cv2.contourArea)
        
       
        contour_area = cv2.contourArea(largest_contour)
        
       
        if contour_area > 5000: 
            print("El Açık - LED YANIK")
            arduino.write(b'1')  # LED aç
        else:
            print("El Kapalı - LED SÖNÜK")
            arduino.write(b'0')  # LED kapat

    cv2.imshow("Frame", frame)
    cv2.imshow("Thresh", thresh)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
arduino.close()