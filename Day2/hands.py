import cv2
import matplotlib.pyplot as plt
img=cv2.imread("image.jpg")
gaussian=cv2.GaussianBlur(img,(5,5),0)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edge=cv2.Canny(gray,50,100)
plt.imshow(cv2.cvtColor(edge,cv2.COLOR_BGR2RGB))
plt.show()