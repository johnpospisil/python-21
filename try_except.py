# A Try-Except block can help prevent crashes by
# catching errors/exceptions
# types of exceptions: https://docs.python.org/3/library/exceptions.html
try:
    num = int(input("Enter an integer: "))
    print(num)
except ValueError as err:
    print("Error: " + str(err))
else:  # runs if there are no errors
    print('No errors.')
finally:  # runs always, whether there is an exception or not
    print('Finally clause.')


# make your own exceptions classes
class ValueTooHighError(Exception):
    pass


def test_value(x):
    if x > 100:
        raise ValueTooHighError('value is too high')


print(test_value(200))


# exceptions can be raised at will too
x = -5
if x < 0:
    raise Exception('exception: x should be positive')

# assert statements - below, assert than x is gretaer than or equal to 0, raise an assert error if False
assert (x >= 0), 'x is negative'
