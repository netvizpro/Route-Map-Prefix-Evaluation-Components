import os

html_file_path = r"c:\Users\Phyo\Downloads\Automate Projects\route-map-analyzer.html"
css_file_path = r"c:\Users\Phyo\Downloads\Automate Projects\new_styles.css"

# Read the new CSS
with open(css_file_path, 'r', encoding='utf-8') as f:
    new_css = f.read()

# Read the HTML file
with open(html_file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find start and end of style block
start_idx = -1
end_idx = -1

for i, line in enumerate(lines):
    if '<style>' in line:
        start_idx = i
    if '</style>' in line:
        end_idx = i
        break

if start_idx != -1 and end_idx != -1:
    # Replace the block
    # We replace from start_idx to end_idx inclusive with the new_css
    # new_css already contains <style>...</style> tags from the previous step?
    # Let's check the content of new_styles.css.
    # It starts with <link ...> and ends with </style>.
    # So we should replace everything from start_idx to end_idx with new_css.
    
    new_lines = lines[:start_idx] + [new_css + '\n'] + lines[end_idx+1:]
    
    with open(html_file_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    print("Successfully updated CSS.")
else:
    print("Could not find style block.")
