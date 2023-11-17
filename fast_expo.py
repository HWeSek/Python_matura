def fastExponentiation(base, exponent):
    if exponent == 0:
        return 1
    elif exponent % 2 == 0:
        halfPower = fastExponentiation(base,exponent//2)
        return halfPower * halfPower
    else:
        return base*fastExponentiation(base,exponent-1)

print(fastExponentiation(2,11))