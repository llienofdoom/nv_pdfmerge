import sys
import os
import glob
from PyPDF2 import PdfFileReader, PdfFileWriter

input_folder = sys.argv[1]

if input_folder == None:
    print('Please drag a folder onto the app, like a boss. Not what you just did. Like a lame-o...')
    sys.exit()
else:
    print('Working in %s' % input_folder)

    print('Collecting initial file names to merge...')
    pdf_files_to_merge = []
    try:
        pdf_files_to_merge.append(glob.glob( os.path.join(input_folder, '*Executive*')   )[0])
        pdf_files_to_merge.append(glob.glob( os.path.join(input_folder, '*Balance*')     )[0])
        pdf_files_to_merge.append(glob.glob( os.path.join(input_folder, '*Profit*')      )[0])
        pdf_files_to_merge.append(glob.glob( os.path.join(input_folder, '*Cash*')       )[0])
        pdf_files_to_merge.append(glob.glob( os.path.join(input_folder, '*Receivables*') )[0])
        pdf_files_to_merge.append(glob.glob( os.path.join(input_folder, '*Payables*')    )[0])
    except:
        print('Files needed for merge NOT found in selected folder. Please be better at what you do...')
        sys.exit()
    print('Done! Carying on...')

    print('Merging Files...')
    pdf_writer = PdfFileWriter()
    for pdf_file in pdf_files_to_merge:
        pdf_reader = PdfFileReader(pdf_file)
        for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page))
    print('Done!')

    print('Generating Output. Hang on Tight!')
    output = os.path.join(input_folder, 'Financial Report VentureWeb International Limited MONTH YEAR.pdf')
    with open(output, 'wb') as out:
        pdf_writer.write(out)
    print('Done! Go have a margarita! ')
