"""A class to start searx's webapp externally.
The Python method exec() is advised against due to how it can execute any Python script hence
any malicious code. It has been used here because calling run() of webapp excludes many lines of code
across the script that need to be executed. Instead of moving these lines around, it was decided to use exec()
as webapp is a trusted file (as it is part of searx) and it is the equivalent of launching the webapp via
running `python webapp.py`."""

import os


# Method to execute a python script
# Taken from answer https://stackoverflow.com/a/41658338
def _execfile(filepath, specified_globals=None, specified_locals=None):
    if specified_globals is None:
        specified_globals = {}
    specified_globals.update({
        "__file__": filepath,
        "__name__": "__main__",
    })
    with open(filepath, 'rb') as file:
        exec(compile(file.read(), filepath, 'exec'), specified_globals, specified_locals)


# Class to import in non-searx modules to run certain scripts
class ExternalCaller:
    # Method to run the webapp.py script
    @staticmethod
    def call_webapp():
        _execfile(os.path.join('searx', 'searx', 'webapp.py'))
