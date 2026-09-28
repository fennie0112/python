def sep(*values):
    strings = ()
    numbers = ()

    for value in values:
        if (type(value)==str):
            strings = strings+(value,)

        else:
            numbers = numbers+(value,)

    return strings,numbers

print(sep(44,"fennie",78,"yeoboseo",7,"magsuku"))
