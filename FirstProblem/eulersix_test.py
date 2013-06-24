def evaluate(func):
    expected = 250166416500L
    result = func()
    if result != expected:
        raise Exception('Unexpected result: ', result, expected)
    print 'Expected result obtained'
