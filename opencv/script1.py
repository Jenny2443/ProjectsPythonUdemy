import cv2

# Read the image
    # 0 -> black and white
    # 1 -> rgb default
    # -1 -> alpha

#type of img -> numpy
img = cv2.imread("galaxy.jpg",-1)

print(img.shape)
print(img.ndim)

# Resizing the image 
resized_image = cv2.resize(img,(int(img.shape[1] / 2),int(img.shape[0] / 2)))

# Open a window with the image
cv2.imshow("Galaxy",resized_image)

# Store the resized img as a new file
cv2.imwrite("galaxy_resized.jpg",resized_image)
# If 0 -> it waits until a key is pressed
# If number as a parameter -> it waits for a input or until that time has passed (1000 = 1s because is in ms)
cv2.waitKey(5000)
cv2.destroyAllWindows()