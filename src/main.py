import os
import shutil
from copystatic import copy_static
from gencontent import generate_pages_recursive

def main():
    public_dir = "public"
    
    if os.path.exists(public_dir):
        shutil.rmtree(public_dir)

    copy_static("static", public_dir)

    generate_pages_recursive("content", "template.html", public_dir)
    

if __name__ == "__main__":
    main()