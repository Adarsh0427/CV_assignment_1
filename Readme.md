# Name : Adarsh Singh
# Roll no. - S20220010004

# Computer Vision Assignment: Feature Detection and Matching

This project implements a computer vision pipeline for feature detection, description, and matching using Python. It includes implementations of Harris Corner Detection, SIFT-like feature description, and feature matching.

## Prerequisites

Before you begin, ensure you have met the following requirements:

* Python 3.7 or later
* pip (Python package installer)
* Git (for cloning the repository)

## Installation

To set up the CV Assignment on your local machine, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/Adarsh0427/CV_assignment_1.git
   cd S20220010004_FDDM
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Place your input images in the project root directory. The code expects two images named `image1.png` and `image2.png`.

2. Run the main script:
   ```bash
   python main.py 
   ```
3. Run the main script (optional):
   ```bash
   python main.py <image1> <image2>
   ```

3. The script will generate two output images:
   - `S20220010004_FDDM_output1.jpg`: Visualization of detected keypoints
   - `S20220010004_FDDM_output2.jpg`: Visualization of matched features

## Project Structure

```
cv-assignment/
├── main.py
├── requirements.txt
├── README.md
├── modules/
│   ├── __init__.py
│   ├── keypoint_detector.py
│   ├── feature_descriptor.py
│   ├── feature_matcher.py
│   └── visualizer.py
```

- `main.py`: Orchestrates the computer vision pipeline
- `modules/`: Package containing individual components
  - `keypoint_detector.py`: Harris Corner Detection
  - `feature_descriptor.py`: SIFT-like feature descriptor
  - `feature_matcher.py`: Feature matching
  - `visualizer.py`: Visualization utilities
