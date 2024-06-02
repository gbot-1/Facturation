import os
import subprocess
import shutil


def generate_main_latex(template_path, output_path, data_dict):
    # Read the template
    try:
        with open(template_path, 'r', encoding='utf-8') as file:
            template_content = file.read()
    except Exception as e:
        print(f"Error reading template: {e}")
        return

    # Replace placeholders with actual data
    for key, value in data_dict.items():
        placeholder = f'{{{{ {key} }}}}'  # Correct placeholder format
        template_content = template_content.replace(placeholder, str(value))
    # Write the output to a new file
    try:
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(template_content)
    except Exception as e:
        print(f"Error writing to output file: {e}")

def compile_tex_to_pdf(tex_folder, tex_filename):
    # Construct the full path to the TeX file and the output PDF file
    tex_path = os.path.join(tex_folder, tex_filename)

    # Check if the specified TeX file exists
    if os.path.exists(tex_path):
        # Compile the TeX file into a PDF
        command = f"pdflatex -output-directory {tex_folder} {tex_path}"
        subprocess.run(command, shell=True, check=True)
    else:
        print(f"The file {tex_path} does not exist.")

def move_and_rename_file(src_folder, dest_folder, src_filename, dest_filename):
    """
    Moves a file from src_folder to dest_folder and renames it.

    :param src_folder: Source folder path
    :param dest_folder: Destination folder path
    :param src_filename: Name of the file in the source folder
    :param dest_filename: New name for the file in the destination folder
    """
    # Construct the full path for the source and destination files
    src_file_path = os.path.join(src_folder, src_filename)
    dest_file_path = os.path.join(dest_folder, dest_filename)

    # Ensure the destination folder exists
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    # Move and rename the file
    shutil.move(src_file_path, dest_file_path)
    print(f"File moved and renamed from {src_file_path} to {dest_file_path}")

def generate_main_latex(template_path, output_path, data_dict):
    # Read the template
    try:
        with open(template_path, 'r', encoding='utf-8') as file:
            template_content = file.read()
    except Exception as e:
        print(f"Error reading template: {e}")
        return

    # Replace placeholders with actual data
    for key, value in data_dict.items():
        placeholder = f'{{{{ {key} }}}}'  # Correct placeholder format
        template_content = template_content.replace(placeholder, str(value))
    # Write the output to a new file
    try:
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(template_content)
    except Exception as e:
        print(f"Error writing to output file: {e}")