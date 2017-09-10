def answer(n):
    num = int(n)
    opers = 0
    powers = []
    i = 1
    while i <= num:
        if i & num:
            powers.append(i)
        i <<= 1
    while len(powers) != 1 or powers[0] == 1:
        if powers[0] == 1 and len(powers) == 1:
                break
        elif len(powers) == 2 and powers[0] == 1 and powers[1] == 2:
            opers+=2
            del powers[1]
            break
        elif powers[0]+1 == powers[1]:
            opers += 1
            powers[0] += 1
            while powers[0] == powers[1]:
                del powers[0]
                powers[0]*=2
                if len(powers) == 1:
                    break
        elif powers[0] == 1:
            del powers[0]
            opers += 1
        else:
            powers[:] = [x/2 for x in powers]
            opers += 1
    if powers[0] != 1:
        opers += powers[0].bit_length() - 1
    return opers

print answer("47")