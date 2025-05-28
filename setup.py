from setuptools import setup

APP = ['main.py']
DATA_FILES = []
OPTIONS = {
    "argv_emulation": True,
    "packages": ["customtkinter"],
    # If you have an .icns for an icon, uncomment and point here:
    # "iconfile": "assets/app.icns",
    "plist": {
        "CFBundleName": "Niagara Lesson Builder",
        "CFBundleShortVersionString": "1.0",
        "CFBundleIdentifier": "com.bestacles.niagaralb"
    },
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={"py2app": OPTIONS},
    setup_requires=["py2app"],
)
