import pytest

from scripts import TRUE, FALSE, NOT, OR, NOR, XOR, XNOR, AND, NAND, IMPLICATION


@pytest.mark.parametrize('given, expected', [
    (FALSE, TRUE),
    (TRUE, FALSE),
])
def test_not(given, expected):
    assert NOT(given) is expected


@pytest.mark.parametrize('left, right, expected', [
    (FALSE, FALSE, FALSE),
    (FALSE, TRUE,  TRUE),
    (TRUE,  FALSE, TRUE),
    (TRUE,  TRUE,  TRUE),
])
def test_or(left, right, expected):
    assert OR(left)(right) is expected


@pytest.mark.parametrize('left, right, expected', [
    (FALSE, FALSE, TRUE),
    (FALSE, TRUE,  FALSE),
    (TRUE,  FALSE, FALSE),
    (TRUE,  TRUE,  FALSE),
])
def test_nor(left, right, expected):
    assert NOR(left)(right) is expected


@pytest.mark.parametrize('left, right, expected', [
    (FALSE, FALSE, FALSE),
    (FALSE, TRUE,  TRUE),
    (TRUE,  FALSE, TRUE),
    (TRUE,  TRUE,  FALSE),
])
def test_xor(left, right, expected):
    assert XOR(left)(right) is expected


@pytest.mark.parametrize('left, right, expected', [
    (FALSE, FALSE, TRUE),
    (FALSE, TRUE,  FALSE),
    (TRUE,  FALSE, FALSE),
    (TRUE,  TRUE,  TRUE),
])
def test_xnor(left, right, expected):
    assert XNOR(left)(right) is expected


@pytest.mark.parametrize('left, right, expected', [
    (FALSE, FALSE, FALSE),
    (FALSE, TRUE,  FALSE),
    (TRUE,  FALSE, FALSE),
    (TRUE,  TRUE,  TRUE),
])
def test_and(left, right, expected):
    assert AND(left)(right) is expected


@pytest.mark.parametrize('left, right, expected', [
    (FALSE, FALSE, TRUE),
    (FALSE, TRUE,  TRUE),
    (TRUE,  FALSE, TRUE),
    (TRUE,  TRUE,  FALSE),
])
def test_nand(left, right, expected):
    assert NAND(left)(right) is expected


@pytest.mark.parametrize('left, right, expected', [
    (FALSE, FALSE, TRUE),
    (FALSE, TRUE,  TRUE),
    (TRUE,  FALSE, FALSE),
    (TRUE,  TRUE,  TRUE),
])
def test_implication(left, right, expected):
    assert IMPLICATION(left)(right) is expected