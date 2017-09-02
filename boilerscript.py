"""
A boilerplate static HTML website creator

-   Place this script and the folder in 'C:/script' or similar
    and point your PATH to that folder.

-   Otherwise, place this script and the folder into the root of
    your project and comment out the ROOT variable
"""
#!/usr/bin/env python

import os
import shutil

ROOT = 'C:/script/boilerscript/'

SRC = {
    'html': ROOT + 'index.html', 'css': ROOT + 'style.css',
    'js': ROOT + 'script.js'
}

DEST = {
    'html': 'index.html', 'css': 'style/style.css',
    'js': 'script/script.js'
}

os.mkdir('style')
os.mkdir('script')

shutil.copy2(SRC['html'], DEST['html'])
shutil.copy2(SRC['css'], DEST['css'])
shutil.copy2(SRC['js'], DEST['js'])
