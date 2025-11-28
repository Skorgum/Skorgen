from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import ParentNode
from markdown_blocks import BlockType, markdown_to_blocks, block_to_block_type
from inline_markdown import text_to_textnodes

def markdown_to_html_node(markdown):
    # split into blocks
    blocks = markdown_to_blocks(markdown)
    children = []

    for block in blocks:
        btype = block_to_block_type(block)

        if btype == BlockType.PARAGRAPH:
            lines = block.split("\n")
            clean_lines = [line.strip() for line in lines if line.strip() != ""]
            paragraph_text = " ".join(clean_lines)
            text_nodes = text_to_textnodes(paragraph_text)
            html_children = [text_node_to_html_node(tn) for tn in text_nodes]
            node = ParentNode("p", html_children)

        elif btype == BlockType.CODE:
            lines = block.split("\n")
            lines = lines[1:-1]
            code_text = "\n".join(lines) + "\n"
            text_node = TextNode(code_text, TextType.TEXT)
            code_child = text_node_to_html_node(text_node)
            code_node = ParentNode("code", [code_child])
            node = ParentNode("pre", [code_node])

        elif btype == BlockType.HEADING:
            line = block.strip()
            level = 0
            for ch in line:
                if ch == "#":
                    level += 1
                else:
                    break
            heading_text = line[level:].strip()
            text_nodes = text_to_textnodes(heading_text)
            html_children = [text_node_to_html_node(tn) for tn in text_nodes]
            tag = f"h{level}"
            node = ParentNode(tag, html_children)

        elif btype == BlockType.QUOTE:
            lines = block.split("\n")
            clean_lines = [line.strip("> ") for line in lines if line.strip("> ") != ""]
            quote_text = " ".join(clean_lines)
            text_nodes = text_to_textnodes(quote_text)
            html_children = [text_node_to_html_node(tn) for tn in text_nodes]
            node = ParentNode("blockquote", html_children)

        elif btype == BlockType.UNORDERED_LIST:
            lines = block.split("\n")
            li_nodes = []
            for line in lines:
                stripped = line.strip()
                if stripped == "":
                    continue
                if stripped.startswith("- "):
                    item_text = stripped[2:]
                elif stripped.startswith("-"):
                    item_text = stripped[1:].lstrip()
                else:
                    item_text = stripped
                text_nodes = text_to_textnodes(item_text)
                html_children = [text_node_to_html_node(tn) for tn in text_nodes]
                li_node = ParentNode("li", html_children)
                li_nodes.append(li_node)
            node = ParentNode("ul", li_nodes)

        elif btype == BlockType.ORDERED_LIST:
            lines = block.split("\n")
            li_nodes = []
            for line in lines:
                stripped = line.strip()
                if stripped == "":
                    continue
                dot_index = stripped.find(". ")
                if dot_index != -1 and stripped[:dot_index].isdigit():
                    item_text = stripped[dot_index + 2 :]
                else:
                    item_text = stripped
                text_nodes = text_to_textnodes(item_text)
                html_children = [text_node_to_html_node(tn) for tn in text_nodes]
                li_node = ParentNode("li", html_children)
                li_nodes.append(li_node)
            node = ParentNode("ol", li_nodes)
                
        children.append(node)


    return ParentNode("div", children)
node = markdown_to_html_node    
