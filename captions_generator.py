# pip install clip-interrogator
# https://github.com/pharmapsychotic/clip-interrogator/blob/main/run_cli.py
#!/usr/bin/env python3
import argparse
import csv
import os
import requests
import torch
from tqdm import tqdm
from PIL import Image
from clip_interrogator import Interrogator, Config, list_clip_models

def inference(ci, image, mode):
    image = image.convert('RGB')
    if mode == 'best':
        return ci.interrogate(image)
    elif mode == 'classic':
        return ci.interrogate_classic(image)
    else:
        return ci.interrogate_fast(image)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clip', 
                        default='ViT-H-14/laion2b_s32b_b79k', 
                        choices=['ViT-L-14/openai', 'ViT-H-14/laion2b_s32b_b79k'], 
                        help='name of caption model to use')
    parser.add_argument('-d', '--device', 
                        default='auto', 
                        help='device to use (auto, cuda or cpu)')
    parser.add_argument('--image_folder', 
                        default=None, 
                        help='path to folder of images')
    parser.add_argument('--output_folder', 
                        default=None, 
                        required=True, 
                        help='path to folder of output captions')
    parser.add_argument('--output_filename', 
                        default=None, 
                        required=True, 
                        help='name for the result of output captions file')
    parser.add_argument('-i', '--image', default=None, help='image file or url')
    parser.add_argument('-m', '--mode', default='best', help='best, classic, or fast')
    parser.add_argument("--lowvram", action='store_true', help="Optimize settings for low VRAM")

    args = parser.parse_args()
    if not args.image_folder and not args.image:
        parser.print_help()
        exit(1)

    if args.image_folder is not None and args.image is not None:
        print("Specify a folder or batch processing or a single image, not both")
        exit(1)

    # validate clip model name
    models = list_clip_models()
    if args.clip not in models:
        print(f"Could not find CLIP model {args.clip}!")
        print(f"    available models: {models}")
        exit(1)

    # select device
    if args.device == 'auto':
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        if not torch.cuda.is_available():
            print("CUDA is not available, using CPU. Warning: this will be very slow!")
    else:
        device = torch.device(args.device)

    # generate a nice prompt
    config = Config(device=device, clip_model_name=args.clip)
    if args.lowvram:
        config.apply_low_vram_defaults()
    ci = Interrogator(config)

    # Check if the output folder exists
    if os.path.exists(args.output_folder):
        print(f"Output folder '{args.output_folder}' already exists.")
    else:
        print(f"Output folder '{args.output_folder}' does not exist. Creating new one...")
        os.mkdir(args.output_folder)

    # process single image
    if args.image is not None:
        image_path = args.image
        if str(image_path).startswith('http://') or str(image_path).startswith('https://'):
            image = Image.open(requests.get(image_path, stream=True).raw).convert('RGB')
        else:
            image = Image.open(image_path).convert('RGB')
        if not image:
            print(f'Error opening image {image_path}')
            exit(1)
        print(inference(ci, image, args.mode))

    # process folder of images
    elif args.image_folder is not None:
        if not os.path.exists(args.image_folder):
            print(f'The folder {args.image_folder} does not exist!')
            exit(1)

        csv_path = os.path.join(args.output_folder, f"{args.output_filename}.csv")
        with open(csv_path, 'w', encoding='utf-8', newline='') as f:
            w = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
            w.writerow(['image', 'prompt'])
        
        files = [f for f in sorted(os.listdir(args.image_folder)) if f.endswith('.jpg') or  f.endswith('.png')]
        for i, file in enumerate(tqdm(files, total=len(files))):
            image_path = os.path.join(args.image_folder, file)
            image = Image.open(image_path).convert('L') # convert to grayscale
            prompt = inference(ci, image, args.mode)
            print(prompt)
            print("\n")

            if len(prompt):
                with open(csv_path, 'a', encoding='utf-8', newline='') as f:
                    w = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
                    w.writerow([image_path, prompt])

        print(f"\n\n\n\nGenerated {len(files)} and saved to {csv_path}, enjoy!")

if __name__ == "__main__":
    main()