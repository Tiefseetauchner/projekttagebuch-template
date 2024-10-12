#!/usr/bin/python

import json
import os
import subprocess

print("Generating Variables...")

def escape_latex_special_chars(value):
    return value.replace(',', '{,}')  # Escape commas

# Load JSON data from the file
with open('variables.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Create a LaTeX file
with open('variables.tex', 'w', encoding='utf-8') as f:
    # Iterate through key-value pairs in the JSON data
    for key, value in data.items():
        if isinstance(value, list):
            # If the value is a list, store it as a comma-separated list
            escaped_value = [escape_latex_special_chars(item) for item in value]
            latex_command = f"\\newcommand{{\\{key.replace(' ', '_')}}}{{{','.join(escaped_value)}}}\n"
        else:
            # Write LaTeX command, converting spaces to underscores for the command name
            latex_command = f"\\newcommand{{\\{key.replace(' ', '_')}}}{{{value}}}\n"

        f.write(latex_command)

print("LaTeX commands generated and saved to 'variables.tex'")
print()
print("Generating daily report TeXs...")

# Define the directories
input_dir = 'TagesberichteMD'
output_dir = 'TagesberichteTeX'

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Iterate over all files in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith('.md'):
        input_path = os.path.join(input_dir, filename)
        output_filename = os.path.splitext(filename)[0] + '.tex'
        output_path = os.path.join(output_dir, output_filename)

        # Run Pandoc command to convert the Markdown file to TeX
        try:
            subprocess.run(['pandoc', input_path, '-o', output_path], check=True)
            print(f"Converted {input_path} to {output_path}")
        except subprocess.CalledProcessError as e:
            print(f"Error converting {input_path}: {e}")

with open("tagesberichte_generated.tex", "w+", encoding='utf-8') as combined:
    for filename in os.listdir(output_dir):
        input_path = os.path.join(output_dir, filename)
        with open(input_path, 'r', encoding='utf-8') as report_content:
            combined.write(report_content.read())


print("LaTeX files generated and combined to 'tagesberichte_generated.tex'")
print()
print("Generating PDF...")

subprocess.run(["pdflatex", "-synctex=1", "-interaction=nonstopmode", "projekttagebuch.tex"])

print("PDF generated and saved under 'projekttagebuch.pdf'")
