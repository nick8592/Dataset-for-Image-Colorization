# map custom captions result with original dataset
import random
import argparse
import pandas as pd
from tqdm import tqdm
from datasets import load_dataset

parser = argparse.ArgumentParser()
parser.add_argument('--dataset', 
                    default=None, 
                    required=True, 
                    help='dataset from hugging face')
parser.add_argument('--captions_path', 
                    default=None, 
                    required=True, 
                    help='path for the result of output captions file')
parser.add_argument('--split', 
                    default=None, 
                    choices=['train', 'validation'],
                    required=True,
                    help='choose split for the dataset')
parser.add_argument('--revision', 
                    default=None, 
                    required=True,
                    help='name for the revision')
args = parser.parse_args()

df_csv = pd.read_csv(args.captions_path, index_col='image')

# Function to replace original caption with custom caption
def choose_sentence(example):
    prompt = df_csv.loc[example['file_name']]
    example["captions"] = prompt.to_list()
    return example

# Load split of the dataset
dataset = load_dataset(args.dataset, split=args.split)

# https://huggingface.co/docs/datasets/process#map
# Modify captions in the dataset
print("Modifying captions in the dataset:")
castom_caption_dataset = dataset.map(choose_sentence)

# Push the modified datasets to the Hugging Face Hub with new split names
castom_caption_dataset.push_to_hub(args.dataset, revision=args.revision)
