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
    def __init__(self, value, tag=None , props=None):
        super().__init__(value, tag, props)

    def to_html(self):
        if self.value is None:
            raise ValueError('Must provide a value')
        if self.tag is None:
            return self.value
        if not self.props:
            return f'<{self.tag}>{self.value}</{self.tag}>'
        else:
            props_str = ' '.join([f'{key}="{value}"' for key, value in self.props.items()])
            return f'<{self.tag} {props_str}>{self.value}</{self.tag}>'