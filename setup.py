# setup.py
from setuptools import setup

APP = ['main.py']
OPTIONS = {
    "argv_emulation": True,
    "packages": ["customtkinter"],
    'alias': False,
    'strip': False,                # same as --no-strip
    'codesign_identity': None,     # same as --codesign-identity ""
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
