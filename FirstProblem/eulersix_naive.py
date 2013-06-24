""" This problem is here to demonstrate the structure our code will
be following. If you can run this example, you should be fine as you
go through the rest of the problems.

This problem is based off of the Project Euler problem #6. In order
to show a little more Numpy functionality, the sizes have been increased.

Links:
http://projecteuler.net/problem=6
"""


def naive():
    x = 0
    y = 0
    for i in range(1, 1001):
        x += pow(i, 2)
        y += i
    return pow(y, 2) - x

if __name__ == '__main__':
    import eulersix_test
    eulersix_test.evaluate(naive)
