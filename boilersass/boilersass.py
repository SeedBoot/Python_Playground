"""
Let's see if we can run cmd
"""
#!/usr/bin/env python

import os
import shutil

STYLE_FOLDER = ['import', 'export']
SCSS_FILE = ['asset/style.scss', 'asset/_var.scss']

os.mkdir('style')

for folder in STYLE_FOLDER:
    os.mkdir(os.path.join('style', folder))

os.system('start cmd /c sass --watch style/import:style/export')

shutil.copy2(SCSS_FILE[0], 'style/import/')
shutil.copy2(SCSS_FILE[1], 'style/import/')
