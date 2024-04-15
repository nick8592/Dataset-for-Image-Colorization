import random
from tqdm import tqdm
from datasets import load_dataset

# Function to randomly choose a sentence for image colorization prompts
def choose_sentence(example):
    sentences = [
        "Add colors to this image",
        "Give realistic colors to this image",
        "Add realistic colors to this image",
        "Colorize this grayscale image",
        "Colorize this image",
        "Restore the original colors of this image",
        "Make this image colorful",
        "Colorize this image as if it was taken with a color camera",
        "Create the original colors of this image"
    ]
    prompt = random.choice(sentences)
    example["captions"] = [prompt]
    return example

def main():
    # Define the original dataset name and image folder
    DATASET = 'nickpai/coco2017-colorization'

    # Load train and validation splits of the dataset
    train_dataset = load_dataset(DATASET, split="train")
    val_dataset = load_dataset(DATASET, split="validation")

    # https://huggingface.co/docs/datasets/process#map
    # Modify captions in the train dataset
    print("Modifying captions in the train dataset:")
    caption_free_train_dataset = train_dataset.map(choose_sentence)

    # Modify captions in the validation dataset
    print("Modifying captions in the validation dataset:")
    caption_free_val_dataset = val_dataset.map(choose_sentence)

    # Push the modified datasets to the Hugging Face Hub with new split names
    caption_free_train_dataset.push_to_hub(DATASET, revision="caption-free")
    caption_free_val_dataset.push_to_hub(DATASET, revision="caption-free")

# Entry point of the script
if __name__ == "__main__":
    main()