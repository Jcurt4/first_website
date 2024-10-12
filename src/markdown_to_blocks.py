import re

BLOCK_TYPE_PARAGRAPH = 'paragraph'
BLOCK_TYPE_HEADER = 'header'
BLOCK_TYPE_UNORDERED_LIST = 'unordered_list'
BLOCK_TYPE_ORDERED_LIST = 'ordered_list'
BLOCK_TYPE_QUOTE = 'quote'
BLOCK_TYPE_CODE = 'code'

def markdown_to_blocks(markdown):
    filtered_blocks = [block.strip() for block in markdown.split('\n\n') if block.strip()]
    return filtered_blocks


def block_to_block_type(block):
    if block.startswith(
        ('# ', '## ', '### ', '#### ', '##### ', '###### ') 
    ):
        return BLOCK_TYPE_HEADER
    
    elif block.startswith('* ') or block.startswith('- '):
        lines = block.split('\n')
        if all(line.startswith('* ') or line.startswith('- ') for line in lines):
            return BLOCK_TYPE_UNORDERED_LIST
        
    elif block.startswith('```') and block.endswith('```'):
        return BLOCK_TYPE_CODE
    
    elif block.startswith('>'):
        lines = block.split('\n')
        if all(line.startswith('> ') for line in lines):
            return BLOCK_TYPE_QUOTE
        
    elif block.startswith('1. '):
        lines = block.split('\n')
        pattern = re.compile(r'^(\d+)\.\s', re.MULTILINE)
        matches = pattern.findall(block)
        is_ordered = True
        if len(lines) == len(matches):
            for i, num in enumerate(matches):
                if int(num) != i+1:
                    is_ordered = False
                    break
            if is_ordered:
                return BLOCK_TYPE_ORDERED_LIST
        return BLOCK_TYPE_PARAGRAPH

    return BLOCK_TYPE_PARAGRAPH
