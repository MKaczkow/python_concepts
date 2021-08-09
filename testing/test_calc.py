import pytest
import calc


@pytest.mark.basic
def test_add():
    assert calc.add(5, 5) == 10
    assert calc.add(-1, 1) == 0
    assert calc.add(-3, -3) == -6


@pytest.mark.basic
def test_subtract():
    assert calc.subtract(5, 5) == 0
    assert calc.subtract(-1, 1) == -2
    assert calc.subtract(-3, -3) == 0


@pytest.mark.basic
def test_multiply():
    assert calc.multiply(5, 5) == 25
    assert calc.multiply(-1, 1) == -1
    assert calc.multiply(-3, -3) == 9


@pytest.mark.basic
def test_divide():
    assert calc.divide(5, 5) == 1
    assert calc.divide(-1, 1) == -1
    assert calc.divide(-3, -3) == 1


@pytest.mark.medium
def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        calc.divide(10, 0)


@pytest.fixture
def numbers():
    a = 10
    b = 20
    c = 25
    return [a, b, c]


def test_fixture_1(numbers):
    x = 10
    assert numbers[0] == x


def test_fixture_2(numbers):
    y = 20
    assert numbers[1] == y


@pytest.mark.parametrize("x, y, z", [(10, 1, 10), (10, 2, 100), (10, 3, 1000)])
def test_params(x, y, z):
    assert x**y == z



