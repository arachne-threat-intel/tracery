import os


# Answer from https://stackoverflow.com/a/41658338
def execfile(filepath, globals=None, locals=None):
    if globals is None:
        globals = {}
    globals.update({
        "__file__": filepath,
        "__name__": "__main__",
    })
    with open(filepath, 'rb') as file:
        exec(compile(file.read(), filepath, 'exec'), globals, locals)


class ExternalCaller:
    @staticmethod
    def call_webapp():
        execfile(os.path.join('searx', 'searx', 'webapp.py'))
