# Dataset Preparation and Augmentation for Image Colorization

This repository contains Python scripts for preparing and augmenting the COCO 2017 dataset for image colorization tasks. The `download_dataset.sh` script downloads the dataset, followed by `dataset_filter.py` which refines the dataset by removing images with low color variation. Then, `prepare_dataset.py` filters removed images and pushes modified datasets to Hugging Face Hub. Finally, `augment_captions.py` adds randomized colorization prompts to captions, enhancing dataset diversity.

## Usage

1. Download the COCO 2017 dataset by running `download_dataset.sh`.
2. Ensure Python is installed on your system.
3. Install the required dependencies by running `pip install -r requirements.txt`.
4. Execute the scripts in a Python environment, specifying any necessary input parameters.
5. Modified datasets will be pushed to the Hugging Face Hub for easy access and sharing.

## Scripts

### 1. `download_dataset.sh`

- **Description:** Downloads the COCO 2017 dataset required for image colorization tasks.

### 2. `dataset_filter.py`

- **Description:** Further refines the COCO 2017 dataset by removing images with low color variation. Images are evaluated based on the differences between the red, green, and blue channels. Images that meet the specified threshold are moved to a separate folder.

### 3. `prepare_dataset.py`

- **Description:** Prepares a modified version of the COCO 2017 dataset for colorization tasks by filtering out removed images from the training split. It then pushes the modified training dataset and the original validation dataset to the Hugging Face Hub for easy access and sharing.

### 4. `augment_captions.py`

- **Description:** Augments the COCO 2017 colorization dataset by adding randomized colorization prompts to the image captions. It then pushes the modified datasets to the Hugging Face Hub with new split names for easy access and sharing.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request with any improvements or suggestions.
