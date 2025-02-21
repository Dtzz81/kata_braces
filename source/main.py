def wild_braces(string):
    counter_p = 0
    for i in string:
        if i == '(':
            counter_p += 1
        elif i == ')':
            counter_p -= 1

    counter_b = 0
    for i in string:
        if i == '[':
            counter_b += 1
        elif i == ']':
            counter_b -= 1


    if counter_p == 0 and counter_b == 0:
        return True
    else:
        return False

