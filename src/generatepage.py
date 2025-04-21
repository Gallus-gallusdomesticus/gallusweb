from markdowntohtml import markdown_to_html_node
from extracttitle import extract_title
from copystatic import copy_static
from htmlnode import ParentNode
from pathlib import Path
import os


def generate_page(from_path, template_path, dest_path, basepath):
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
    template_file=template_file.replace('href="/', f'href="{basepath}')
    template_file=template_file.replace('src="/', f'src="{basepath}')

    with open(dest_path, "w") as dest_file:
        dest_file.write(template_file)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    p=Path(dir_path_content) #make the path files
    markdown_list=list(p.glob("*.md"))  #make the list of the path
    list_dir=os.listdir(dir_path_content)
    if list_dir==[]: #return if list directory empty
        return

    #create destination directory if there is markdown file
    if os.path.exists(dest_dir_path)==False and markdown_list:
            os.makedirs(dest_dir_path)



    #process markdown files
    for markdown in markdown_list:
        markdown_path=str(markdown)
        markdown_filename=os.path.basename(markdown_path)
        html_name=markdown_filename.replace(".md", ".html")
            
        combined_markdown_destination=os.path.join(dest_dir_path, html_name)
        generate_page(markdown_path, template_path, combined_markdown_destination, basepath)

    #process the directories
    for dir in list_dir:
        combined_directory=os.path.join(dir_path_content, dir)
        
        if os.path.isdir(combined_directory)==True:
            combined_markdown_destination=os.path.join(dest_dir_path,dir)
            generate_pages_recursive(combined_directory,template_path, combined_markdown_destination, basepath)
        
        



        

