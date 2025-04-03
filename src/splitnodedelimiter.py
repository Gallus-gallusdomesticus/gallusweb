from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes=[]
    
    for nodes in old_nodes:

        if nodes.text_type != TextType.TEXT:
            new_nodes.append(nodes)

        else:
            word_node_list = nodes.text.split(delimiter)
            i=0
            if len(word_node_list) % 2 == 0 and len(word_node_list) > 1:
                raise Exception("Invalid Markdown Syntax")
            while i < len(word_node_list):
                if i%2 == 0:
                    new_nodes.append(TextNode(word_node_list[i], nodes.text_type))
                else:
                    new_nodes.append(TextNode(word_node_list[i], text_type))
                i+=1
    return new_nodes
