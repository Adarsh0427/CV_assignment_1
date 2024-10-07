# Description: Main script for running the Harris corner detector, SIFT descriptor, and feature matcher.
import cv2
from modules import HarrisCornerDetector, SIFTDescriptor, FeatureMatcher, Visualizer
import sys

def main(image1, image2):

    # Part 1: Keypoint detection
    detector = HarrisCornerDetector()
    keypoints1 = detector.detect(image1)
    keypoints2 = detector.detect(image2)

    # Visualize keypoints
    visualizer = Visualizer()
    output1 = visualizer.visualize_keypoints(image1, keypoints1)
    cv2.imwrite('S20220010004_FDDM_output1.png', output1)

    # Part 2: Feature description
    descriptor = SIFTDescriptor()
    descriptors1 = [descriptor.compute(image1, kp) for kp in keypoints1]
    descriptors2 = [descriptor.compute(image2, kp) for kp in keypoints2]

    # Part 3: Feature matching
    matcher = FeatureMatcher()
    matches = matcher.match(descriptors1, descriptors2)

    # Visualize matches
    output2 = visualizer.visualize_matches(image1, keypoints1, image2, keypoints2, matches)
    cv2.imwrite('S20220010004_FDDM_output2.png', output2)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        image1_path = 'image1.png'
        image2_path = 'image2.png'
    else:
        image1_path = sys.argv[1]
        image2_path = sys.argv[2]
    
    # Load images
    image1 = cv2.imread(image1_path)
    image2 = cv2.imread(image2_path)

    main(image1, image2)
