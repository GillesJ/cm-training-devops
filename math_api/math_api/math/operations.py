from numbers import Number

def add(t1: Number, t2: Number) -> Number:
    """For two integers t1 and t2, returns t1+t2."""
    return t1 + t2


def sub(t1: Number, t2: Number) -> Number:
    """For two integers t1 and t2, returns t1-t2."""
    return t1 - t2


def div(t1: Number, t2: Number) -> Number:
    """For two integers t1 and t2, returns t1/t2."""
    if t2 == 0:
        raise ValueError("Division by 0")
    return int(t1 / t2)


def mul(t1: Number, t2: Number) -> Number:
    """For two integers t1 and t2, returns t1*t2."""
    return t1 * t2
