# chardet's setup.py
from distutils.core import setup
setup(
    name = "traveller_utils",
    packages = ["traveller_utils"],
    version = "0.0.1",
    description = "Utilities to help in running Traveller games",
    author = "Arthur Green",
    author_email = "arthur.green045@gmail.com",
    keywords = ["encoding", "i18n", "xml"],
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Linguistic",
        ],
    long_description = """\
A collection of Python libraries and command-line tools that use them. They can be used
to generate some useful data for use with the Traveller RPG.

* LBB2
    * cargo.py/Cargo() - LBB2 cargo generator
    * cargo/py/CargoSale() - LBB2 cargo sale details generator
* utils
    * util.py/Die() - generic die-roller
    * util.pyTable() - table of results (e.g. cargo generator) that can return a random row on demand
"""
)