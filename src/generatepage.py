from markdowntohtml import markdown_to_html_node
from extracttitle import extract_title
from copystatic import copy_static
from htmlnode import ParentNode
import os

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    if os.path.exists(from_path)==False:
        raise Exception(f"Source path does not exist")
    if os.path.exists(template_path)==False:
        raise Exception(f"Template path does not exist")   

    parent_dir = os.path.dirname(dest_path)
    if os.path.exists(parent_dir)==False:
        os.makedirs(parent_dir)

    with open(from_path, "r") as markdown_content:
        markdown_file=markdown_content.read()

    with open(template_path, "r") as template_content:
        template_file = template_content.read()

    html_from_markdown = markdown_to_html_node(markdown_file).to_html()
    title=extract_title(markdown_file)
    template_file=template_file.replace("{{ Title }}", title)
    template_file=template_file.replace("{{ Content }}", html_from_markdown)

    with open(dest_path, "w") as dest_file:
        dest_file.write(template_file)

