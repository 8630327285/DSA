def writeAsPowerofTwo(n):
    if n < 0:
        return
    PowerofTwo = []
    exponent = 0:

    while n > 0:
        if n&1 == True:
            PowerofTwo.append(2**exponent)
            exponent+=1
            n = n>>1
            print(PowerofTwo)

    