def add_everything_up(a, b):
    try:
        a + b
    except TypeError:
        a = str(a)
        b = str(b)
        print(a + b)
    else:
        print(a + b)


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
