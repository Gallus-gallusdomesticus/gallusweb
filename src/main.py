print("hello world")

from textnode import TextNode, TextType
from copystatic import copy_static
from generatepage import generate_page,generate_pages_recursive

def main():
    print(TextNode("test", TextType.LINKS, "https://www.boot.dev"))
    copy_static("./static", "./public")
    generate_pages_recursive("./content", "./template.html", "./public")


main()

