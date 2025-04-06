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



#Split nodes for images and links

from extractlinks import extract_markdown_images, extract_markdown_links

def split_nodes_image(old_nodes):
    new_nodes=[]
    
    for nodes in old_nodes: #each node in old nodes
        
        extracted=extract_markdown_images(nodes.text) #extract the markdown in the node

        if extracted == []: #if there is nothing to extract just return as it is
            new_nodes.extend([nodes])

        else:
            remaining=nodes.text
            for extract in extracted: #for each list that get extracted
                splitted_nodes = remaining.split(f"![{extract[0]}]({extract[1]})",1) #split the nodes and remove the extracted once
                if splitted_nodes[0]: #if there is something in beginning of the splitted nodes
                    new_nodes.extend([TextNode(splitted_nodes[0],TextType.TEXT)])
                new_nodes.extend([TextNode(extract[0], TextType.IMAGES, extract[1])]) #append the extracted to new_nodes    
                remaining=splitted_nodes[1] #update the remaining to the remainder
            if remaining: #if there is remainder on the end
                new_nodes.extend([TextNode(remaining, TextType.TEXT)])

    return new_nodes

def split_nodes_links(old_nodes):
    new_nodes=[]
    
    for nodes in old_nodes: #each node in old nodes
        
        extracted=extract_markdown_links(nodes.text) #extract the markdown in the node

        if extracted == []: #if there is nothing to extract just return as it is
            new_nodes.extend([nodes])

        else:
            remaining=nodes.text
            for extract in extracted: #for each list that get extracted
                splitted_nodes = remaining.split(f"[{extract[0]}]({extract[1]})",1) #split the nodes and remove the extracted once
                if splitted_nodes[0]: #if there is something in beginning of the splitted nodes
                    new_nodes.extend([TextNode(splitted_nodes[0],TextType.TEXT)])
                new_nodes.extend([TextNode(extract[0], TextType.LINKS, extract[1])]) #append the extracted to new_nodes    
                remaining=splitted_nodes[1] #update the remaining to the remainder
            if remaining: #if there is remainder on the end
                new_nodes.extend([TextNode(remaining, TextType.TEXT)])

    return new_nodes


