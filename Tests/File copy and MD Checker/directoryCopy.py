
def dirCopy():

    import os

    inputpath = 'Markdown/'
    outputpath = 'HTML'

    for dirpath, dirnames, filenames in os.walk(inputpath):
        structure = os.path.join(outputpath, dirpath[len(inputpath):])
        if not os.path.isdir(structure):
            os.mkdir(structure)
        else:
            print("Folder already exists")
            break

dirCopy()
