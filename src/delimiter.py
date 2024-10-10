from textnode import * # Custom class
import re # Regular expressions


def split_nodes_delimiter(old_nodes, delimiter, text_type='text'):
    if not old_nodes:
        return []

    new_nodes = []
    
    if delimiter is None or delimiter == '':
        raise ValueError('Delimiter cannot be None or an empty string.')
    
    for node in old_nodes:
        if node.text_type != 'text':
            new_nodes.append(node)
            continue
        
        parts = node.text.split(delimiter)
        if len(parts) % 2 == 0:
            raise ValueError(f"Mismatched or unpaired delimiters in text: {node.text}")
        
        if delimiter not in node.text:
            new_nodes.append(node)
        else:
            for i, part in enumerate(parts):
                if part or (i > 0 and i < len(parts) - 1):  # Skip empty parts at start/end
                    new_type = text_type if i % 2 else 'text'
                    new_nodes.append(TextNode(part, new_type))
        
    return new_nodes
            


def extract_markdown_images(text):
    image_pattern = r'!\[(.*?)\]\s*\(((?:[^()]|\([^()]*\))*)\)'
    matches = re.findall(image_pattern, text)
    return matches


def split_nodes_image(old_nodes):
    new_nodes = []
    image_pattern = r'!\[(.*?)\]\s*\(((?:[^()]|\([^()]*\))*)\)'

    for node in old_nodes:

        if not re.search(image_pattern, node.text):
            new_nodes.append(node)
            continue

        parts = re.split(image_pattern, node.text)

        for i, part in enumerate(parts):
            if i % 3 == 0:
                if part.strip():
                    new_nodes.append(TextNode(part, 'text'))
            elif i % 3 == 1:
                alt_text = part
            elif i % 3 == 2:
                new_nodes.append(TextNode(alt_text, 'image', part))

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    link_pattern = r'\[(.*?)\]\s*\(((?:[^()]|\([^()]*\))*)\)'

    for node in old_nodes:

        if not re.search(link_pattern, node.text):
            new_nodes.append(node)
            continue

        parts = re.split(link_pattern, node.text)

        for i, part in enumerate(parts):
            if i % 3 == 0:
                if part.strip():
                    new_nodes.append(TextNode(part, 'text'))
            elif i % 3 == 1:
                link_text = part
            elif i % 3 == 2:
                new_nodes.append(TextNode(link_text, 'link', part))

    return new_nodes