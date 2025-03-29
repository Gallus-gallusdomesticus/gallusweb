class HTMLNode:
    def __init__(self,tag=None, value=None, children=None, props=None):
        self.tag      = tag
        self.value    = value
        self.children = children if children is not None else []
        self.props    = props if props is not None else {}

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        text=""
        for key in self.props:
            text+=f' {key}="{self.props[key]}"'
        return text
    
    def __eq__(self, other):
        return self.tag==other.tag and self.value==other.value and self.children==other.children and self.props==other.props

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"