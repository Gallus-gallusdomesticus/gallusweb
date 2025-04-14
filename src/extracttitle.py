from markdowntoblocks import markdown_to_blocks
from blocktype import block_to_block_type, BlockType


def extract_title(markdown):
    block_list=markdown_to_blocks(markdown)
    for block in block_list:
        if block.startswith("# "):
            return block[2:]
    raise Exception("Title not found")