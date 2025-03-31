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


class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, props)
        self.props=props
 

    def to_html(self):
        if self.value==None or self.value=="":
            raise ValueError("LeafNode must have value")
        
        if self.tag==None or self.tag=="":
            return self.value
        

        if self.props==None or self.props=={}:
            return f"<{self.tag}>{self.value}</{self.tag}>"

        text=""
        for key in self.props:
            text+=f' {key}="{self.props[key]}"'
        return f'<{self.tag}{text}>{self.value}</{self.tag}>'



    def __eq__(self, other):
        return self.tag==other.tag and self.value==other.value and self.props==other.props

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"


