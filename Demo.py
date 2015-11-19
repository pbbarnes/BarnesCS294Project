#!/usr/bin/env python3

import DEMO1

# Prototype for writing discussion group spreadsheets.
# Make a new copy of this file for each discussion board

# Enter values for XXX and NAME below
url = 'http://docushare-test.tmt.org/docushare/dsweb/View/BulletinBoard-11'
htmlfile = 'Demostration Purposes.html'
xlsfile = 'Demonstartion Purposes.xlsx'

# Call get_discussion
# The htmlfile will be stored in the dccfilepath directory and the
# xlsfile will be stored in the current directory

DEMO1.get_discussion(url, htmlfile, xlsfile)
