from setuptools import setup

setup(
    app=['RobloxPatcher.py'],
    options={
        "py2app": {
             "includes": ["os", "platform"],
			 "packages": ["chardet"]
        }
    },
)