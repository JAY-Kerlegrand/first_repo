def hypotenuse(a, b):
    """Determine the hypotenuse of a right triangle given the length of the legs"""
    s = a**2 + b**2
    c = s**(0.5)
    return c