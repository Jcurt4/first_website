from delimiter import *
from textnode import *


def text_to_textnodes(text):
    if not text:
        return [TextNode([], TEXT_TYPE_TEXT)]
    nodes = [TextNode(text, 'text')]
    nodes = split_nodes_delimiter(nodes, '**', TEXT_TYPE_BOLD)
    nodes = split_nodes_delimiter(nodes, '*', TEXT_TYPE_ITALIC)
    nodes = split_nodes_delimiter(nodes, '`', TEXT_TYPE_CODE)
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_image(nodes)
    return nodes