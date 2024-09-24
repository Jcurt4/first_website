from textnode import TextNode


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != 'text':
            new_nodes.append(node)
        else:
            start_index = node.text.find(delimiter)
            if start_index != -1:
                end_index = node.text.find(delimiter, start_index + len(delimiter))
                if end_index != -1:
                    before_delimiter = node.text[0: start_index]
                    inside_delimiter = node.text[(start_index + len(delimiter)):end_index]
                    after_delimiter = node.text[(end_index + len(delimiter)):]

                    if before_delimiter:
                        new_nodes.append(TextNode(before_delimiter, 'text'))
                    if inside_delimiter:
                        new_nodes.append(TextNode(inside_delimiter, text_type))
                    if after_delimiter:
                        new_nodes.extend(split_nodes_delimiter([TextNode(after_delimiter, 'text')], delimiter, text_type))

                else:
                    raise Exception(f"Delimiter {delimiter} not closed in text: {node.text}")

            else:
                new_nodes.append(node)

    return new_nodes
            