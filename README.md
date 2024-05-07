# Dataset Preparation and Augmentation for Image Colorization

This repository contains Python scripts for preparing and augmenting the COCO 2017 dataset for image colorization tasks. The `download_dataset.sh` script downloads the dataset, followed by `dataset_filter.py` which refines the dataset by removing images with low color variation. Then, `dataset_prepare.py` filters removed images and pushes modified datasets to Hugging Face Hub.
## Requirements

1. Download the COCO 2017 dataset by running `download_dataset.sh`.
2. Ensure Python is installed on your system.
3. Install the required dependencies by running `pip install -r requirements.txt`.

## Usage

### Main

#### `download_dataset.sh`
Downloads the COCO 2017 dataset required for image colorization tasks.

#### `dataset_filter.py`
Further refines the COCO 2017 dataset by removing images with low color variation. Images are evaluated based on the differences between the red, green, and blue channels. Images that meet the specified threshold are moved to a separate folder.

#### `dataset_prepare.py`
Prepares a modified version of the COCO 2017 dataset for colorization tasks by filtering out removed images from the training split. It then pushes the modified training dataset and the original validation dataset to the Hugging Face Hub for easy access and sharing.

### Caption-free 

#### `augment_captions.py`
Augments the COCO 2017 colorization dataset by adding randomized colorization prompts to the image captions. It then pushes the modified datasets to the Hugging Face Hub with new split names for easy access and sharing.

### Custom-caption
#### `captions_generator.py`
Using CLIP Interrogator, based on the project available at [clip-interrogator/run_cli.py](https://github.com/pharmapsychotic/clip-interrogator/blob/main/run_cli.py). It generates captions for images. It can process a single image or a folder full of images. The user can choose between different captioning modes and CLIP models for optimal results. 

#### `csv_filter.py`
This code cleans a CSV file containing image captions. It defines a function to remove unlikely words related to image descriptions, such as "black and white" or "desaturated". The script then reads the CSV, cleans the captions using the defined function, and writes the cleaned data to a new CSV file.

#### `dataset_map_custom.py`
This code modifies captions in a Hugging Face dataset with custom captions. It takes arguments for the dataset name, captions file path, dataset split ('train' or 'validation'), and a revision name. It then reads the custom captions from a CSV file and defines a function to replace the original captions with the custom ones for each example in the dataset. Finally, it applies the function to the specified split of the dataset, pushes the modified dataset to the Hugging Face Hub with a new revision name.

#### `custom_caption_dataset.sh`
It first use `captions_generator.py` to generate captions, then use `csv_filter.py` to filter out unlikely words. Finally, it use `dataset_map_custom.py` to push the filtered captions to a custom dataset on Huggingface for potential use in colorization tasks.  

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request with any improvements or suggestions.
