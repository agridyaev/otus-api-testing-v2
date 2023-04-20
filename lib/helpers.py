import os.path

def get_path(files_dir: str, filename: str):
    return os.path.join(files_dir, filename)
