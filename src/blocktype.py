from enum import Enum

class BlockType(Enum):
    PARAGRAPH= "paragraph"
    HEADING="heading"
    CODE="code"
    QUOTE="quote"
    UNORDERED_LIST="unordered_list"
    ORDERED_LIST="ordered_list"

def block_to_block_type(block_text):
    if block_text.startswith(("# ", "## ","### ","#### ","##### ","###### ")):
        return BlockType.HEADING
    
    if block_text.startswith("```") and block_text.endswith("```"):
        return BlockType.CODE

    block_split=block_text.split("\n")

    block_quote=[]
    for block in block_split:
        block_quote.append(block.startswith(">"))
    if all(block_quote):
        return BlockType.QUOTE

    block_unordered=[]
    for block in block_split:
        block_unordered.append(block.startswith("- "))
    if all(block_unordered):
        return BlockType.UNORDERED_LIST
    
    
    list_number=[]
    for e in range(len(block_split)):
        list_number.append(f"{e+1}") #Make a list number for length of block split
    i=0
    block_ordered=[]
    while i < len(block_split):
        if ". " in block_split[i]:
            number_part, content_part = block_split[i].split(". ", 1)
            block_ordered.append(number_part==list_number[i])
            i+=1

        else:
            return BlockType.PARAGRAPH

    if all(block_ordered):
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH




