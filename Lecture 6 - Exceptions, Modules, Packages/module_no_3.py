print('Print the built-in attribute name of the module:',__name__)

X = 1
print('The value of the variable X is:', X)

def CelsiusToFahrenheit(Temperature):
    assert Temperature >= 0, 'Colder than absolute zero!'
    return ((Temperature-32)/1.8)
    