number = 1

def add10():
    number += 10
    return number

number = add10()
assert(number == 11)