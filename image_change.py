import cv2

imgs = cv2.imread('assets/f.jpeg', 1)

cv2.imshow('Image', imgs)
cv2.waitKey(0)
cv2.destroyAllWindows()