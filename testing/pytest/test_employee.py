import pytest
import random

from employee import Employee


# pytest doesn't require TestCase to inherit from anything
class EmployeeTestCase():
    # pytest doesn't use JUnit-like setUp/ tearDown mechanism - instead fixtures are utilized

    def test_mock(self):
        assert 1 == 1

# classes aren't even needed - they just group code
@pytest.fixture
def employee():
    return Employee('John', 'Smith', 2137)

def test_first_name(employee):
    assert 'John' == employee.first

def test_last_name(employee):
    assert 'Smith' == employee.last

def test_pay(employee):
    assert 2137 == employee.pay

# test can be parametrized using built-in marker
@pytest.mark.parametrize('given_value, expected_value',
[
    (1, 1),
    (2, 2),
    (19, 19),
    (100, 100),
    (1999, 1999),
    (2022, 2022),
    tuple([random.randint(0, 100)] * 2),
    tuple([random.randint(0, 100)] * 2),
    tuple([random.randint(0, 100)] * 2),
    tuple([random.randint(0, 100)] * 2),
    tuple([random.randint(0, 100)] * 2),
    tuple([random.randint(0, 100)] * 2),
    tuple([random.randint(0, 100)] * 2),
    tuple([random.randint(0, 100)] * 2),
    tuple([random.randint(0, 100)] * 2)
])
def test_very_simple(given_value, expected_value):
    assert given_value == expected_value


# indirect parameters 
# from official pytest docs: https://docs.pytest.org/en/stable/example/parametrize.html#apply-indirect-on-particular-arguments
@pytest.fixture(scope="function")
def x(request):
    return request.param * 3


@pytest.fixture(scope="function")
def y(request):
    return request.param * 2


@pytest.mark.parametrize("x, y", [("a", "b")], indirect=["x"])
def test_indirect(x, y):
    assert x == "aaa"
    assert y == "b"

# how does generating test via metafunc works??