from textnode import *
from htmlnode import *


def main():
    node0 = ParentNode(
        "p",
        [
            LeafNode("b", "0000BOLDTEXT"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "0000italic text"),
            LeafNode(None, "Normal text"),
        ],
    )
    node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
            node0
        ],
    )

    print(node.to_html())

if __name__ == '__main__':
    main()