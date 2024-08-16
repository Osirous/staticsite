class HTMLNode:
    def __init__(self,tag=None,value=None,children=None,props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if not self.props: 
            return ""

        prop_string = ""
        for key, value in self.props.items():
            prop_string += f' {key}="{value}"'
        return prop_string

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
    # If you have problems later on, this was added during Ch 2: Nodes 6. TextNode to HTMLNode
    # because we kept returning an error saying that they were not equal in the test_textnode.py
    # There is a commented out test that does work without this def __eq__ being here.
    # Note: 5/23/2024 - After reviewing the solution textnode.py and adjusting our textnode.py
    # accordingly. this is unnecessary, but I am leaving it for future reference.
    #
    #def __eq__(self, other):
    #    if isinstance(other, HTMLNode):
    #        return (self.tag == other.tag and
    #                self.value == other.value and
    #                self.children == other.children and
    #                self.props == other.props)
    #    return False

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None):
        super().__init__(tag=tag, value=value)

        if self.value is None:
            raise ValueError("LeafNode requires a value.")
        
    def to_html(self):
        if self.tag is None:
            return f"{self.value}"
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Invalid HTML: no tag")
        if self.children is None:
            raise ValueError("Invalid HTML: no children")
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
