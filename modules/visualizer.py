# Description: This module contains the Visualizer class which provides methods to visualize keypoints and matches.
import cv2
import numpy as np

class Visualizer:
    @staticmethod
    def visualize_keypoints(image, keypoints):
        vis = image.copy()
        for kp in keypoints:
            cv2.circle(vis, kp, 3, (0, 255, 0), 1)
        return vis

    @staticmethod
    def visualize_matches(img1, kp1, img2, kp2, matches):
        h1, w1 = img1.shape[:2]
        h2, w2 = img2.shape[:2]
        vis = np.zeros((max(h1, h2), w1 + w2, 3), dtype=np.uint8)
        vis[:h1, :w1] = img1
        vis[:h2, w1:w1+w2] = img2
        
        for idx1, idx2 in matches:
            pt1 = tuple(map(int, kp1[idx1]))
            pt2 = tuple(map(int, [kp2[idx2][0] + w1, kp2[idx2][1]]))
            cv2.line(vis, pt1, pt2, (0, 255, 0), 1)
        
        return vis