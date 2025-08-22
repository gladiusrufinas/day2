import cv2
import matplotlib.pyplot as plt
img=cv2.imread("image1.jpg")
print(img.shape)
cv2.rectangle(img,(1200,1200),(500,500),(0,255,0),15)
plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.show()
