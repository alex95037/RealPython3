#!C:\Python33\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pip==1.5','console_scripts','pip'
__requires__ = 'pip==1.5'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('pip==1.5', 'console_scripts', 'pip')()
    )
