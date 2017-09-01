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

import shutil
import os

SOURCE = 'C:/oscript/Boilerplate.html'
DESTINATION = 'index.html'

shutil.copy2(SOURCE, DESTINATION)

os.mkdir('style')
os.mkdir('script')

os.system('touch style/style.css') #hmmmm?
