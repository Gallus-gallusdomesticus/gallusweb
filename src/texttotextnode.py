from textnode import TextNode, TextType
from splitnodedelimiter import split_nodes_delimiter, split_nodes_image, split_nodes_links

def text_to_textnodes(text):
    textnode_list=[TextNode(text, TextType.TEXT)]
    delimiter_list={TextType.BOLD:"**", TextType.ITALIC:"_", TextType.CODE:"`"}
    for key in delimiter_list:
        textnode_list=split_nodes_delimiter(textnode_list, delimiter_list[key], key)
    
    textnode_list=split_nodes_image(textnode_list)
    textnode_list=split_nodes_links(textnode_list)
    

    return textnode_list

