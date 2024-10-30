def prime_factorization(n):
    max_prime = int(n ** 0.5)
    prime = 2
    res = []
    print('0n:', n)
    cnt = 0
    while prime <= max_prime and n > 1:
        while n > 0 and n % prime == 0:
            n //= prime
            res.append(prime)
        prime += 1

    # do not forget this !!!
    if n > 1:
        res.append(n)
    return res
    
if __name__ == "__main__":
    print(prime_factorization(68))
