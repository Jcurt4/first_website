from htmlnode import *


TEXT_TYPE_TEXT = "text"
TEXT_TYPE_BOLD = "bold"
TEXT_TYPE_ITALIC = "italic"
TEXT_TYPE_CODE = "code"
TEXT_TYPE_LINK = "link"
TEXT_TYPE_IMAGE = "image"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url


    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return False
        return (self.text == other.text and
                self.text_type == other.text_type and
                self.url == other.url)
    def __repr__(self):
        return f"TextNode({self.text!r}, {self.text_type!r}, {self.url!r})"
    

    
def text_node_to_html_node(text_node):
    tag_map = {
        None: ("", text_node.text),
        "": ("", text_node.text),
        "text": ("", text_node.text),
        "bold": ("b", text_node.text),
        "italic": ("i", text_node.text),
        "code": ("code", text_node.text),
        "link": ("a", text_node.text, {"href": text_node.url}),
        "image": ("img", "", {"src": text_node.url, "alt": text_node.text}),
    }

    if text_node.text_type not in tag_map:
        raise ValueError(f"Unsupported text type: {text_node.text_type}")

    tag, value, *props = tag_map[text_node.text_type]
    return LeafNode(tag=tag, value=value, props=(props[0] if props else None))