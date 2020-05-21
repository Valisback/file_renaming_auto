import os

folder_name = input('Folder Name: ')
pattern = input('Enter pattern to remove: ')


folder_name = folder_name + '/'

with os.scandir(folder_name) as entries:
    for entry in entries:
        if( pattern in entry.name):
            size = len(folder_name) + len(pattern)
            new_entry = entry.path[size:]
            new_entry = folder_name + new_entry
            os.rename(entry.path, new_entry)

