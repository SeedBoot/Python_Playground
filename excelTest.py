import openpyxl
import os

#Change the directory as required
dir = 'C:\\Scratch\\dev\\py\\test'
os.chdir(dir)

# filename of the file in the directory
workBook = openpyxl.load_workbook('AW17 weekly Trading Plan EU.xlsx')

print('Sheets in selected workbook:')
print('----------------------------')

# gets sheet names in file
wb = workBook.get_sheet_names()
for sheets in wb:
    print('+ ', sheets)

print('')
print('Targeting this particular sheet:')
print('--------------------------------')

# identify a particular sheet
hp = workBook.get_sheet_by_name('HP')
print(hp)

print('')

# generates report within given row numbers
def printCells(num1, num2):
    for i in range(num1, num2):
            print(hp['B' + str(i)].value)
            print('----------')
            print(hp['Y' + str(i)].value)
            print('')

printCells(6, 11)
