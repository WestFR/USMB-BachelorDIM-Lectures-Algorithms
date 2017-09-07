#Searching path and folder files)

import os
import time

THISSCRIPT = os.path.abspath(__file__)
PATHFILE = os.path.dirname(THISSCRIPT)

print("The folder = " + PATHFILE)
print("The file = " + THISSCRIPT)

time.sleep(60)
