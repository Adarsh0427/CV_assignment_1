Installing CV Assignment
To install CV Assignment, follow these steps:

Clone the repository:
Copygit clone https://github.com/yourusername/cv-assignment.git
Replace yourusername with your actual GitHub username if you've pushed this to your own repository.
Navigate to the project directory:
Copycd cv-assignment

(Optional) Create and activate a virtual environment:
Copypython -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

Install the required packages:
Copypip install -r requirements.txt


Using CV Assignment
To use CV Assignment, follow these steps:

Ensure you're in the project directory and your virtual environment is activated (if you're using one).
Place your input images in the project directory. The code expects two images named image1.jpg and image2.jpg.
Run the main script:
Copypython main.py

The script will generate two output images:

S20220010XYZ_FDDM_output1.jpg: Visualization of detected keypoints
S20220010XYZ_FDDM_output2.jpg: Visualization of matched features

Note: Replace "S20220010XYZ" with your actual roll number in the code before running.

Project Structure
Copycv_assignment/
├── main.py
├── requirements.txt
├── README.md
├── modules/
│   ├── __init__.py
│   ├── keypoint_detector.py
│   ├── feature_descriptor.py
│   ├── feature_matcher.py
│   └── visualizer.py

main.py: The main script that orchestrates the computer vision pipeline
modules/: A package containing the individual components of the pipeline

keypoint_detector.py: Implements Harris Corner Detection
feature_descriptor.py: Implements a SIFT-like feature descriptor
feature_matcher.py: Implements feature matching
visualizer.py: Provides visualization utilities