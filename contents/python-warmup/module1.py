from pathlib import Path

PERSON1 = {'name': 'John', 
           'age': 36, 
           'country': 'Norway'}


def greeting(name):
    return 'Hello, ' + name + '!'


class FolderOperations:
    def __init__(self, foldername: str) -> None:
        self.folderpath = Path(foldername)

    def exists(self):
        return self.folderpath.exists()

    def delete(self):
        for filepath in self.folderpath.iterdir():
            if filepath.exists():
                filepath.unlink()
        self.folderpath.rmdir()

    def create(self):
        self.folderpath.mkdir()

    def add_file(self, filename: str = 'Untitled.txt'):
        filepath = self.folderpath.joinpath(filename)
        if not filepath.exists:
            filepath.touch()

        return filepath
