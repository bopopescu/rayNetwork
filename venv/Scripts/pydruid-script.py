#!C:\Users\raymo\PycharmProjects\raypycharm\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pydruid==0.5.0','console_scripts','pydruid'
__requires__ = 'pydruid==0.5.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('pydruid==0.5.0', 'console_scripts', 'pydruid')()
    )
