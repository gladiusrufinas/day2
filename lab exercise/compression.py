import cv2
import matplotlib.pyplot as plt
img=cv2.imread("sample.jpg")
cv2.imwrite("Compressed.jpg",img,[cv2.IMWRITE_JPEG_QUALITY,50])
cv2.imwrite("Compressed.png",img,[cv2.IMWRITE_JPEG_QUALITY,50])
cv2.imwrite("Compressed.webp",img,[cv2.IMWRITE_JPEG_QUALITY,50])
