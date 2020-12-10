import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

options = {
    'build_exe': {
        'includes': 'atexit',
        "zip_include_packages": ["PyQt5"]
    }
}

executables = [
    Executable('main.py', base=base)
]

setup(name='ClearDesktop',
      version='0.1',
      description='Clear Desktop',
      options=options,
      executables=executables
      )
