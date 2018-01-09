import os

dir = 'C:/Scratch/dev/py'

print(os.listdir(dir))

directoryList = os.listdir(dir)

for i in directoryList:
    stringSplit = i[:-4].split('.')
    addSpace = ' '.join(stringSplit)
    returnExtension = addSpace + i[-4:]
    print(stringSplit)
    print(addSpace)
    print(returnExtension)
