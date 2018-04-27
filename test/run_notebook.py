# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 13:57:34 2018
Testing wrapper for ipython notebooks
https://blog.thedataincubator.com/2016/06/testing-jupyter-notebooks/
@author: Tom
"""
import os
import subprocess
import tempfile

import nbformat

def _notebook_run(path):
    """Execute a notebook via nbconvert and collect output.
       :returns (parsed nb object, execution errors)
    """
    dirname, __ = os.path.split(path)
#    if len(dirname) == 0:
#        path = os.path.join(os.getcwd(), path)
    with tempfile.NamedTemporaryFile(suffix=".ipynb") as fout:
        args = ["jupyter", "nbconvert", "--to", "notebook", "--execute",
          "--ExecutePreprocessor.timeout=60",
          "--output", "temp.ipynb", path]
        proc = subprocess.run(args)
        rc = proc.returncode
        fout.seek(0)
        nb = nbformat.read("temp.ipynb", nbformat.current_nbformat)

    errors = [output for cell in nb.cells if "outputs" in cell
                     for output in cell["outputs"]\
                     if output.output_type == "error"]

    return nb, errors, rc


def test_ipynb():
    rootdir = os.path.split(os.getcwd())[0]
    for path, subdirs, files in os.walk(rootdir):
        for name in files:
            if (name.endswith('.ipynb') and 'checkpoint' not in name
                and 'temp' not in name):
                nbook = os.path.join(path,name)
                nb, errors, rc = _notebook_run(nbook)
                print(nbook)
                assert errors == []
                assert rc == 0
    
if __name__ == '__main__':
    test_ipynb()