import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": ["os", "PyQt5", "pandas", "sklearn", "pickle", "scipy", "sklearn", "pandas", "numpy"], 
    "include_files": ["./src/svc.pkl", "./src/heart.csv"]
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"


setup(
    name='Hearth Attack Prediction',
    version = '1.0',
    description = 'Heart Attack Prediction Using SVC and PyQt',
    options={"build_exe": build_exe_options},
    executables=[Executable('./src/ui.py', base=base, targetName = 'heart_attack_prediction')],
)
