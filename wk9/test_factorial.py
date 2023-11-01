from recursion import factorial
import pytest

def iterative_factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

@pytest.mark.parametrize('n',[-5, 1,5,10,10.2])
def test_recursion(n):
    v1 = iterative_factorial(n)
    v2 = factorial(n)
    assert v1 == v2