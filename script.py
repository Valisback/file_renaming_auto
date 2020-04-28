import os

folder_name = input('Folder Name: ')

folder_name = folder_name + '/'

with os.scandir(folder_name) as entries:
    for entry in entries:
        if( 'IMG-' in entry.name):
            size = len(folder_name) + len('IMG-')
            new_entry = entry.path[size:]
            new_entry = folder_name + new_entry
            os.rename(entry.path, new_entry)

