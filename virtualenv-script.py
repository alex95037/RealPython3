#!C:\Python33\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'virtualenv==1.9.1','console_scripts','virtualenv'
__requires__ = 'virtualenv==1.9.1'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('virtualenv==1.9.1', 'console_scripts', 'virtualenv')()
    )
