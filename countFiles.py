#!/usr/bin/env python3

import os
from datetime import datetime


# returns all files that contains currentDate
def countFiles(dir: str) -> int:
    currentDate = datetime.today().strftime('%Y%m%d')
    count = 0
    list_dir = list(os.scandir(dir))
    for file in list_dir:
        if file.is_file() and file.name.__contains__(currentDate):
            count += 1
    return count


args = {
    'path': '/home/cezarcozta',
}

directory = args['path']

try:
    files = countFiles(directory)
    currentDate = datetime.today().strftime('%Y%m%d')

    if(files == 79):
        print('valido')
    else:
        print('invalido')

    print(f'existem {files} arquivos que contem a data { {currentDate} }')
except Exception as e:
    print(e)
