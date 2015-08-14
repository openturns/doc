#!/usr/bin/env python

# BEGIN_TEX
import coupling_tools as ct

def _exec( X ):
    in_file = 'input.py'
    ct.replace('input_template.py', in_file, ['@E', '@F'], X)
    ct.execute('python external_program.py ' + in_file)
    return ct.get('output.py', tokens=['Z='])

# END_TEX
