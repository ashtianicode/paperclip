import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

VERSION = '0.1.0'
PACKAGE_NAME = 'paperclip'
AUTHOR = 'Taha'
AUTHOR_EMAIL = 'taha.m.ashtiani@gmail.com'
URL = 'https://github.com/ashtianicode'

LICENSE = 'Apache License 2.0'
DESCRIPTION = 'PaperClip helps you keep your large local datasets on the cloud'
LONG_DESCRIPTION = (HERE / "README.md").read_text()
LONG_DESC_TYPE = "text/markdown"

INSTALL_REQUIRES = [
      'fire',
      'boto3',
      'db-sqlite3',
      'zipfile36'
      
]

setup(name=PACKAGE_NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      long_description_content_type=LONG_DESC_TYPE,
      author=AUTHOR,
      license=LICENSE,
      author_email=AUTHOR_EMAIL,
      url=URL,
      install_requires=INSTALL_REQUIRES,
      packages=find_packages()
      )