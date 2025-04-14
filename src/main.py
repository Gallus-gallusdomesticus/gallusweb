print("hello world")

from textnode import TextNode, TextType
from copystatic import copy_static

def main():
    print(TextNode("test", TextType.LINKS, "https://www.boot.dev"))
    copy_static("./static", "./public")


main()

