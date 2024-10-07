from textnode import TextNode


def split_nodes_delimiter(old_nodes, delimiter, text_type='text'):
    new_nodes = []
    
    if delimiter is None or delimiter == '':
        raise ValueError('Delimiter cannot be None or an empty string.')
    
    for node in old_nodes:
        if node.text_type != 'text':
            new_nodes.append(node)
            continue
        
        parts = node.text.split(delimiter)
        if len(parts) % 2 == 0:
            raise ValueError(f"Mismatched delimiters in text: {node.text}")
        
        if delimiter not in node.text:
            new_nodes.append(node)
        else:
            for i, part in enumerate(parts):
                if part:  # only create nodes for non-empty parts
                    new_type = text_type if i % 2 else 'text'
                    new_nodes.append(TextNode(part, new_type))
        
    return new_nodes
            