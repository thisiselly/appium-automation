def assert_equal(expected, actual, message=""):
    assert expected == actual, f"Assertion Failed: {message}, Expected: {expected}, Actual: {actual}"

def assert_not_equal(expected, actual, message=""):
    assert expected != actual, f"Assertion Failed: {message}, Expected: {expected}, Actual: {actual}"

def assert_true(condition, message=""):
    assert condition, f"Assertion Failed: {message}, Expected: True, Actual: {condition}"

def assert_false(condition, message=""):
    assert not condition, f"Assertion Failed: {message}, Expected: False, Actual: {condition}"

def assert_in(element, container, message=""):
    assert element in container, f"Assertion Failed: {message}, Expected: {element} in {container}"

def assert_not_in(element, container, message=""):
    assert element not in container, f"Assertion Failed: {message}, Expected: {element} not in {container}"

def assert_greater(expected, actual, message=""):
    assert expected > actual, f"Assertion Failed: {message}, Expected: {expected} > {actual}"

def assert_greater_equal(expected, actual, message=""):
    assert expected >= actual, f"Assertion Failed: {message}, Expected: {expected} >= {actual}"

def assert_less(expected, actual, message=""):
    assert expected < actual, f"Assertion Failed: {message}, Expected: {expected} < {actual}"

def assert_less_equal(expected, actual, message=""):
    assert expected <= actual, f"Assertion Failed: {message}, Expected: {expected} <= {actual}"
