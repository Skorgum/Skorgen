from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unorderd_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block: str) -> BlockType:
    lines = block.split("\n")
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    
    for i in range(1, 7):
        if block.startswith("#" * i + " "):
            return BlockType.HEADING
      
    for i, line in enumerate(lines, start=1):
        expected_prefix = f"{i}. "
        if not line.startswith(expected_prefix):
            break
    else:
        return BlockType.ORDERED_LIST
    
    for line in lines:
        if not line.startswith("- "):
            break
    else:
        return BlockType.UNORDERED_LIST
    
    for line in lines:
        if not line.startswith(">"):
            break
    else:
        return BlockType.QUOTE
    
    return BlockType.PARAGRAPH

def markdown_to_blocks(markdown):
    result = []
    new_strings = markdown.split("\n\n")
    for new_string in new_strings:
        new_string = new_string.strip()
        if not new_string:
            continue
        result.append(new_string)
    return result

