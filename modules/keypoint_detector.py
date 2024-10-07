# Description: Harris corner detector implementation
import cv2
import numpy as np
from scipy.ndimage import gaussian_filter

class HarrisCornerDetector:
    def __init__(self, k=0.04, threshold=0.01, window_size=5):
        self.k = k
        self.threshold = threshold
        self.window_size = window_size

    def detect(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = np.float32(gray)
        
        dx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
        dy = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
        
        Ixx = dx * dx
        Ixy = dx * dy
        Iyy = dy * dy
        
        Ixx = gaussian_filter(Ixx, sigma=self.window_size)
        Ixy = gaussian_filter(Ixy, sigma=self.window_size)
        Iyy = gaussian_filter(Iyy, sigma=self.window_size)
        
        det = Ixx * Iyy - Ixy**2
        trace = Ixx + Iyy
        harris_response = det - self.k * (trace**2)
        
        threshold = self.threshold * harris_response.max()
        corner_mask = harris_response > threshold
        
        coords = np.column_stack(np.where(corner_mask))
        keypoints = []
        for y, x in coords:
            if np.all(harris_response[y, x] >= harris_response[max(0, y-1):min(y+2, harris_response.shape[0]), 
                                                              max(0, x-1):min(x+2, harris_response.shape[1])]):
                keypoints.append((x, y))
        
        return keypoints