import os
import shutil
from copystatic import copy_static
from gencontent import generate_page

def main():
    public_dir = "public"
    
    if os.path.exists(public_dir):
        shutil.rmtree(public_dir)

    copy_static("static", public_dir)
    # generate_page("content/index.md", "template.html", f"{public_dir}/index.html")
    for root, dirs, files in os.walk("content"):
        for filename in files:
            if not filename.endswith(".md"):
                continue
            from_path = os.path.join(root, filename)

            relative_path = from_path[len("content/"):]

            dest_path = os.path.join(public_dir, relative_path)
            dest_path = dest_path.replace(".md", ".html")

            generate_page(from_path, "template.html", dest_path)

if __name__ == "__main__":
    main()