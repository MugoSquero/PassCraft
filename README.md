# PassCraft: Custom Password Generation Tool

PassCraft is a versatile tool designed to generate customized wordlists for password cracking, data analysis, and more. By using user-defined templates and corresponding values, PassCraft generates tailored wordlists that match specific patterns or criteria. Enhance your password cracking or data analysis efforts with unique and targeted wordlists created using this efficient and flexible generator.

## Features

- Generate customized wordlists based on user-defined templates.
- Template files can be stored in a directory for easier organization.

## TODO

- Utilize modifiers like `[name.upper]`, `[pet.reverse]`, etc., to enhance wordlist variety.

## Usage

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/MugoSquero/PassCraft.git
   cd PassCraft
   ```

2. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Script:**

   ```bash
   python passcraft.py -k -m 8 -o generated_passwords.txt
   ```

   - `-k` or `--keep-missing`: Preserve password structure even with missing values.
   - `-m` or `--min-length`: Set a minimum password length (default is 6).
   - `-o` or `--output-file`: Specify an output file to save generated passwords.

4. **Provide Template Values:**

   - Answer the questions as clearly as possible.
   - For multiple values, separate them with commas (no spaces).

5. **Generated Passwords:**

   The generated passwords will be printed to the console or saved to the specified output file.

## Templates

- Define templates in separate files within the `templates` directory.
- Use placeholders like `[name]`, `[pet]`, etc., in your templates.

## Examples

- Generate passwords with default settings:

  ```bash
  python passcraft.py
  ```

- Generate passwords with a minimum length of 10 characters and save to a file:

  ```bash
  python passcraft.py -m 10 -o output_passwords.txt
  ```

## License

This project is licensed under the AGPLv3 License.