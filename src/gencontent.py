import os
from markdown_to_html import markdown_to_html_node

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            title_text = line[2:]
            title_text = title_text.strip()
            return title_text
    raise Exception("no h1 title found")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    #read markdown file
    from_file = open(from_path, "r")
    markdown_content = from_file.read()
    from_file.close()
    #read template file
    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()
    #markdown to html
    node = markdown_to_html_node(markdown_content)
    html = node.to_html()
    #extract title
    title= extract_title(markdown_content)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)
    #ensure destination exists and write file
    dest_dir = os.path.dirname(dest_path)
    if dest_dir != "":
        os.makedirs(dest_dir, exist_ok=True)

    dest_file = open(dest_path, "w")
    dest_file.write(template)
    dest_file.close()