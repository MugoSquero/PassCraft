import argparse
import re
import os
from os import system as xcmd
from itertools import product
from tqdm import tqdm
from colorama import Fore, Style
from platform import system

def process_templates(templates, values, keep_missing, min_length):
    passwords = []
    with tqdm(total=len(templates), desc="Generating Passwords...", unit="line", leave=True, dynamic_ncols=True) as pbar:
        for template in templates:
            placeholders = re.findall(r'\[(.*?)\]', template)
            placeholder_values = []
            for placeholder in placeholders:
                if placeholder in values and values[placeholder]:
                    placeholder_values.append(values[placeholder])
    
            if not placeholder_values:
                continue
    
            combinations = product(*placeholder_values)
            for combination in combinations:
                password = template
                for placeholder, value in zip(placeholders, combination):
                    password = password.replace('[' + placeholder + ']', value)
                if len(password) >= min_length and password not in passwords:
                    passwords.append(password)
            pbar.update(1)

    return passwords




def main():
    # Check the operating system and set console color for Windows
    if system() == "Windows":
        xcmd("color")
        
    # Fancy Logo
    print(Fore.RED + """                                                                                                      
88888888ba                                       ,ad8888ba,                              ad88           
88      "8b                                     d8"'    `"8b                            d8"      ,d     
88      ,8P                                    d8'                                      88       88     
88aaaaaa8P'  ,adPPYYba,  ,adPPYba,  ,adPPYba,  88             8b,dPPYba,  ,adPPYYba,  MM88MMM  MM88MMM  
88\"""\"""'    ""     `Y8  I8[    ""  I8[    ""  88             88P'   "Y8  ""     `Y8    88       88     
88           ,adPPPPP88   `"Y8ba,    `"Y8ba,   Y8,            88          ,adPPPPP88    88       88     
88           88,    ,88  aa    ]8I  aa    ]8I   Y8a.    .a8P  88          88,    ,88    88       88,    
88           `"8bbdP"Y8  `"YbbdP"'  `"YbbdP"'    `"Y8888Y"'   88          `"8bbdP"Y8    88       "Y888  
    """ + Style.RESET_ALL)
    # Command-line argument parsing
    parser = argparse.ArgumentParser(description=Fore.GREEN+'PassCraft is a powerful tool designed to generate unique and targeted wordlists for password cracking or data analysis purposes. By utilizing user-defined templates and providing corresponding values, this tool generates customized wordlists that match specific patterns or criteria. Enhance your password cracking or data analysis efforts with tailored wordlists created using this efficient and flexible generator. Generate wordlists optimized for your specific needs and maximize your success in targeted attacks or data exploration tasks.'+Style.RESET_ALL)
    parser.add_argument('-k', '--keep-missing', action='store_true', help='Preserves the generated password structure despite any empty/missing values')
    parser.add_argument('-o', '--output-file', help='The output file to save the generated passwords')
    parser.add_argument('-t', '--template-dir', default="templates", help='Template file path (default: templates)')
    parser.add_argument('-m', '--min-length', type=int, default=6, help='Minimum password length (default: 6)')
    args = parser.parse_args()
    
    keep_missing = args.keep_missing
    min_length = args.min_length
    output_file = args.output_file
    template_dir = args.template_dir

    # Read templates from a directory
    templates = []
    if os.path.isdir(template_dir):
        for filename in os.listdir(template_dir):
            file_path = os.path.join(template_dir, filename)
            if os.path.isfile(file_path):
                with open(file_path, 'r') as file:
                    templates += file.read().splitlines()
    else:
        print(f"The '{template_dir}' directory does not exist.")

    # Get the list of placeholders from the templates
    placeholders = set(re.findall(r'\[(.*?)\]', ' '.join(templates)))

    # Prompt the user for values
    values = {}
    print("Answer the questions as clear as possible, be creative. (multiple values separated by commas, no spaces)")
    try:
        for key in placeholders:
            value = input(f"Enter value for '{key}': ")
            values[key] = [v.strip() for v in value.split(',')]
    except:
        print("\nAn error occured, exiting!")
        exit(0)

    # Process the templates and generate passwords 
    passwords = process_templates(templates, values, keep_missing, min_length)


    if output_file:
        # Save the generated passwords
        with open(output_file, 'w') as file:
            for password in passwords:
                file.write(f"{password}\n")
    else:
        # Print the generated passwords
        for password in passwords:
            print(password)

if __name__ == '__main__':
    main()
