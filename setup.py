from setuptools import setup

APP = ['main.py']
DATA_FILES = []
OPTIONS = {
    "argv_emulation": True,
    "packages": ["customtkinter"],
    # "iconfile": "assets/app.icns",  # optional: path to your .icns file
    "plist": {
        "CFBundleName": "Niagara Lesson Builder",
        "CFBundleShortVersionString": "1.0",
        "CFBundleIdentifier": "com.bestacles.niagaralb"
    },
    # disable auto code-signing & stripping in CI
    "codesign_identity": None,
    "strip": False,
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={"py2app": OPTIONS},
    setup_requires=["py2app"],
)
