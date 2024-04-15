import os
import shutil
import numpy as np
from PIL import Image
from tqdm.auto import tqdm
import multiprocessing

def process_image(file_name):
    file_path = os.path.join(folder_path, file_name)

    # Check if the file is an image
    if os.path.isfile(file_path) and file_name.lower().endswith(('.png', '.jpg', '.jpeg')):

        # Open the image using PIL
        image = Image.open(file_path)

        # Check if the image is grayscale or if red, green, and blue histograms are identical
        if image.mode == "L" or image.histogram()[:256] == image.histogram()[256:512] == image.histogram()[512:]:
            # Move the image file to the "train_removed" folder
            new_file_path = os.path.join(removed_folder_path, file_name)
            shutil.move(file_path, new_file_path)
            return 1
        else:
            image = image.convert("RGB")  # Convert the image to RGB mode explicitly

            # Convert the image to a NumPy array for easier manipulation
            image_array = np.array(image)

            # Calculate the differences between the red, green, and blue channels
            red_channel = image_array[:, :, 0]
            green_channel = image_array[:, :, 1]
            blue_channel = image_array[:, :, 2]

            red_green_diff = np.abs(red_channel - green_channel)
            red_blue_diff = np.abs(red_channel - blue_channel)
            green_blue_diff = np.abs(green_channel - blue_channel)
            avg_diff = np.mean([red_green_diff, red_blue_diff, green_blue_diff])

            if avg_diff < threshold:
                # Move the image file to the "train_removed" folder
                new_file_path = os.path.join(removed_folder_path, file_name)
                shutil.move(file_path, new_file_path)
                return 1
    return 0

threshold = 30 # average difference threshold

folder_path = 'train2017'
removed_folder_path = 'train2017_removed'

# Create the "train_removed" folder if it doesn't exist
os.makedirs(removed_folder_path, exist_ok=True)

# Get the list of files in the folder
file_list = os.listdir(folder_path)

# Reset removed image number
removed_num = 0

# Multiprocessing
pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
results = list(tqdm(pool.imap(process_image, file_list), total=len(file_list), desc=folder_path))
pool.close()
pool.join()

# Count removed images
removed_num = sum(results)

print(f"Original has {len(file_list)} images.")
print(f"Total removed {removed_num} images.")

# Calculate the percentage of removed images
percentage_removed = (removed_num / len(file_list)) * 100

print(f"Percentage of removed images: {percentage_removed:.2f}%")
print(f"Images in '{folder_path}' moved successfully.")

