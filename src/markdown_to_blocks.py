

def markdown_to_blocks(markdown):
    filtered_blocks = [block.strip() for block in markdown.split('\n\n') if block.strip()]
    return filtered_blocks