import re
from enum import Enum

from textnode import TextNode, TextType

class BlockType(Enum):
    PARAGRAPH = 'paragraph'
    HEADING = 'heading'
    CODE = 'code'
    QUOTE = 'quote'
    ULIST = 'unordered_list'
    OLIST = 'ordered_list'

def block_to_block_type(block):
    lines = block.split('/n')
    if block.startswith('```') and block.endswith('```'): return BlockType.CODE
    if block.startswith('#') and re.match(r'^\#{1,6} ', block): return BlockType.HEADING
    if block.startswith('>'):
        for line in lines:
            if not line.startswith('>'): return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if block.startswith('- '):
        for line in lines:
            if not line.startswith('- '): return BlockType.PARAGRAPH
        return BlockType.ULIST
    if re.match(r"^\d+\. ", block):
        for line in lines:
            if not re.match(r"^\d+\. ", line): return BlockType.PARAGRAPH
        return BlockType.OLIST

    return BlockType.PARAGRAPH

def markdown_to_blocks(markdown):
    split_blocks = markdown.split('\n\n')
    split_blocks = [re.sub(' +', ' ', i.strip()) for i in split_blocks if i != '']

    return split_blocks



if __name__ == '__main__':
    md = """
        ###### This is 6 heading
        This is **bolded** paragraph

        This is another paragraph with _italic_ text and `code` here
        This is the same paragraph on a new line

        - This is a list
        - with items
    """
    blocks = markdown_to_blocks(md)
    block = "1. list\n2. items"
    mkdwn_to_blk = block_to_block_type(block)
    print(mkdwn_to_blk)

