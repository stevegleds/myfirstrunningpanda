import datetime
import os

# old_file is used to test if we are using an out of date file. This means we have forgotten to copy the new gmail export file mbox.
# Specify just the filenames. Process_sourcefile() will deal with paths and also check if the files are up to date.
# Usage: process_sourcefile

def process_sourcefile(input_filename, old_file=False):
    """
    :rtype:bool
    """
    input_file = os.path.join('', input_filename)
    input_modified_date = datetime.date.fromtimestamp(os.path.getmtime(input_file))
    print('today is:', datetime.date.today(), 'file is: ', input_modified_date )
    if datetime.date.today() != input_modified_date :
        old_file = True
    print("filename is: ", input_file, "modified on :", datetime.date.fromtimestamp(os.path.getmtime(input_file)))
    if old_file:
        print('Your file is old, are you sure you want to continue? It was last saved on :', input_modified_date)
        response = input('Enter Y to continue. Any other input will quit.')
        if response.lower() != 'y':
            raise SystemExit
    return True

