import os
import shutil
from copystatic import copy_static
from gencontent import generate_page

def main():
    public_dir = "public"
    
    if os.path.exists(public_dir):
        shutil.rmtree(public_dir)

    copy_static("static", public_dir)
    generate_page("content/index.md", "template.html", f"{public_dir}/index.html")

if __name__ == "__main__":
    main()