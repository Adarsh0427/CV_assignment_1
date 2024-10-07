# Description: This module implements a feature matcher that matches features between two images based on the distance between their descriptors.
import numpy as np

class FeatureMatcher:
    def __init__(self, ratio_threshold=0.7):
        self.ratio_threshold = ratio_threshold

    def match(self, descriptors1, descriptors2):
        matches = []
        for i, desc1 in enumerate(descriptors1):
            distances = np.sum((desc1 - descriptors2)**2, axis=1)
            sorted_indices = np.argsort(distances)
            best_match = sorted_indices[0]
            second_best_match = sorted_indices[1]
            
            ratio = distances[best_match] / distances[second_best_match]
            if ratio < self.ratio_threshold:
                matches.append((i, best_match))
        return matches