#!/usr/bin/env python

# BEGIN_TEX
from __future__ import print_function
import openturns as ot

external_program = 'python external_program.py'

def _exec( X ):
    # create input file
    in_file = 'input.py'
    ot.coupling_tools.replace('input_template.py', in_file, ['@E', '@F'], X)

    # compute
    ot.coupling_tools.execute(external_program + ' ' + in_file)

    # parse output file
    Y = ot.coupling_tools.get('output.py', tokens=['Z='])

    return Y

model = ot.PythonFunction(2, 1, _exec)
out_sample = model( ot.NumericalSample([[2, 3], [5, 8]]) )
print(out_sample)
#...
# END_TEX
