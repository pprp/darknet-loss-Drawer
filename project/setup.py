from cx_Freeze import setup, Executable
import sys
base = 'WIN32GUI' if sys.platform == "win32" else None


executables = [Executable("main_window.py", base=base, icon='draw.png')]

packages = []
include_files = ['draw.png','Ui_main.py','extract_log.py','visualization_loss.py']
options = {
    'build_exe': {
        'packages': packages,
        'include_files': include_files
    },

}

setup(
    name="prog",
    options=options,
    version="1.0",
    description='desc of program',
    executables=executables
)
