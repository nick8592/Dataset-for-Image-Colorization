# Generate captions specific for "Stable Diffusion 2".
export IMAGE_FOLDER="train2017"
export OUTPUT_FOLDER="coco_captions_sdv2"
export OUTPUT_FILENAME="train2017"

python captions_generator.py \
    --clip='ViT-H-14/laion2b_s32b_b79k' \
    --device='cuda' \
    --mode='fast' \
    --image_folder=$IMAGE_FOLDER \
    --output_folder=$OUTPUT_FOLDER \
    --output_filename=$OUTPUT_FILENAME


# Filter dataset to remove unlikely words from generated captions.
export INPUT_FILE="/home/nick/Documents/code/control-color/coco_captions_sdv2/train2017.csv"
export OUTPUT_FILE="/home/nick/Documents/code/control-color/coco_captions_sdv2/train2017_r.csv"

python csv_filter.py \
    --input_file=$INPUT_FILE \
    --output_file=$OUTPUT_FILE

# # Push custom caption dataset to Hugginface
export DATASET='nickpai/coco2017-colorization'
export CAPTIONS_PATH="coco_captions_sdv2/train2017_r.csv"
export SPLIT="train"
export REVISION="custom-caption"

python dataset_map_custom.py \
    --dataset=$DATASET \
    --captions_path=$CAPTIONS_PATH \
    --split=$SPLIT \
    --revision=$REVISION





