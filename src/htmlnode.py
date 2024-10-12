class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None:
            return '' #this is just hanndling the TypeError by giving nothing back.  probably sloppy.  
        return (' ' + ' '.join([f'{key}="{value}"' for key, value in self.props.items()]))
    
    def __repr__(self):
        return f'tag={self.tag}, value={self.value}, children={self.children}, props={self.props}'
    

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError('Must provide a value')
        if self.tag == 'text':
            raise ValueError('Try using "" or None')
        if self.tag is None or self.tag == '':
            return self.value
        self_closing_tags = ["img", "br", "hr", "input", "meta"]
        if self.tag in self_closing_tags:
            if not self.props:
                return f'<{self.tag} />'
            else:
                props_str = ' '.join([f'{key}="{value}"' for key, value in self.props.items()])
                return f'<{self.tag} {props_str}>'
        if not self.props:
            return f'<{self.tag}>{self.value}</{self.tag}>'
        else:
            props_str = ' '.join([f'{key}="{value}"' for key, value in self.props.items()])
            return f'<{self.tag} {props_str}>{self.value}</{self.tag}>'
        

class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        props_str = ''
        if not self.tag:
            raise ValueError('Must have a tag')
        if not self.children:
            raise ValueError('Must have children')
        if self.props:
            props_str = ' ' + ' '.join(f'{key}="{value}"' for key, value in self.props.items())
        
        opening_tag = f"<{self.tag}{props_str}>"
        closing_tag = f"</{self.tag}>"

        children_html = "".join(child.to_html() for child in self.children)

        return f"{opening_tag}{children_html}{closing_tag}"