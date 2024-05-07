import csv
import argparse

def remove_unlikely_words(prompt):
    """
    Removes unlikely words from a prompt.

    Args:
        prompt: The text prompt to be cleaned.

    Returns:
        The cleaned prompt with unlikely words removed.
    """
    unlikely_words = []

    a1_list = [f'{i}s' for i in range(1900, 2000)]
    a2_list = [f'{i}' for i in range(1900, 2000)]
    a3_list = [f'year {i}' for i in range(1900, 2000)]
    a4_list = [f'circa {i}' for i in range(1900, 2000)]
    b1_list = [f"{year[0]} {year[1]} {year[2]} {year[3]} s" for year in a1_list]
    b2_list = [f"{year[0]} {year[1]} {year[2]} {year[3]}" for year in a1_list]
    b3_list = [f"year {year[0]} {year[1]} {year[2]} {year[3]}" for year in a1_list]
    b4_list = [f"circa {year[0]} {year[1]} {year[2]} {year[3]}" for year in a1_list]

    words_list = [
        "black and white,", "black and white", "black & white,", "black & white", "circa", 
        "balck and white,", "monochrome,", "black-and-white,", "black-and-white photography,", 
        "black - and - white photography,", "monochrome bw,", "black white,", "black an white,",
        "grainy footage,", "grainy footage", "grainy photo,", "grainy photo", "b&w photo",
        "back and white", "back and white,", "monochrome contrast", "monochrome", "grainy",
        "grainy photograph,", "grainy photograph", "low contrast,", "low contrast", "b & w",
        "grainy black-and-white photo,", "bw", "bw,",  "grainy black-and-white photo",
        "b & w,", "b&w,", "b&w!,", "b&w", "black - and - white,", "bw photo,", "grainy  photo,",
        "black-and-white photo,", "black-and-white photo", "black - and - white photography",
        "b&w photo,", "monochromatic photo,", "grainy monochrome photo,", "monochromatic",
        "blurry photo,", "blurry,", "blurry photography,", "monochromatic photo",
        "black - and - white photograph,", "black - and - white photograph", "black on white,",
        "black on white", "black-and-white", "historical image,", "historical picture,", 
        "historical photo,", "historical photograph,", "archival photo,", "taken in the early",
        "taken in the late", "taken in the", "historic photograph,", "restored,", "restored", 
        "historical photo", "historical setting,",
        "historic photo,", "historic", "desaturated!!,", "desaturated!,", "desaturated,", "desaturated", 
        "taken in", "shot on leica", "shot on leica sl2", "sl2",
        "taken with a leica camera", "taken with a leica camera", "leica sl2", "leica", "setting", 
        "overcast day", "overcast weather", "slight overcast", "overcast", 
        "picture taken in", "photo taken in", 
        ", photo", ",  photo", ",   photo", ",    photo", ", photograph",
        ",,", ",,,", ",,,,", " ,", "  ,", "   ,", "    ,", 
    ]

    unlikely_words.extend(a1_list)
    unlikely_words.extend(a2_list)
    unlikely_words.extend(a3_list)
    unlikely_words.extend(a4_list)
    unlikely_words.extend(b1_list)
    unlikely_words.extend(b2_list)
    unlikely_words.extend(b3_list)
    unlikely_words.extend(b4_list)
    unlikely_words.extend(words_list)
    
    for word in unlikely_words:
        prompt = prompt.replace(word, "")
    return prompt

def clean_csv(input_file, output_file):
    """
    Reads a CSV file, cleans the 'prompt' column by removing unlikely words, and writes the modified data to a new CSV file.

    Args:
        input_file: Path to the input CSV file.
        output_file: Path to the output CSV file.
    """
    with open(input_file, 'r', newline='') as csvfile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(csvfile)
        writer = csv.writer(outfile)
        headers = next(reader)  # Read headers
        writer.writerow(headers)  # Write headers to output file

        for row in reader:
            image, prompt = row
            cleaned_prompt = remove_unlikely_words(prompt)
            writer.writerow([image, cleaned_prompt])

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_file', 
                        default=None, 
                        required=True, 
                        help='path for the original captions file')
    parser.add_argument('--output_file', 
                        default=None, 
                        required=True, 
                        help='path for the result of filterd captions file')
    args = parser.parse_args()

    clean_csv(args.input_file, args.output_file)
    print(f"\nCSV cleaned successfully!\nOutput written to {args.output_file}")

# Entry point of the script
if __name__ == "__main__":
    main()