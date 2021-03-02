from . import module1


if __name__ == '__main__':
    """
    Entry point of a python program.
    """
    folder = module1.FolderOperations('data')

    if not folder.exists():
        folder.create()

    filepath = folder.add_file('some_file.txt')

    with open(filepath, 'w') as stream:
        person1 = module1.PERSON1
        stream.write(module1.greeting(person1['name']) + '\n')

    folder.delete()
