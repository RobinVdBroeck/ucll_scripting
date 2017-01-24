import testing
import testing.tests


def fail():
    """
    When called within a test, aborts the test immediately.
    The test is considered to have failed.
    """
    printer = testing.environment.settings.printer
    
    printer.log(1, "FAIL: {} (in {})", testing.environment.tests.testName, testing.environment.tests.path)
    printer.log(2, "Additional information:")
    for item in testing.environment.tests.context:
        printer.log(2, "  " + item)

    printer.log(2, "")

    raise testing.tests.TestFailure()

def mustBeEqual(expected, actual, epsilon = None):
    """
    Assert that the given values must be equal to each other.
    If they are not, failure ensues.
    """
    if epsilon:
        with testing.tests.context("Expected value: {}", expected), \
             testing.tests.context("Actual value: {}", actual), \
             testing.tests.context("Epsilon: {}", epsilon):
            if abs(expected - actual) > epsilon:
                fail()
    else:
        with testing.tests.context("Expected value: {}", expected), \
             testing.tests.context("Actual value: {}", actual):
            if expected != actual:
                fail()

def mustBeSameTruthiness(expected, actual):
    """
    Assert that both values represent the same truthiness.
    If they do not, failure ensues.
    """
    if expected:
        with testing.tests.context("Expected truthy value; got {}", actual):
            if not actual:
                fail()
    else:
        with testing.tests.context("Expected falsey value; got {}", actual):
            if actual:
                fail()
            
def mustBeTruthy(actual):
    """
    Assert that the given value must be truthy.
    If it is not, failure ensues.
    """
    with testing.tests.context("Value that should be true: {}", actual):
        if not actual:
            fail()

def mustBeFalsey(actual):
    """
    Assert that the given value must be falsey.
    If it is not, failure ensues.
    """
    with testing.tests.context("Value that should be false: {}", actual):
        if actual:
            fail()

def mustRaise(exceptionType, code):
    """
    Assert that the execution of the given code
    leads to an exception of the given type.
    """    
    try:
        code()
        with testing.tests.context("No exception thrown; expected exception {}", exceptionType):
            fail()
    except Exception as e:
        if type(e) != exceptionType:
            with testing.tests.context("Wrong exception thrown, expected {}, got {}", exceptionType.__name__, type(e).__name__):
                fail()
            
def ignore(*args, **kwargs):
    """
    Does nothing.
    """
    pass
