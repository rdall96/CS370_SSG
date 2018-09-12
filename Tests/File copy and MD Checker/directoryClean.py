import os


def directoryClean(srcDir):
    for root, dirs, files in os.walk(srcDir):
        for file in files:
            fullFilePath = os.path.join(root , file)
            if os.path.isfile(fullFilePath):
                if fullFilePath.endswith(".html"):
                    os.remove(os.path.join(root , file))
