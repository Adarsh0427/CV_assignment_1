# Description: This module contains the implementation of the SIFT feature descriptor.
import cv2
import numpy as np

class SIFTDescriptor:
    def __init__(self, num_bins=8, window_size=16):
        self.num_bins = num_bins
        self.window_size = window_size

    def compute(self, image, keypoint):
        x, y = keypoint
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        window = gray[max(0, y-self.window_size//2):min(y+self.window_size//2, gray.shape[0]), 
                      max(0, x-self.window_size//2):min(x+self.window_size//2, gray.shape[1])]
        
        gx = cv2.Sobel(window, cv2.CV_64F, 1, 0, ksize=3)
        gy = cv2.Sobel(window, cv2.CV_64F, 0, 1, ksize=3)
        
        magnitude = np.sqrt(gx**2 + gy**2)
        orientation = np.arctan2(gy, gx) * 180 / np.pi % 360
        
        hist, _ = np.histogram(orientation, bins=self.num_bins, range=(0, 360), weights=magnitude)
        
        hist = hist / np.linalg.norm(hist)
        
        return hist