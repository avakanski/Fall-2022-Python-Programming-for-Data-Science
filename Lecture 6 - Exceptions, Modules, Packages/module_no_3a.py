print('Print the built-in attribute name of the module:',__name__)

X = 1
print('The value of the variable X is:', X)

def CelsiusToFahrenheit(Temperature):
    assert Temperature >= 0, 'Colder than absolute zero!'
    return ((Temperature-32)/1.8)

if __name__ == '__main__':
    print(20*'-')
    print('Self-testing')
    print('100 degrees Fahrenheit is', CelsiusToFahrenheit(100),'degrees Celsius')
    print('32 degrees Fahrenheit is', CelsiusToFahrenheit(32),'degrees Celsius')
    print('0 degrees Fahrenheit is', CelsiusToFahrenheit(0),'degrees Celsius')
    