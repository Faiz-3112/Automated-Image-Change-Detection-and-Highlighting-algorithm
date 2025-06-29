# 🖼️ Automated Image Change Detection & Highlighting

## Overview
This project provides an automated solution for detecting and highlighting significant changes between pairs of images. It is ideal for visual regression testing, surveillance, and quality control—anywhere you need to quickly spot and localize visual differences.

---

## Features
- **Batch Processing:** Effortlessly analyzes hundreds of image pairs in a single run.
- **Automated Change Detection:** Pinpoints and localizes meaningful visual differences between "before" and "after" images.
- **Noise Filtering:** Ignores minor or irrelevant changes using configurable thresholds and area filters.
- **Visual Output:** Draws clear, red bounding boxes around detected changes for rapid inspection.
- **Numeric Reporting:** Outputs the number of changed pixels and detected regions for each image pair.
- **Reproducible Pipeline:** Built with Python, PIL, NumPy, and SciPy for consistent, reliable results.

---

## How It Works
1. **Input Preparation:**  
   Place your "before" images (e.g., `1.jpg`) and corresponding "after" images (e.g., `1~2.jpg`) in the `input-images` directory.
   - **Note:** The script expects pairs like `N.jpg` (before) and `N~2.jpg` (after) for each image, where N is a number or identifier.

2. **Processing Logic:**  
   - Compares each "before" and "after" image pair.
   - Computes the absolute pixel-wise difference and converts it to grayscale.
   - Applies a threshold to identify significant changes.
   - Uses connected component analysis to group adjacent changed pixels into regions.
   - Filters out small regions (default: area < 100 pixels) to reduce noise.
   - Draws red bounding boxes around significant regions on the "after" image.

3. **Output:**  
   - Saves the original "before" image and the marked "after" image (with bounding boxes) in the `output` directory.
   - Prints a summary for each processed image.

---

## Quickstart

### 1. Clone the Repository
```bash
git clone https://github.com/Faiz-3112/Automated-Image-Change-Detection-and-Highlighting-algorithm.git
cd "Automated-Image-Change-Detection-and-Highlighting-algorithm"
```

### 2. Set Up the Environment
```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Prepare Input Images
- Place your "before" and "after" image pairs in the `input-images` folder.
- Naming convention:
  - Before: `N.jpg`  
  - After:  `N~2.jpg`
- Example: `1.jpg` (before), `1~2.jpg` (after)

### 4. Run the Script
```bash
python "Automated Image Change Detection and Highlighting algorithm.py"
```

### 5. View Results
- Output images with highlighted changes will be saved in the `output` directory.
- For each pair, you will find both the original and the marked (with bounding boxes) images.

---

## Configuration
You can fine-tune detection sensitivity and noise filtering by editing these parameters in `Automated Image Change Detection and Highlighting algorithm.py`:
- `threshold_val`: Pixel intensity difference threshold (default: 30)
- `min_size`: Minimum area (in pixels) for a region to be considered significant (default: 100)

---

## Numeric Reporting
For each image pair, the script reports:
- **Total changed pixels:** Number of pixels exceeding the threshold.
- **Detected regions:** Number of distinct changed areas (blobs).
- **Region area:** Area (in pixels) of each detected region.

---

## Dependencies
- Python 3.x
- [Pillow (PIL)](https://python-pillow.org/)
- [NumPy](https://numpy.org/)
- [SciPy](https://scipy.org/)

Install all dependencies using:
```bash
pip install -r requirements.txt
```

---

## Recent Changes
- **File/Folder Naming:** Output is now saved in the `output` directory. Input images should be placed in `input-images`.
- **Image Pairing:** The script expects pairs like `N.jpg` and `N~2.jpg` for each image.
- **Updated Instructions:** All steps and paths have been revised for clarity and accuracy.

---

## License
This project is licensed under the MIT License.

---

## Acknowledgements
- Built using open-source libraries: Pillow, NumPy, and SciPy.
- Inspired by real-world needs in visual regression and automated quality assurance.

---
