from textnode import TextNode, TextType
from extract_images_and_links import extract_markdown_images, extract_markdown_links

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        parts = node.text.split(delimiter)

        if len(parts) % 2 == 0:
            raise Exception("invalid markdown, missing closing delimiter")
    
        for i, part in enumerate(parts):
            if part == "":
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(part, TextType.TEXT))
            else:
                new_nodes.append(TextNode(part, text_type))

    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        images = extract_markdown_images(node.text)

        if not images:
            new_nodes.append(node)
            continue

        current_text_to_process = node.text
        
        for image in images:
            alt_txt = image[0]
            url = image[1]
            markdown_str = f"![{alt_txt}]({url})"
            parts = current_text_to_process.split(markdown_str, 1)

            if parts[0] != "":
                new_nodes.append(TextNode(parts[0], TextType.TEXT))

            img = TextNode(alt_txt, TextType.IMAGE, url)
            new_nodes.append(img)

            current_text_to_process = parts[1]
        if current_text_to_process != "":
            new_nodes.append(TextNode(current_text_to_process, TextType.TEXT))

    return new_nodes
                
def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        links = extract_markdown_links(node.text)

        if not links:
            new_nodes.append(node)
            continue

        current_text_to_process = node.text
        
        for link in links:
            link_txt = link[0]
            url = link[1]
            markdown_str = f"[{link_txt}]({url})"
            parts = current_text_to_process.split(markdown_str, 1)

            if parts[0] != "":
                new_nodes.append(TextNode(parts[0], TextType.TEXT))

            next_link = TextNode(link_txt, TextType.LINK, url)
            new_nodes.append(next_link)

            current_text_to_process = parts[1]
        if current_text_to_process != "":
            new_nodes.append(TextNode(current_text_to_process, TextType.TEXT))

    return new_nodes

def text_to_textnodes(text):
    new_nodes = []
    new_nodes.append(TextNode(text, TextType.TEXT))
    new_nodes = split_nodes_delimiter(new_nodes, "`", TextType.CODE)
    new_nodes = split_nodes_image(new_nodes)
    new_nodes = split_nodes_link(new_nodes)
    new_nodes = split_nodes_delimiter(new_nodes, "**", TextType.BOLD)
    new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
    new_nodes = split_nodes_delimiter(new_nodes, "*", TextType.ITALIC)

    return new_nodes