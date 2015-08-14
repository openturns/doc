#! /usr/bin/env python

from openturns import *
from numpy import *

TESTPREAMBLE()

try :

    # Check tuple / NumericalPoint conversion
    t0 = (0.5 ,1.5)
    p0 = NumericalPoint( t0 )
    print "tuple", t0, "=> NumericalPoint", p0

    t1 = tuple( p0 )
    print "NumericalPoint", p0, "=> tuple", t1

    print "NumericalPoint", p0, "+ tuple", t0, "=> NumericalPoint", p0+t0

    # Check list / NumericalPoint conversion
    l0 = [0.5 ,1.5]
    p0 = NumericalPoint( l0 )
    print "list", l0, "=> NumericalPoint", p0

    l1 = list( p0 )
    print "NumericalPoint", p0, "=> list", l1

    print "NumericalPoint", p0, "+ list", l0, "=> NumericalPoint", p0+l0

    # Check sequence protocol for NumericalPoint
    for x in p0:
        print "value", x
        x0 = p0[0]
        p0[0] = x0
        if x0 not in p0:
            raise ValueError, "NumericalPoint badly implements __contains__()"

    # Check array / NumericalPoint conversion
    a0 = array( (0.5 ,1.5) )
    p0 = NumericalPoint( a0 )
    print "array", a0, "=> NumericalPoint", p0

    a1 = array( p0 )
    print "NumericalPoint", p0, "=> array", a1

    print "NumericalPoint", p0, "+ array", a0, "=> NumericalPoint", p0+a0
    print "array", a0, "+ NumericalPoint", p0, "=> array", a0+p0

    # Check tuple / NumericalSample conversion
    t0 = ((1.,2.), (3.,4.))
    s0 = NumericalSample( t0 )
    print "tuple", t0, "=> NumericalSample", s0

    t0 = ([1.,2.], [3.,4.])
    s0 = NumericalSample( t0 )
    print "tuple", t0, "=> NumericalSample", s0

    t1 = tuple( s0 )
    print "NumericalSample", s0, "=> tuple", t1

    # Check list / NumericalSample conversion
    l0 = [[1.,2.], [3.,4.]]
    s0 = NumericalSample( l0 )
    print "list", l0, "=> NumericalSample", s0

    l0 = [(1.,2.), (3.,4.)]
    s0 = NumericalSample( l0 )
    print "list", l0, "=> NumericalSample", s0

    l1 = list( s0 )
    print "NumericalSample", s0, "=> list", l1

    # Check array / NumericalSample conversion
    a0 = array( ((1.,2.), (3.,4.)) )
    s0 = NumericalSample( a0 )
    print "array", a0, "=> NumericalSample", s0

    a1 = array( s0 )
    print "NumericalSample", s0, "=> array", a1


    # Check tuple / NumericalMathFunction interoperability
    F = NumericalMathFunction( "poutre" )
    t0 = (1.,2.,3.,4.)
    print "NumericalPoint", F( t0 ), "= F( tuple", t0, ")"

    # Check list / NumericalMathFunction interoperability
    l0 = [1.,2.,3.,4.]
    print "NumericalPoint", F( l0 ), "= F( list", l0, ")"

    # Check array / NumericalMathFunction interoperability
    a0 = array( (1.,2.,3.,4.) )
    print "NumericalPoint", F( a0 ), "= F( array", a0, ")"

    # Check Python function / NumericalMathFunction interoperability
    def aFunc( x ):
        return x[0] + x[1] + x[2] + x[3]

    class OTPyFunc( OpenTURNSPythonFunction ):
        def __init__( self ):
            OpenTURNSPythonFunction.__init__( self, 4, 1 )
            def _exec( self, x ):
                return [ aFunc( x ) ]

    PYNMF = NumericalMathFunction( OTPyFunc() )

    print "NumericalPoint", PYNMF( t0 ), "= PYNMF( tuple", t0, ")"
    print "NumericalPoint", PYNMF( l0 ), "= PYNMF( list", l0, ")"
    print "NumericalPoint", PYNMF( a0 ), "= PYNMF( array", a0, ")"



except :
    import sys
    print "t_NumPyTypeConversion_std.py", sys.exc_type, sys.exc_value
