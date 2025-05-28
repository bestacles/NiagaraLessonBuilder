# setup.py
from setuptools import setup

APP = ['main.py']
OPTIONS = {
    "argv_emulation": True,
    "packages": ["customtkinter"],
    "plist": {
        "CFBundleName": "Niagara Lesson Builder",
        "CFBundleShortVersionString": "1.0",
        "CFBundleIdentifier": "com.bestacles.niagaralb"
    },
    # (no codesign_identity / strip here)
}

setup(
    app=APP,
    options={"py2app": OPTIONS},
    setup_requires=["py2app"],
)
