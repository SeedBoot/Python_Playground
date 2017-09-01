"""
A boilerplate HTML website creator

#- Place !folder? in the root of your project# forget this for now

- In the variable SOURCE,
  change the directory to point to the source
- In the variable DESTINATION,
  change 'project' to suit your needs
-
"""
#!/usr/bin/env python

import os
import shutil

#HTML variables
SOURCE_H = 'Boilerplate.html'
DESTINATION_H = '../index.html'
#CSS variables
SOURCE_C = 'style.css'
DESTINATION_C = '../style/style.css'
#JS variables
SOURCE_J = 'script.js'
DESTINATION_J = '../script/script.js'

os.mkdir('../style')
os.mkdir('../script')

shutil.copy2(SOURCE_H, DESTINATION_H)
shutil.copy2(SOURCE_C, DESTINATION_C)
shutil.copy2(SOURCE_J, DESTINATION_J)
