def wild_braces(string):
    counter = 0
    for i in string:
        if i == '(':
            counter += 1
        elif i == ')':
            counter -= 1

    if counter == 0:
        return True
    else:
        return False




