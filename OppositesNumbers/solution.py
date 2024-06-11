def lovefunc(fl1, fl2): # My solution
    if fl1 % 2 == 0 and fl2 % 2 != 0:
        return True
    if fl1 % 2 != 0 and fl2 % 2 == 0:
        return True
    return False


# Simplest version: return (fl1 + fl2)%2
# Sum Up flowers, then modulo 2 it will return 0 (False) or 1 (True)
# It will be always even or odd no matter, how big the number is ;)