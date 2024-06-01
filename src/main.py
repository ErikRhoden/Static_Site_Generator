from textnode import TextNode
from htmlnode import HTMLNode

def main():
    node = TextNode("This is a text node", "bold", "https://www.boot.dev")
    print(node)
    node2 = HTMLNode("p", "This is text inside a paragraph", None, {"href": "https://www.google.com", "target": "_blank"})
    print(node2.props_to_html())
    print(node2)

if __name__ == "__main__":
    main()
