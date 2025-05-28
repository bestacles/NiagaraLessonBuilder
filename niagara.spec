# niagara.spec
from PyInstaller.utils.hooks import collect_submodules
hiddenimports = collect_submodules('customtkinter')

block_cipher = None
a = Analysis(
    ['main.py'],
    hiddenimports=hiddenimports,
    pathex=[],
)
pyz = PYZ(a.pure)
exe = EXE(
    pyz,
    a.scripts,
    name='Niagara Lesson Builder',
    windowed=True,           # no console
)
app = BUNDLE(exe, name='Niagara Lesson Builder.app')
