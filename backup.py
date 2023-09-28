import zipfile, os

def backupToZip(folder, destination_folder):
    folder = os.path.abspath(folder)
    destination_folder = os.path.abspath(destination_folder)

    number = 1
    while True:
        zipFilename = os.path.join(destination_folder, os.path.basename(folder) + '_' + str(number) + '.zip')
        if not os.path.exists(zipFilename):
            break
        number += 1

    print('Creating %s...' % (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' % (foldername))
        
        # Add the current folder to the ZIP file.
        backupZip.write(foldername)
        
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue   # don't backup the backup ZIP files
            backupZip.write(os.path.join(foldername, filename))

    backupZip.close()
    print('Done.')

# Example usage:
backupToZip('/path/to/your/source_folder', '/path/to/your/destination_folder')
