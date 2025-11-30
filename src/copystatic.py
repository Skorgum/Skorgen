import os
import os.path
import shutil

def copy_static(source, destination):
    if os.path.exists(destination):
        shutil.rmtree(destination)
    os.mkdir(destination)
    
    for name in os.listdir(source):
        source_path = os.path.join(source, name)
        dest_path = os.path.join(destination, name)

        if os.path.isfile(source_path):
            shutil.copy(source_path, dest_path)
        elif os.path.isdir(source_path):
            os.mkdir(dest_path)
            copy_static(source_path, dest_path)
