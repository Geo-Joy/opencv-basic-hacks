import cv2
import numpy as np

### THRESHOLDING

# reading the image as greyscale
org_img = cv2.imread("data/images/threshold.png", cv2.IMREAD_GRAYSCALE)

threshold = 0 # set value above which thresholding works
maxValue = 255 # min value below which thresholding should be applied

#retval, dst = cv.threshold(src, thresh, maxval, type[, dst])
ret, th_img = cv2.threshold(org_img, threshold, maxValue, cv2.THRESH_BINARY)

# display the images
cv2.imshow("Original Image", org_img)
cv2.imshow("Thresholded Image", th_img)

# write the new image to disk
cv2.imwrite("data/images/threshold_out.png", th_img)



### Dilation

org_img_dilation = cv2.imread("data/images/truth.png", cv2.IMREAD_GRAYSCALE)

# We create the kernel/structuring element that is used for dilation operation.
dilationSize = 5
kernal = cv2.getStructuringElement(cv2.MORPH_CROSS, (2*dilationSize+1, 2*dilationSize+1),(dilationSize, dilationSize))
print(kernal)

imageDilated = cv2.dilate(org_img_dilation, kernal)

cv2.imshow("Original Image", org_img_dilation)
cv2.imshow("Dilated Image", imageDilated)


### Erosion

org_img_dilation = cv2.imread("data/images/truth.png", cv2.IMREAD_GRAYSCALE)

# We create the kernel/structuring element that is used for dilation operation.
dilationSize = 5
kernal = cv2.getStructuringElement(cv2.MORPH_CROSS, (2*dilationSize+1, 2*dilationSize+1),(dilationSize, dilationSize))
print(kernal)

imageDilated = cv2.erode(org_img_dilation, kernal)

cv2.imshow("Original Image", org_img_dilation)
cv2.imshow("Eroded Image", imageDilated)




### Morphological Open

org_img_morph = cv2.imread("data/images/opening.png", cv2.IMREAD_GRAYSCALE)

# We create the kernel/structuring element that is used for dilation operation.
openingSize = 5
kernal = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2*openingSize+1, 2*openingSize+1),(openingSize, openingSize))
print(kernal)

imageMorphOpen = cv2.morphologyEx(org_img_morph, cv2.MORPH_OPEN, kernal, iterations=2)

cv2.imshow("Original Image", org_img_morph)
cv2.imshow("Open Image", imageMorphOpen)


### Morphological Close

org_img_morph = cv2.imread("data/images/closing.png", cv2.IMREAD_GRAYSCALE)

# We create the kernel/structuring element that is used for dilation operation.
openingSize = 5
kernal = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2*openingSize+1, 2*openingSize+1),(openingSize, openingSize))
print(kernal)

imageMorphOpen = cv2.morphologyEx(org_img_morph, cv2.MORPH_CLOSE, kernal, iterations=2)

cv2.imshow("Original Image", org_img_morph)
cv2.imshow("Open Image", imageMorphOpen)


### Connected Component Analysis (CCA)

cca_image = cv2.imread('data/images/truth.png', cv2.IMREAD_GRAYSCALE)
threshold = 0
maxValue = 255
ret, imThresh = cv2.threshold(cca_image, threshold, maxValue, cv2.THRESH_BINARY)
_, imLabels = cv2.connectedComponents(imThresh)

def displayConnectedComponents(im):
    imlabels = im
    # find min max pixel value and their locations
    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(imlabels)
    print(minVal, maxVal, minLoc, maxLoc)
    
    #normalizing the pixel values in range of 0-255
    imLabels = 255 * (imlabels - minVal)/(maxVal - minVal)
    
    #convert the image to 8bit unsigned type
    imLabels = np.uint8(imLabels)
    
    # Apply a color map
    imColorMap = cv2.applyColorMap(imLabels, cv2.COLORMAP_RAINBOW)
    
    #Display
    cv2.imshow("Labels", imColorMap)
    cv2.waitKey(0)

displayConnectedComponents(imLabels)
