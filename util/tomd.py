import requests
import subprocess

# URL of the JSON file
json_url = "https://dev-api.velocityln.ai/swagger/v1/swagger.json" ## Path of the JSON file to download and convert to MD file

json_file_path = "filetoconvert/" ## This is folder path where your JSON or YAML file will be downloaded
json_file_name = "VLN_API.json" ## This is your file name which is to be converted to MD file
md_file_name = "../source/includes/_cust.md" ## This is your md file name


# Construct the full paths for the input JSON file and the output MD file
input_file = json_file_path + json_file_name
output_file = md_file_name

# Download the JSON file from the URL
response = requests.get(json_url)
if response.status_code == 200:
    # Save the JSON content to a file
    with open(input_file, 'w') as json_file:
        json_file.write(response.text)
else:
    print(f"Failed to download the file: {response.status_code}")
    exit(1)
    
# Construct the widdershins command
command = f"widdershins {input_file} -o {output_file}"

# Execute the command using subprocess
subprocess.run(command, shell=True, check=True)



# Replace the specified content with null in the generated Markdown file as this content is already there as part of index.html.md file
with open(output_file, 'r') as file:
    md_content = file.read()

md_content = md_content.replace(
    '''---
title: SLP Service1.0 v1.0
language_tabs:
  - shell: Shell
  - http: HTTP
  - javascript: JavaScript
  - ruby: Ruby
  - python: Python
  - php: PHP
  - java: Java
  - go: Go
toc_footers: []
includes: []
search: true
highlight_theme: darkula
headingLevel: 2

---''', '')

# Write the modified content back to the Markdown file
with open(output_file, 'w') as file:
    file.write(md_content)