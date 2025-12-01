import os
import shutil
import sys
from copystatic import copy_static
from gencontent import generate_pages_recursive

def main():
    public_dir = "docs"
    
    if os.path.exists(public_dir):
        shutil.rmtree(public_dir)

    copy_static("static", public_dir)

    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"


    generate_pages_recursive("content", "template.html", public_dir, basepath)
    

if __name__ == "__main__":
    main()