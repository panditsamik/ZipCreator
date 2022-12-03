import pathlib
import zipfile


def make_archive(files, folder):
    dest_path = pathlib.Path(folder, "compressed.zip")
    with zipfile.ZipFile(dest_path, "w") as archive:
        for file in files:
            file = pathlib.Path(file)
            archive.write(file, arcname=file.name)
