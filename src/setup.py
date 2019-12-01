# -*- coding: utf-8 -*-
import sys
from cx_Freeze import setup, Executable


application = 'PyTetris'
includes = []
include_files = ['image','sound','gameobject','font']
packages = ['numpy', 'sys', 'copy', 'pygame', 'math', 'random']
excludes = []

build_exe_options = {
    'includes': includes,
    'include_files': include_files,
    'packages': packages,
    'excludes': excludes
}

exe = [
    Executable(script='tetris.py', base=None, targetName=application)
]


setup(name=application,
      version='1.0.0',
      description='Simple Tetris-like game written in Python.',
      options={'build_exe': build_exe_options},
      executables=exe)
