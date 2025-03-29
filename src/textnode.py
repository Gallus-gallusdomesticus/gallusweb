from enum import Enum

class TextType(Enum):
    NORMAL= "normal"
    BOLD="bold"
    ITALIC="italic"
    CODE="code"
    LINKS="links"
    IMAGES="images"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text=text
        self.text_type=text_type
        self.url=url

    def __eq__(self, other):
        return self.text==other_text and self.text_type==other.text_type and self.url==other.url

    def __repr__(self):
        text_type_string=self.text_type.value
        return f"TextNode({self.text}, {text_type_string}, {self.url})"
