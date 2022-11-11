# Import library
import cv2

# Import Image
#image = cv2.imread("C:/Users/Yashesh Pandya/Downloads/programming/project/Convert_img/bee.jpg")
image = cv2.imread("C:/Users/Yashesh Pandya/Downloads/programming/project/Convert_img/jerry.jpg")

# Add grey filter
grey_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Add inverted filter
invert = cv2.bitwise_not(grey_img)

# Add blur filter
blur = cv2.GaussianBlur(invert, (21,21),0)
invertedblur = cv2.bitwise_not(blur)

# Export the sketch image
sketch = cv2.divide(grey_img, invertedblur, scale=256.0)

cv2.imwrite("sketch1.png", sketch)