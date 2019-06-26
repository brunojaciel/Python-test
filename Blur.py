import cv2
img = cv2.imread("bruno.jpg", cv2.IMREAD_COLOR)
blur = cv2.blur(img, (10, 10))
cv2.imshow('bruno', blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("brunoresult.png", blur)
