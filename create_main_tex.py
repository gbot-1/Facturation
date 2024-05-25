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