import os

def mkdirp(*dictionaries):
    """Recursively create all directories as necessary"""
    path = [i for i in dictionaries]
    os.makedirs(path)

mkdirp("/Users/nicholas/codewars/")