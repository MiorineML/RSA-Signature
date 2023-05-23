# Ed Le
# CS426 - RSA
# Python 3

import random

# Splits into two functions depending on what the detected "mode" is
def signVerify():
    
    args = input().split()
    
    # If we find the first argument to be sign
    if args[0] == "sign":
        sign(" ".join(args[1:]))  
        exit()
    
    # If we find the first argument to be verify, parses the message so we can read it as one
    elif(args[0] == "verify"): 
        message = args[2]
        for i in range(3, len(args) - 1):
            message += " " + args[i]
        
        verify(args[1], message[1:-1], args[-1])
        exit()
     
def sign(m):
    
    # This strip might seem redudant, the end result will be ""hello, friend!"", which is not what we want
    m = m.strip(' "')
    h = elfHash(m)
    sKey = 65537
    
    # Allowing p/q to be random
    p = randomPrime()
    q = randomPrime()
    
    # Calculating the mod "n" and the totient
    n = q * p
    t = (p - 1) * (q - 1)
    
    print(f"p = {hex(p)[2:]}, q = {hex(q)[2:]}, n = {hex(n)[2:]}, t = {hex(t)[2:]}")
    print(f"received message: {m}")
    
    # Calculate the key x using euclid
    x = euclidean(sKey, t)
    print(f"message hash: {hex(h)[2:]}")
    print(f"signing with the following private key: {hex(x)[2:]}")
    
    # Using the mod expo to sign the msg
    signedString = modXP(n, h, x)
    print(f"signed hash: {hex(signedString)[2:]}")
    
    # Using the mod expo to verify the sig
    univert = modXP(n, signedString, sKey)
    print(f"uninverted message to ensure integrity: {hex(univert)[2:]}")
    print(f'complete output for verification: \n{hex(n)[2:]} "{m}" {hex(signedString)[2:]}')


def verify(n, m, s):
    
    h = elfHash(m)
    sKey = 65537
    
    # Necessary to convert here since we don't do it elsewhere (Change 16 here if we want bigger bits)
    univert = modXP(int(n, 16), int(s, 16), sKey)
    
    # Comparing the message hash and calculate the mod expo
    if(h == univert):
        print("message verified!")
    
    else:
        print("!!! message is forged !!!")


# Random generator for p/q
def randomPrime():
    
    sKey = 65537
    
    p = random.randint(0x8000, 0xFFFF)
    while(isPrime(p, 20) != 1):
        p = random.randint(0x8000, 0xFFFF)
    
    q = random.randint(0, sKey)
    while isPrime(q, 20) != 1:
        q = random.randint(0, sKey)
    
    return p

# Used Example: https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
def isPrime(n, trials):
    
    # Small primes
    if n <= 3:
        return True
    
    expo, rem = 0, n - 1
    
    # Determine the value of "s" and "d"
    while rem % 2 == 0:
        expo += 1
        rem //= 2
    
    # Millar-Rabin tests
    for _ in range(trials):
        x = random.randint(2, n - 2)
        x = pow(x, rem, n)
        
        # If x is not 1 or n - 1, we apply the test
        if x not in (1, n - 1):
            
            for _ in range(expo - 1):
                x = pow(x, 2, n)

                # If x is (n - 1), we have found a good "x"
                if x == n - 1:
                    break
            else:
                return False
            
    return True

def modXP(x, e, m):
    
    # For negative expo
    if (m < 0):
        
        # Mod inverse of "e" and make "m" a positive
        e = pow(e, -1, x)
        m = -m
    
    # If power raised to the 0, auto 1    
    if (m == 0):
        return 1
    
    # If power raised to the 1, it is itself
    if (m == 1):
        return e % x
    
    # If "m" is even, square and half the base
    if (m % 2 == 0):
        return modXP(x, pow(e, 2, x), m // 2) % x
    
    # If "m" is odd, square and decrement, then multiply the base
    else:
        return modXP(x, pow(e, 2, x), (m - 1) // 2) * e % x

# Used example: https://en.wikipedia.org/wiki/PJW_hash_function
def elfHash(s):
    
    i, h, high = 0, 0, 0
 
    while i < len(s):
        h = (h << 4) + ord(s[i])
        high = h & 0xF0000000
        
        if high:
            h ^= high >> 24
            
        h &= (0xFFFFFFFF ^ high)
        i += 1
        
    return h

# Used example: https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
def euclidean(a, x):
    
    t, r = 0, x
    newt, newr = 1, a
    
    t, newt = 0, 1
    r, newr = x, a
    
    while newr != 0:
        
        quotient = r // newr
        t, newt = (newt, t - quotient * newt)
        r, newr = (newr, r - quotient * newr)
        
    if (r > 1):
        print("a is not invertible")
    
    if (t < 0):
        t = t + x
        
    return t

# Starts the program       
signVerify()