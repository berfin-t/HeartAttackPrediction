from cx_Freeze import setup, Executable
import PyQt5
import pandas
import sklearn
import pickle

buildOptions = dict(packages = ["PyQt5", "pandas", "sklearn", "pickle"], excludes = [], includes=["prediction_file"], include_files=["svc.pkl"])

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('test.py', base=base, targetName = 'heart_attack_prediction')
]

setup(name='Hearth Attack Prediction',
      version = '1.0',
      description = 'Heart Attack Prediction Using SVC and PyQt',
      options = dict(build_exe = buildOptions),
      executables = executables)