print("hello world")

from textnode import TextNode, TextType
from copystatic import copy_static
from generatepage import generate_page

def main():
    print(TextNode("test", TextType.LINKS, "https://www.boot.dev"))
    copy_static("./static", "./public")
    generate_page("./content/index.md", "template.html", "./public/index.html")


main()

