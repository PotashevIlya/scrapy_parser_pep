def build_dir(base_dir, subdir):
    dir = base_dir / subdir
    dir.mkdir(exist_ok=True)
    return dir
