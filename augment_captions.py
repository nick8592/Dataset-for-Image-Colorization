import os
from datasets import load_dataset

# Function to extract the non-zero part of an image filename as an ID
def get_non_zero_part(image_name):
    # Remove leading zeros from the filename and convert to integer
    return int(image_name.split('.')[0])

# Function to get the IDs of removed images from a folder
def get_removed_image_ids(folder):
    # Get the list of files in the folder
    images = os.listdir(folder)

    image_ids = []
    for image in images:
        id = get_non_zero_part(image)
        image_ids.append(id)

    # Sort the list of image ids
    image_ids.sort()

    return image_ids

def main():
    # Define the folder containing removed images
    removed_images_folder = 'train2017_removed'

    # Get IDs of removed images
    sorted_removed_file_ids = get_removed_image_ids(removed_images_folder)
    print(f"Number of total removed images: {len(sorted_removed_file_ids)}")

    # Define the original dataset name and image folder
    dataset_name = 'phiyodr/coco2017'

    # Load train and validation splits of the original dataset
    train_dataset = load_dataset(dataset_name, split="train")
    val_dataset = load_dataset(dataset_name, split="validation")

    # Filter out removed images from the training dataset
    color_train_dataset = train_dataset.filter(lambda example: example['image_id'] not in sorted_removed_file_ids)
    print(f"Number of remaining train images: {len(color_train_dataset)}")

    # Push the modified training dataset and original validation dataset to the Hugging Face Hub
    color_train_dataset.push_to_hub("nickpai/coco2017-colorization", split="train")
    val_dataset.push_to_hub("nickpai/coco2017-colorization", split="validation")

# Entry point of the script
if __name__ == "__main__":
    main()
