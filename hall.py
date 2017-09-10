def answer(s):
    salutes = 0
    people = 0
    for person in s:
        if person == '-':
            continue
        elif person == '>':
            people+=1
        else:
            salutes+=people
    return salutes*2
