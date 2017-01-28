from testing import *
from testing.tests import *
from testing.assertions import *


with path('Person'), cumulative():
    Person = testedModule().Person

    with path('constructor'):
        @test("initializes fields")
        def _():
            p = Person(80, 1.8)

            mustBeEqual(80, p.weight)
            mustBeEqual(1.8, p.height)

    with path('weight'):
        @test("setting weight")
        def _():
            p = Person(45, 1.52)
            p.weight = 50

            mustBeEqual(50, p.weight)

        @test("invalid weight should raise RuntimeError")
        def _():
            p = Person(80, 1.8)

            def code():
                p.weight = -5

            mustRaise(RuntimeError, code)
            
    with path('height'):
        @test("setting height")
        def _():
            p = Person(45, 1.52)
            p.height = 1.50

            mustBeEqual(1.50, p.height)
            
        @test("invalid height should raise RuntimeError")
        def _():
            p = Person(80, 1.8)

            def code():
                p.height = -1

            mustRaise(RuntimeError, code)

    with path('bmi'):
        @test("yields correct result")
        def _():
            p = Person(80, 1.8)

            mustBeEqual(80 / 1.8**2, p.bmi, epsilon = 0.0001)
