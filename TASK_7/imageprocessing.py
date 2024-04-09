import cv2
  
path=r"C:\\Users\\chint\\AppData\\Local\\Programs\\Python\\Python310\\Summer Project Robotics Club Task\\Screenshot 2024-04-08 095210.png" 

image = cv2.imread(path)
#cv2.imshow('Original', image)
image = cv2.GaussianBlur(image, (9, 9), 0) 

cv2.waitKey(0) 
  

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 

cv2.imshow('Grayscale',gray_image) 
cv2.waitKey(0)

cv2.destroyAllWindows()
