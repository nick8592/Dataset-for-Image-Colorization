# Dataset Preparation and Augmentation for Image Colorization

## Overview

This repository contains Python scripts for dataset preparation and augmentation tailored for image colorization tasks. The scripts are designed to work with the COCO 2017 dataset and utilize the Hugging Face Datasets library for dataset management. The goal is to facilitate the creation of modified datasets with filtered images and augmented captions, suitable for training image colorization models.

## Scripts

### 1. `prepare_dataset.py`

This script prepares a modified version of the COCO 2017 dataset for colorization tasks by filtering out removed images from the training split. It then pushes the modified training dataset and the original validation dataset to the Hugging Face Hub for easy access and sharing.

#### Functions:
- `get_non_zero_part(image_name)`: Extracts the non-zero part of an image filename as an ID.
- `get_removed_image_ids(folder)`: Retrieves the IDs of removed images from a specified folder.
- `main()`: Entry point of the script; orchestrates the dataset preparation process.

### 2. `augment_captions.py`

This script augments the COCO 2017 colorization dataset by adding randomized colorization prompts to the image captions. It then pushes the modified datasets to the Hugging Face Hub with new split names for easy access and sharing.

#### Functions:
- `choose_sentence(example)`: Randomly selects a colorization prompt and adds it to the captions of the given example.
- `main()`: Entry point of the script; orchestrates the dataset augmentation process.

## Usage

1. Download the COCO 2017 dataset by running `download_dataset.sh`.
2. Ensure Python is installed on your system.
3. Install the required dependencies by running `pip install -r requirements.txt`.
4. Execute the scripts in a Python environment, specifying any necessary input parameters.
5. Modified datasets will be pushed to the Hugging Face Hub for easy access and sharing.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request with any improvements or suggestions.
