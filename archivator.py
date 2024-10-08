import shutil
def archivator(name_arch: str, format_arch: str, root_dir_arch: str):
    shutil.make_archive(base_name=name_arch,format=format_arch, root_dir=root_dir_arch)


if __name__ == "__main__":
    archivator(None)