# opencv-basic-hacks

## Binary Image Processing
1. Thresholding: used to create binary image from a grayscale image
2. Erosion: used to shrink the size of blobs (a group of connected pixels) in a binary image'
3. Dilation: used to expand the size of blobs in a binary image
4. Connected componenet analysis: used to label blob in a binary image.

### 1 - Thresholding
Thresholding is a simple operation that converts a grayscale image into a binary image based on the intensity of each pixels.
Documentation [https://docs.opencv.org/3.4.0/d7/d1b/group__imgproc__misc.html#gae8a4a146d1ca78c626a53577199e9c57]

![alt text](/data/images/threshold_out1.png)

### 2 - Dilation
Used to expand the edges of a blocb
![alt text](/data/images/truth_out.png)

### 3 - Erosion
Used to remove(erode) the white pixels around the blob
![alt text](/data/images/truth_e_out.png)

