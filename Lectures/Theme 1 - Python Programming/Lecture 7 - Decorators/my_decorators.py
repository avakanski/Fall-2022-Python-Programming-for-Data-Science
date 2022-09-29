def star(func):
    def inner():
        print('Star decorator wrapper')
        print('*' * 30)
        func()
        print('Star decorator exit')
    return inner


def percent(func):
    def inner():
        print('Percent decorator wrapper')
        print("%" * 30)
        func()
        print('Percent decorator exit')
    return inner