print("hello world")

from textnode import TextNode, TextType
from copystatic import copy_static
from generatepage import generate_page,generate_pages_recursive
import sys

base=sys.argv

if len(sys.argv)==1:
    base="/"
else:
    base=sys.argv[1]


def main():
    print(TextNode("test", TextType.LINKS, "https://www.boot.dev"))
    copy_static("./static", "./docs")
    generate_pages_recursive("./content", "./template.html", "./docs", base)


main()

