import cv2
tesla1 = cv2.imread("20220415124700.jpg")
cv2.imshow("t1",tesla1)
key=cv2.waitKey()
if key==ord('q'):
    cv2.destroyWindow("t1")
    