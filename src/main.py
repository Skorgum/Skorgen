from textnode import TextNode, TextType
from copystatic import copy_static

def main():
    source = "static"
    destination = "public"
    copy_static(source, destination)

if __name__ == "__main__":
    main()