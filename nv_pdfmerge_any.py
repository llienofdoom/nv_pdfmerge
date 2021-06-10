import sys
import os
import glob
from PyPDF2 import PdfFileReader, PdfFileWriter

print('Merge PDF files in any order. Starting:\n')
print('Drag first PDF to this window, then press ENTER:')

pdf_files_to_merge = []
input_file = input()
path = os.path.dirname(input_file)
while input_file != '':
    pdf_files_to_merge.append(input_file.rstrip())
    print('\nDrag next PDF to this window, then press ENTER, until finished, then just ENTER:')
    input_file = input()

print('Done! Carying on...')

print('Merging Files...')
pdf_writer = PdfFileWriter()
for pdf_file in pdf_files_to_merge:
    pdf_reader = PdfFileReader(pdf_file)
    for page in range(pdf_reader.getNumPages()):
        pdf_writer.addPage(pdf_reader.getPage(page))
print('Done!')

print('Generating Output. Hang on Tight!')
output = os.path.join(path, 'Group Transfer Pricing Overhead - YEAR MONTH.pdf')
with open(output, 'wb') as out:
    pdf_writer.write(out)
print('Done! Go have some sangrea! ')
