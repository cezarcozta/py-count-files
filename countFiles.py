#!/usr/bin/env python3

import os
from os.path import isfile


# returns all files that starts with 'piece' parameter
def countFiles(dir: str, piece: str) -> int:
    count = 0
    list_dir = list(os.scandir(dir))
    for file in list_dir:
        if file.is_file() and file.name.__contains__(piece):
            count += 1
    return count


args = {
    'path': '/path/to/folder',
    'piece': 'somefilepiecename'
}

directory = args['path']
piece = args['piece']

try:
    files = countFiles(directory, piece)
    print(f'has {files} files that starts with { {piece} }')
except Exception as e:
    print(e)

# OUTPUT: Valid folder:
#           has 0 files that starts with { piece }
# OUTPUT: Invalid folder:
#           [Errno 2] No such file or directory: '/invalid_folder/'
